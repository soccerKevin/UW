# def flatten(_list):
#   flat = []
#   for i in _list:
#     if isinstance(i, list):
#       i = flatten(i)
#       flat += i
#     else:
#       flat.append(i)
#   return flat

# l = [1, 2, [3, [4, [5]]], [6, [7]], 8, 9, [10, 11, [12, 13, [14]]]]
# print(l)
# print(flatten(l))

# # string splicing
# s = 'barney stinson'
# print(s[:-4])
# print(s[:-3])
# print(s[:-2])


# a = [1, 2, 3, 4, 5, 6, 7]
# m = tuple(map(lambda n: n + 1, a))
# print(m)
