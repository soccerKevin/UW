from bitarray import bitarray
from memory import Memory

# A list of bits defining which blocks in memory are used/empty
# For quick lookup, no need to iterate through memory to find empty blocks
class Bitmap:
  def __init__(self):
    self.bits = bitarray()
    pass

  # Returns the index of the first available block
  def getFirstAvailableBlock(self):
    # returns the first 0 in the bit array
    pass

  # sets the blockIndex bit to 0
  def setBlockEmpty(self, blockIndex)
    pass

bitmap = Bitmap()
