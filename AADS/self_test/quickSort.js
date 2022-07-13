const shuffle = (array) => {
  for (var i = array.length - 1; i > 0; i--) {
    var j = Math.floor(Math.random() * (i + 1));
    var temp = array[i];
    array[i] = array[j];
    array[j] = temp;
  }
}

const pickPivot = (start, end) => Math.floor((start + end) / 2)

const swap = (array, i, k) => {
  temp = array[i]
  array[i] = array[k]
  array[k] = temp
}

const partition = (array, start, end, pivotI) => {
  pivotValue = array[pivotI]
  swap(array, start, pivotI)
  lowI = start + 1

  for (i = start + 1; i <= end; i++) {
    if (array[i] < pivotValue) {
      swap(array, i, lowI)
      lowI++
    }
  }

  finalPivotI = lowI - 1
  swap(array, start, finalPivotI)

  return finalPivotI
}

const quickSort = (array, start=0, end) => {
  if (isNaN(end)) end = array.length - 1
  if (start >= end) return

  pivotI = pickPivot(start, end)
  finalPivotI = partition(array, start, end, pivotI)
  quickSort(array, start, finalPivotI)
  quickSort(array, finalPivotI + 1, end)
}

const a = [...Array(301).keys()]
shuffle(a)
console.log(a)
quickSort(a)
console.log(a)
