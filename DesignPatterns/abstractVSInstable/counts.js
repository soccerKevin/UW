const { existsSync, promises } = require('fs')

const path = require('path')

const neo4jDir = path.join(__dirname, 'neo4j/community')

const getFilesIn = async (path, type=null) => {
  let directories = null


  if (!existsSync(path))
    throw new Error('No such path')

  const stat = await promises.lstat(path)
  if (!stat.isDirectory())
    throw new Error('No such directory')

  const files = await promises.readdir(path, { withFileTypes: true })

  if (type == 'd')
    return files.filter((file) => file.isDirectory()).map((dir) => dir.name)
  if (type == 'f')
    return files.filter((file) => !file.isDirectory()).map((dir) => dir.name)

  return files.map((dir) => dir.name)
}

const javaPath = 'src/main/java/org/neo4j'

const run = async () => {
  const modules = await getFilesIn(neo4jDir, 'd')

  modules.forEach(async (m) => {
    const javaClassesDir = path.join(neo4jDir, m, javaPath)
    try {
      const components = await getFilesIn(javaClassesDir, 'f')
      console.log(`${javaClassesDir}: `, components)
    }
    catch (err){
      if (err.message == 'No such path')
        console.log('No such path: ', javaClassesDir)

      else if (err.message == 'No such directory')
        console.log('No such directory: ', javaClassesDir)
    }
  })
}

run()


module.exports = {
  getFilesIn,
}
