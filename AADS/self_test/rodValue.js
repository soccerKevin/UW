const maxRodValue = (rodLength, lengthValues) => {
  cache = { 0: 0 }
  lengths = [... new Array(rodLength + 1).keys()]
  lengths.shift()
  console.log(lengths)
  lengths.map((l) => {
    cache[l] = maxValueOfLength(l, lengthValues, cache)
  })
  console.log('cache: ', cache)
  return cache[rodLength]
}

const maxValueOfLength = (length, prices, cache) => {
  maxValue = -1
  cuts = [... new Array(length + 1).keys()]
  cuts.shift()
  console.log('cuts: ', cuts)
  console.log('cache: ', cache)
  cuts.map((cut) => {
    maxValue = Math.max(prices[cut] + cache[length - cut], maxValue)
  })

  return maxValue
}

length = 8
prices = [ 0, 1, 6, 2, 4, 3, 3, 2, 8 ]

console.log(maxRodValue(length, prices))

