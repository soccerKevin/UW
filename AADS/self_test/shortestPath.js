randomGrid = require('./grid')

const shortestPath = (costGrid, x, y) => {
  tc = new Array(costGrid.length).fill().map(() => new Array(costGrid[0].length).fill(0))

  tc[0][0] = costGrid[0][0]

  // set first row
  for (i = 1; i < tc[0].length; i++)
    tc[0][i] = tc[0][i - 1] + costGrid[0][i]

  // set first column
  for (i = 1; i < tc.length; i++)
    tc[i][0] = tc[i - 1][0] + costGrid[i][0]

  // create the tc grid
  for (i = 1; i < tc.length; i++) {
    for (j = 1; j < tc[0].length; j++) {
      tc[i][j] = Math.min(tc[i - 1][j - 1], tc[i][j - 1], tc[i - 1][j]) + costGrid[i][j]
    }
  }

  console.log('tc: ', tc)
  const cost = tc[y - 1][x - 1]
  return cost
}


costGrid = randomGrid(5, 5, 20, 1)
// costGrid = [ [ 1, 2, 3 ],
//              [ 4, 8, 2 ],
//              [ 1, 5, 3 ] ]
console.log('costGrid: ', costGrid)
console.log(shortestPath(costGrid, 3, 4))
