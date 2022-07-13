const bfs = (graph, start=0) => {
  const aIndex = 'a'.charCodeAt(0)
  const searchedNodes = []
  const visited = {}
  const queue = [start]

  while (queue.length) {
    const i = queue.shift()
    const char = String.fromCharCode(i + aIndex)

    if (visited[char]) continue

    visited[char] = true
    searchedNodes.push(char)

    const edges = graph[i]
    edges.split('').forEach((edgeChar) => {
      const edgeI = edgeChar.charCodeAt(0) - aIndex
      queue.push(edgeI)
    })
  }

  return searchedNodes
}

const aIndex = 'a'.charCodeAt(0)
const searchedNodes = []
const visited = {}

const dfs1 = (graph, i) => {
  const char = String.fromCharCode(i + aIndex)
  if (visited[char]) return
  visited[char] = true
  searchedNodes.push(char)

  const edges = graph[i]
  edges.split('').forEach((edgeChar) => {
    const edgeI = edgeChar.charCodeAt(0) - aIndex
    return dfs1(graph, edgeI)
  })

  return searchedNodes
}

const dfs2 = (graph, start=0) => {
  const aIndex = 'a'.charCodeAt(0)
  const searchedNodes = []
  const visited = {}
  const stack = [start]

  while (stack.length) {
    const i = stack.pop()
    const char = String.fromCharCode(i + aIndex)

    if (visited[char]) continue

    visited[char] = true
    searchedNodes.push(char)

    const edges = graph[i]
    edges.split('').forEach((edgeChar) => {
      const edgeI = edgeChar.charCodeAt(0) - aIndex
      stack.push(edgeI)
    })
  }

  return searchedNodes
}

graph = ['e', 'cehi', 'bg', 'f', 'fba', 'de', 'c', 'ib', 'bh']
// console.log(bfs(graph, 1))
console.log(dfs1(graph, 1))
console.log(dfs2(graph, 1))
