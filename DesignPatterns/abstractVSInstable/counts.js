const { existsSync, readFileSync, promises: fsPromises } = require('fs')
const glob = require('glob')

const nodePath = require('path')
const NEO4J_PATH = nodePath.join(__dirname, 'neo4j/community')

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
    const javaFiles = await getFilesIn({ path: modulePath, match: '**/**.java', type: 'f'})
    const scalaFiles = await getFilesIn({ path: modulePath, match: '**/**.scala', type: 'f'})
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

const isAbstract = async (filePath) => {
  const contents = readFileSync(filePath, { encoding: 'utf8', flag: 'r' })
  const lowerContents = contents.toLowerCase()
  const isAbstract = lowerContents.indexOf('abstract') > -1
  const isInterface = lowerContents.indexOf('interface') > -1
  return isAbstract || isInterface
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
  return abstractCount / concreteCount
}

const run = async () => {
  const modules = await getFilesIn({ path: NEO4J_PATH, match: '/*/', type: 'd' })

  modules.forEach(async (m) => {
    const ma = await moduleAbstractness(m)
    console.log(m, ': ', ma)
  })

}

run()


module.exports = {
  getFilesIn,
}
