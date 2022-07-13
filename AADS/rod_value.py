from typing import Tuple, List

class RodLengthCalculator:
  def __init__(self, rod_length, price_array):
    self.length = length
    self.prices = price_array

  def find_max_value_top_down_memoization(self, length=None, cache={}) -> Tuple[int, List[int]]:
    if length is None:
      length = self.length

    if length < 1:
      return 0

    if cache.get(length) is not None:
      return cache[length]

    current_max = -1
    for cut in range(1, length + 1):
      current_max = max(self.prices[cut] + self.find_max_value_top_down_memoization(length - cut, cache), current_max)

    cache[length] = current_max
    return current_max

  def find_max_value_bottom_up(self, length=None) -> Tuple[int, List[int]]:
    if length is None:
      length = self.length

    cache = { 0: 0 }
    for cut in range(1, length + 1):
      cache[cut] = self.max_value_for_length(cut, cache)

    return cache[length]

  def max_value_for_length(self, length, cache):
    max_value = -1
    for cut in range(1, length + 1):
      max_value = max(self.prices[cut] + cache[length - cut], max_value)

    return max_value

length = 8
prices = [ 0, 1, 6, 2, 4, 3, 3, 2, 8 ]
calc = RodLengthCalculator(length, prices)
print('top down: ', calc.find_max_value_top_down_memoization())
print('bottom up: ', calc.find_max_value_bottom_up())
