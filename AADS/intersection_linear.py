def intersection_linear(array1, array2):
  array1.sort()
  array2.sort()
  matches = []
  i1 = 0
  i2 = 0

  while i1 < len(array1) and i2 < len(array2):
    elem1 = array1[i1]
    elem2 = array2[i2]

    if elem1 < elem2:
      i1 += 1
    elif elem1 > elem2:
      i2 += 1
    else:
      matches.append(elem1)
      i1 += 1
      i2 += 1

  return matches
