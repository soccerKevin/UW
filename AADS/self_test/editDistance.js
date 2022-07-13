const editDistance = (str1, str2) => {
  cache = new Array(str1.length + 1).fill(0).map(() => new Array(str2.length + 1).fill(0))

  for (i = 0; i < str1.length + 1; i++) {
    for (j = 0; j < str2.length + 1; j++) {
      if (i == 0) {
        cache[0][j] = j
      }
      else if (j == 0) {
        cache[i][0] = i
      }
      else if (str1[i - 1] == str2[j - 1]) {
        cache[i][j] = cache[i - 1][j - 1]
      }
      else {
        cache[i][j] = 1 + Math.min(cache[i][j - 1], cache[i - 1][j], cache[i - 1][j -1])
      }
    }
  }

  return cache[str1.length][str2.length]
}

w1 = 'intention'
w2 = 'execution'

console.log(editDistance(w1, w2))
