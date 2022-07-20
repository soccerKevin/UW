
const { existsSync, readFileSync, writeFileSync, promises: fsPromises } = require('fs')
const { XMLParser } = require('fast-xml-parser')
const _ = require('lodash');
const xmlParser = new XMLParser()
const glob = require('glob')
const Bluebird = require('bluebird')
const nodePath = require('path')
const NEO4J_PATH = nodePath.join(__dirname, 'neo4j/community')

const csvFile = 'abstractnessVsInstability.csv'
const modulesFinal = {}
const incomingDependencies = {}
const outgoingDependencies = {}
const modulesAbstractness = {}

const getFilesIn = async ({ path, match='/**', type=null }) => {
  let directories = null

  const statPath = path.slice(-1) == '/' ? path.slice(0, -1) : path
  if (!existsSync(statPath)) {
    throw new Error('No such path')
  }

  const stat = await fsPromises.lstat(statPath)
  if (!stat.isDirectory())
    throw new Error('No such directory')

  const filePaths = glob.sync(path + match)

  if (type == 'd')
    return filePaths.filter(async (filePath) => {
      const stat = await fsPromises.lstat(filePath)
      return stat.isDirectory()
    })

  if (type == 'f')
    return filePaths.filter(async (filePath) => {
      const stat = await fsPromises.lstat(filePath)
      return !stat.isDirectory()
    })

  return filePaths
}

const getModuleCodeFiles = async (modulePath) => {
  try {
    const javaFiles = await getFilesIn({ path: modulePath, match: '**/**.java', type: 'f' })
    const scalaFiles = await getFilesIn({ path: modulePath, match: '**/**.scala', type: 'f' })
    const files = javaFiles.concat(scalaFiles)
    return files
  }
  catch (err) {
    if (err.message == 'No such path')
      console.log('No such path: ', modulePath)

    else if (err.message == 'No such directory')
      console.log('No such directory: ', modulePath)

    else
      console.log(err)
  }
}

const getFileContents = (filePath) =>
  readFileSync(filePath, { encoding: 'utf8', flag: 'r' })

const isAbstract = async (filePath) => {
  const contents = getFileContents(filePath)
  const lowerContents = contents.toLowerCase()
  return !!lowerContents.match(/(public|protected) (abstract|interface)/gm)
}

const moduleAbstractness = async (modulePath) => {
  const mFiles = await getModuleCodeFiles(modulePath)
  const files = []
  await mFiles.map(async (filePath) => {
    const abstract = await isAbstract(filePath)
    files.push({ path: filePath, isAbstract: abstract })
  })

  const abstractCount = files.filter((f) => f.isAbstract).length
  const concreteCount = files.length - abstractCount
  const abstractness = abstractCount / files.length
  return { abstractCount, concreteCount, abstractness }
}

const setModuleDepencies = async (modulePath) => {
  const pomFiles = await getFilesIn({ path: modulePath, match: '**/pom.xml', type: 'f' })
  const xml = getFileContents(pomFiles[0])
  const parsedXML = xmlParser.parse(xml)

  const dependencies = [parsedXML.project.dependencies.dependency].flat()
  const artifactIds = dependencies.map((d) => d.artifactId.replace('neo4j-', ''))
  const name = getModuleName(modulePath)
  modulesFinal[name].incomingDependencies = modulesFinal[name].incomingDependencies.concat(artifactIds)

  artifactIds.forEach((dependency) => {
    if (!modulesFinal[dependency]) return
    if (modulesFinal[dependency].outgoingDependencies.indexOf(name) < 0)
      modulesFinal[dependency].outgoingDependencies.push(name)
  })
}

const getModuleName = (modulePath) => modulePath.split('/').slice(-2, -1)[0].replace('neo4j-', '')

const run = async () => {
  const modules = await getFilesIn({ path: NEO4J_PATH, match: '/*/', type: 'd' })
  modules.forEach((mPath) => {
    modulesFinal[getModuleName(mPath)] = {
      incomingDependencies: [],
      outgoingDependencies: []
    }
  })

  await Bluebird.map(modules, async (mPath) => {
    const name = getModuleName(mPath)
    await setModuleDepencies(mPath)
    const abstractness = await moduleAbstractness(mPath)
    mf = { ...modulesFinal[name], ...abstractness }
    const inDep = _.uniq(mf['incomingDependencies']).length
    const outDep = _.uniq(mf['outgoingDependencies']).length
    mf.instability = inDep / (inDep + outDep)
    modulesFinal[name] = mf
  })

  // console.log('modulesFinal: ', modulesFinal)

  let chartData = Object.entries(modulesFinal).map(([name, { abstractness, instability }]) => {
    return { name, abstractness, instability }
  })

  chartData = chartData.filter((cd) => !['zstd-proxy', 'community'].includes(cd.name))

  console.log('chartData: ', chartData)
  const csvData = chartData.map(({ name, abstractness, instability }) => name + ', ' + abstractness + ', ' + instability).join('\r\n')
  const header = 'Name, Abstractness, Instability \r\n'
  const csvText = header + csvData
  console.log('csvText: ', csvText)

  writeFileSync(csvFile, csvText)
}

run()


module.exports = {
  getFilesIn,
}
