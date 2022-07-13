import math
import random

def swap(array, i1, i2):
  elem = array[i1]
  array[i1] = array[i2]
  array[i2] = elem

def choose_pivot(start, end, style):
  if style == 'rnd':
    return random.randint(start, end - 1)
  elif 'mid':
    return math.floor((start + end) / 2)
  elif 'start':
    return start
  elif 'end':
    return end

def partition(array, start, end, pivot_index):
  pivot_value = array[pivot_index]
  swap(array, start, pivot_index)

  s = start + 1
  left = s
  for i in range(s, end):
    if (array[i] < pivot_value):
      swap(array, i, left)
      left += 1

  final_pivot_index = left - 1
  swap(array, start, final_pivot_index)

  return final_pivot_index

def quick_sort(array, start = 0, end = None, pivot_style = 'rnd'):
  if end == None:
    end = len(array)

  if start >= end:
    return

  pivot_index = choose_pivot(start, end, pivot_style)
  pivot_final_index = partition(array, start, end, pivot_index)

  quick_sort(array, start, pivot_final_index)
  quick_sort(array, pivot_final_index + 1, end)

  return array

