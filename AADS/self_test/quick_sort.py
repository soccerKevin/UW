# in place
# O(nlog(n))
import random
import math

def quick_sort(l, start=0, end=None):
  if end is None:
    end = len(l)

  if end <= start:
    return


  pivot_i = math.floor((start + end) / 2)
  pivot = l[pivot_i]
  switch(l, start, pivot_i)
  low_i = start + 1

  for i in range(start + 1, end):

    if l[i] < pivot:
      switch(l, i, low_i)
      low_i += 1

  new_pivot_i = low_i - 1
  switch(l, start, new_pivot_i)
  quick_sort(l, start, new_pivot_i)
  quick_sort(l, new_pivot_i + 1, end)


def switch(l, i, k):
  temp = l[i]
  l[i] = l[k]
  l[k] = temp


a = list(range(0, 300))
random.shuffle(a)
quick_sort(a)
print(a)
