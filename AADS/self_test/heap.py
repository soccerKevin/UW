import math

class minHeap:
  def __init__(self):
    self.list = []

  def parent_index(self, i):
    return math.floor((i - 1) / 2)

  def swap(self, i, k):
    temp = self.list[i]
    self.list[i] = self.list[k]
    self.list[k] = temp

  def insert(self, value):
    self.list.append(value)
    i = len(self.list) - 1
    self.heapify_up(i)

  def heapify_up(self, current_i):
    if current_i <= 0:
      return
    current_value = self.list[current_i]
    parent_i = self.parent_index(current_i)
    parent_value = self.list[parent_i]

    if current_value < parent_value:
      self.swap(current_i, parent_i)
      self.heapify_up(parent_i)

  def root(self):
    return self.list[0]

  def print(self):
    print(self.list)

mh = minHeap()
mh.insert(20)
mh.print()
mh.insert(14)
mh.print()
mh.insert(17)
mh.print()
mh.insert(18)
mh.print()
mh.insert(8)
mh.print()
mh.insert(9)
mh.print()
mh.insert(22)
mh.print()
mh.insert(4)
mh.print()
mh.insert(2)
mh.print()
