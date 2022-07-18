class Stream:
  def __init__(self, memory):
    # pass in memory, so memory types can be swapped out (dependency injection)
    self.memory = memory
    self.startingBitIndex = -1

  # opens a connection to memory
  # points to the starting bit index in memory
  def open(self, startingBitIndex=0)
    self.startingBitIndex = startingBitIndex
    # create connection to memory

  def movePointer(self, startingBitIndex):
    self.startingBitIndex = startingBitIndex

  # closes the connection to memory
  def close(self)
    # throw error if no connection
    pass
