from heap import Heap

class StreamingMedianCalculator:
  def __init__(self, initial_values):
    self.lower_heap = Heap([])
    self.upper_heap = Heap([])

  def add_number_and_return_median(self, i: int) -> float:
    self.add_number(i)
    return self.get_median()

  def add_number(self, num):
    if (self.lower_heap.get_size() <= self.upper_heap.get_size()):
      self.lower_heap.insert_max(num)
    else:
      self.upper_heap.insert_min(num)

  def get_median(self):
    median = None
    upper_size = self.upper_heap.get_size()
    lower_size = self.lower_heap.get_size()

    if (upper_size == 0 or lower_size == 0):
      if (upper_size > 0):
        return self.upper_heap.get_root()
      else:
        return self.lower_heap.get_root()

    if (upper_size == lower_size):
      median = (self.upper_heap.get_root() + self.lower_heap.get_root()) / 2
    elif (lower_size > upper_size):
      median = self.lower_heap.get_root()
    else:
      median = self.upper_heap.get_root()
    return median

smc = StreamingMedianCalculator([])

print(smc.add_number_and_return_median(1))
print(smc.add_number_and_return_median(16))
print(smc.add_number_and_return_median(7))
print(smc.add_number_and_return_median(9))
print(smc.add_number_and_return_median(14))
print(smc.add_number_and_return_median(27))
print(smc.add_number_and_return_median(34))
print(smc.add_number_and_return_median(15))
print(smc.add_number_and_return_median(61))
print(smc.add_number_and_return_median(43))
print(smc.add_number_and_return_median(52))

