const minCoins = (coins, n, cache={ 0: 0 }) => {
  if (!isNaN(cache[n])) return cache[n]

  let minCount = Number.MAX_VALUE

  coins.forEach((coin) => {
    if (coin > n) return
    const remainder = n - coin
    smaller = 1 + minCoins(coins, remainder, cache)
    minCount = Math.min(smaller, minCount)
  })

  cache[n] = minCount
  return minCount
}

// const coins = [1, 5, 10, 25]
const coins = [25, 10, 5, 1]
count = minCoins(coins, 100)
console.log('count: ', count)
