from intersection_linear import intersection_linear
from intersection_binary import intersection_binary
import random_array

def print_intersection_linear():
  a1 = list(range(1, 1000))
  a2 = random_array.create_array()

  intersection = intersection_linear(a1, a2)
  print('intersection_linear:', intersection_linear)


def print_intersection_binary():
  array1 = [*range(0, 100)]
  array2 = [*range(0, 1000)]

  intersection_b = intersection_binary(array1, array2)
  print('intersection: ', intersection_b)

print_intersection_binary()
