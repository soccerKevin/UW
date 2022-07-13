const pairSum = (array, target) => {
  const hash = {}
  answers = []
  array.forEach((num) => {
    remainder = target - num
    if (hash[remainder])
      answers.push([num, remainder])
    else
      hash[num] = true
  })
  return answers
}

target = 22

nums = [ 10, 20, 7, 14, 12, 8, 2, 4, 3, 9]

sums = pairSum(nums, target)
console.log(sums)
