from bst import newBST

def intersection_binary(array1, array2):
  array1.sort()
  array2.sort()
  smallArray = None
  largeArray = None

  if len(array1) < len(array2):
    smallArray = array1
    largeArray = array2
  else:
    smallArray = array2
    largeArray = array1

  largeBST = newBST(largeArray)
  intersection = []

  for value in smallArray:
    if largeBST.contains(value):
      intersection.append(value)

  return intersection
