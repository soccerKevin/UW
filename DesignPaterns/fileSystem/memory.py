class Memory:
  # A Singleton to handle simple memory access and allocation
  def __init__(self):
    self.totalBits = '16gb'

  # Allocate n blocks in memory, starting at a given bit
  def allocate(self, startingBitNumber, blocksCount):
    pass

  # Returns the data from the given blocks
  def read(self, startingBitNumber, blocksCount):
    pass

memory = Memory()
