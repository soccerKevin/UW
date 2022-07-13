const quickSearch = (array, target, start = 0, end) => {
  if (isNaN(end)) end = array.length - 1

  if (start > end) return "not found"

  const midI = Math.floor((start + end) / 2)
  const midValue = array[midI]
  if (midValue == target) return midValue

  if (target < midValue)
    return quickSearch(array, target, start, midI - 1)
  else
    return quickSearch(array, target, midI + 1, end)
}

a = [...new Array(301).keys()]
answer = quickSearch(a, 400)
console.log(answer)
