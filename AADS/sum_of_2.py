def sum_of_2(a, target_sum):
  dictionary = {}
  for i, x in enumerate(a):
    dictionary[x] = i

  array = a.copy()
  array.sort()
  left = 0
  right = len(array) - 1
  pairs = []

  while left <= right:
    ssum = array[left] + array[right]
    if ssum == target_sum:
      pairs.append([left, right])
      left += 1
      right -= 1
    elif ssum < target_sum:
      left += 1
    else:
      right -= 1

  if not pairs:
    return (-1, -1)

  flat_list = [item for sublist in pairs for item in sublist]
  indexes = []
  for x in flat_list:
    indexes.append(dictionary[x])
  return tuple(indexes)

a = [*range(0, 100)]
s = sum_of_2(a, 100)

print(s)
