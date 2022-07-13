const createRange = (range) => {
  const r = []
  for (i = range[0]; i <= range[1]; i++) {
    r.push(i)
  }
  return r
}

const concatenateRanges = (ranges) => {
  const fullRanges = ranges.map((range) => createRange(range))
  return joinRange(0, fullRanges)
}

const joinRange = (i, fullRanges) => {
  const currentRange = fullRanges[i]
  if (i + 1 >= fullRanges.length) return currentRange

  const numbers = joinRange(i + 1, fullRanges)

  return currentRange.map((n) => numbers.map((num) => parseInt(`${n}${num}`))).flat()
}

const ranges = [[2, 20], [1, 20], [1, 20]]
const sorted = concatenateRanges(ranges)
// console.log(sorted)
