class Memory:
  # A Singleton to handle simple memory access and allocation
  def __init__(self):
    self.totalBits = '16gb'
    # break space into blocks
    self.blockAddresses = [4096, 8192, 12288, '...']

  # Returns the data from the given blocks
  def read(self, startingBitNumber, blocksCount):
    pass

  # Writes to the given blocks
  def write(self, startingBitNumber, blocksCount):
    pass

memory = Memory()
