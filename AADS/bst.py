class Node:
  def __init__(self, value, left=None, right=None):
    self.value = value
    self.left  = left
    self.right = right

  def get_value(self):
    return self.value

  def get_left(self):
    return self.left

  def get_right(self):
    return self.right

  def contains(self, value):
    if self.value == value:
      return True

    if self.left:
      leftContains = self.left.contains(value)
      if leftContains:
        return leftContains

    if self.right:
      rightContains = self.right.contains(value)
      return rightContains

    return False

def createBST(array, start=0, end=None):
  if end == None:
    end = len(array)

  length = end - start
  if length == 1:
    return Node(array[start])
  elif length < 1:
    return None

  mid = start + int(length / 2)

  leftNode = createBST(array, start, mid)
  rightNode = createBST(array, (mid + 1), end)

  node = Node(array[mid], leftNode, rightNode)

  return node

def newBST(array):
  array.sort()
  return createBST(array)

def traverseBST(head):
  if head == None:
    return

  traverseBST(head.get_left())
  print(head.get_value())
  traverseBST(head.get_right())

bst = newBST([*range(0, 100)])
traverseBST(bst)
