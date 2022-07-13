import random_array
from quicksort import quick_sort
from time import time

def run_quick_sort(pivot_style='rnd', array=None):
  if array == None:
    array = random_array.create_array(100000, 100000)
  # print(array)

  start = time()

  quick_sort(array, 0, len(array))

  end = time()

  delta = end - start

  # print(array)

print(len(range(0, 1000)))

pivot_styles = ['rnd', 'mid', 'start', 'end']
total_run_times = { 'rnd': 0, 'mid': 0, 'start': 0, 'end': 0 }

for i in range(0, 100):
  print(i)
  nums_base = random_array.create_array(100000, 100000)

  for style in pivot_styles:
    nums = nums_base.copy()

    start = time()
    run_quick_sort(style, nums)
    end = time()

    delta_time = end - start
    total_run_times[style] += delta_time

for style in pivot_styles:
  run_time = total_run_times[style]
  print(style, "total: ", run_time, '.  avg: ', run_time / len(range(0, 1000)))
