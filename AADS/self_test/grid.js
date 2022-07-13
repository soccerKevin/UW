const randomGrid = (n=10, m=10, max=10, min=0) =>
  new Array(n).fill(5).map((n) =>
    new Array(m).fill(5).map((m) =>
      Math.floor(Math.random() * (max - min)) + min
    )
  )

module.exports = randomGrid
