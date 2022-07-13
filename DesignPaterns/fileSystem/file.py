from memory import memory
from stream import Stream
from inode import INode
from bitmap import bitmap

# A File is 2 parts, the inode (metadata) and some space/content in memory
# contains methods to work with
class File:
  def __init__(self, name):
    self.inode = inode

  # writes bits to memory
  def write(self, content):
    # break into block sized chunks
    # for block in blocks
      # open stream
      # writes from stream until end
      # close stream
    self.inode.fileSize = 'number of bits'
    pass

  # Returns the contents of the file from memory
  def read(self):
    # open stream
    # read from stream until end
    # close stream
    # return contents
    pass

  # Deletes the file from memory
  def delete(self):
    # delete content from memory
    # delete inode from table
    pass

  # Returns a read stream to read bits chunk by chunk
  def readStream(self):
    pass

  # Returns a write stream to write bits chunk by chunk
  def writeStream(self):
    pass

