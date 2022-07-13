import math
import traceback

class Heap:
  def __init__(self, elements=[]):
    self.size = len(elements)
    self.elements = elements

  def print(self):
    print(self.elements)

  def get_root(self):
    if (len(self.elements) > 0):
      return self.elements[0]
    else:
      return None

  def get_size(self):
    return self.size

  def parent_i(self, i):
    return math.floor((i - 1) / 2)

  def left_child_i(self, i):
    return 2 * i + 1

  def right_child_i(self, i):
    return 2 * i + 2

  def is_leaf(self, i):
    return (self.size / 2) < i <= self.size

  def swap(self, x, y):
    if (x < 0 or y < 0):
      raise Exception('stopping')

    a = self.elements[x]
    self.elements[x] = self.elements[y]
    self.elements[y] = a

  def min_heapify(self, i):
    if (self.is_leaf(i)):
      return None

    elem = self.elements[i]
    left_i = self.left_child_i(i)
    left_child = self.elements[left_i]
    right_i = self.right_child_i(i)
    right_child = self.elements[right_i]

    if (elem > left_child or elem > right_child):
      if (left_child < right_child):
        self.swap(i, left_i)
        self.min_heapify(left_i)
      else:
        self.swap(i, right_i)
        self.min_heapify(right_i)

  def max_heapify(self, i):
    if (self.is_leaf(i)):
      return None

    elem = self.elements[i]
    left_i = self.left_child_i(i)
    left_child = self.elements[left_i]
    right_i = self.right_child_i(i)
    right_child = self.elements[right_i]

    if (elem < left_child or elem < right_child):
      if (left_child > right_child):
        self.swap(i, left_i)
        self.max_heapify(left_i)
      else:
        self.swap(i, right_i)
        self.max_heapify(right_i)

  def insert_min(self, elem):
    self.elements.append(elem)
    if (self.size == 0):
      self.size += 1
      return

    current = self.size
    parent_i = self.parent_i(current)

    while (parent_i > -1 and self.elements[current] < self.elements[parent_i]):
      self.swap(current, parent_i)
      current = parent_i
      parent_i = self.parent_i(current)

    self.size = len(self.elements)

  def insert_max(self, elem):
    self.elements.append(elem)
    if (self.size == 0):
      self.size += 1
      return

    current = self.size
    parent_i = self.parent_i(current)

    while (parent_i > -1 and self.elements[current] > self.elements[parent_i]):
      self.swap(current, parent_i)
      current = parent_i
      parent_i = self.parent_i(current)

    self.size = len(self.elements)

  def insert(self, elem):
    self.elements.append(elem)
    if (self.size == 0):
      self.size += 1
      return

    current = self.size
    parent_i = self.parent_i(current)

    while (parent_i > -1 and self.elements[current] > self.elements[parent_i]):
      self.swap(current, parent_i)
      current = parent_i
      parent_i = self.parent_i(current)

    self.size = len(self.elements)

# inp = [1, 16, 7, 9, 14, 27, 34, 15, 61, 43, 52]
# heap = Heap([])
# for i, x in enumerate(inp):
#   heap.insert(x)
# heap.print()
