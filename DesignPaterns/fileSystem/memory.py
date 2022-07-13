from bitarray import bitarray

class Memory:
  # A Singleton to handle simple memory access and allocation
  def __init__(self):
    self.totalBits = '16gb'

    # break space into blocks
    self.blockAddresses = [4096, 8192, 12288, '...']

    # A list of bits defining which blocks in memory are used/empty
    # For quick lookup, no need to iterate through memory to find empty blocks
    self.bitmap = bitarray()

  # Returns the data from the given blocks
  def read(self, startingBitNumber, blocksCount):
    pass

  # Writes to the given blocks
  def write(self, startingBitNumber, blocksCount):
    pass

  # Returns the index of the first available block
  def getFirstAvailableBlock(self):
    # returns the first 0 in the bit array
    pass

  # sets the blockIndex bit to 0
  def setBlockEmpty(self, blockIndex)
    pass

memory = Memory()
