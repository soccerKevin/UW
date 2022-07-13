// end = NaN
// if (!end) end = 1
// console.log('end: ', end)

// a = [0, 1, 2, 3]
// console.log('a.length: ', a.length)

// console.log([... new Array(11).keys()])
// const a = new Array(64)
// a[4] = 5
// console.log(a)

// str = 'laksjdf'
// console.log(str[0])

a = parseInt(0)
a = a | (1 << 4)
a = a | (1 << 6)
five = a & (1 << 5)
console.log(a)
console.log(five)

bits = (5).toString(2)
console.log(typeof(bits))
