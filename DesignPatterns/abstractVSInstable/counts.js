const { existsSync, promises } = require('fs')
const glob = require('glob')

const {
  NEO4J_PATH,
  SRC_PATH,
  JAVA_PATH
} = require('./const')

const getFilesIn = async ({ path, match='/**', type=null }) => {
  let directories = null

  const statPath = path.slice(-1) == '/' ? path.slice(0, -1) : path
  if (!existsSync(statPath)) {
    throw new Error('No such path')
  }

  const stat = await promises.lstat(statPath)
  if (!stat.isDirectory())
    throw new Error('No such directory')

  const filePaths = glob.sync(path + match)

  if (type == 'd')
    return filePaths.filter(async (filePath) => {
      const stat = await promises.lstat(filePath)
      return stat.isDirectory()
    })

  if (type == 'f')
    return filePaths.filter(async (filePath) => {
      const stat = await promises.lstat(filePath)
      return !stat.isDirectory()
    })

  return filePaths
}

const getModuleFiles = async (modulePath) => {
  try {
    const javaFiles = await getFilesIn({ path: modulePath, match: '**/**.java', type: 'f'})
    const scalaFiles = await getFilesIn({ path: modulePath, match: '**/**.scala', type: 'f'})
    const components = javaFiles.concat(scalaFiles)
    return components
  }
  catch (err){
    if (err.message == 'No such path')
      console.log('No such path: ', modulePath)

    else if (err.message == 'No such directory')
      console.log('No such directory: ', modulePath)

    else
      console.log(err)
  }
}

const run = async () => {
  const modules = await getFilesIn({ path: NEO4J_PATH, match: '/*/', type: 'd' })
  console.log('modules: ', modules)

  modules.forEach(async (m) => getModuleFiles(m))
}

run()


module.exports = {
  getFilesIn,
}
