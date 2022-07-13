from memory import memory
from stream import Stream
from inode import INode

# Open/Closed Principle
#  subclass (Directory)
#  directory shouldn't override methods in File

# A File is 2 parts, the inode (metadata) and some space/content in memory
# contains methods to work with
class File:
  # private constructor
  # use create, createFromInode
  def __init__(self, inode):
    self.inode = inode

  # writes bits to memory
  # protected
  def _write(self, content):
    # break into block sized chunks
    # finds open memory
    # for block in blocks
      # open stream
      # writes from stream until end
      # close stream
    self.inode.fileSize = 'number of bits'
    pass

  # Returns the contents of the file from memory
  # protected
  def _read(self):
    # open stream
    # read from stream until end
    # close stream
    # return contents
    pass

  # Deletes the file from memory
  # protected
  def _delete(self):
    # delete content from memory
    # delete inode from table
    pass

  # Returns a read stream to read bits chunk by chunk
  # protected
  def _readStream(self):
    pass

  # Returns a write stream to write bits chunk by chunk
  # protected
  def _writeStream(self):
    pass

  # creates a new file, unsaved
  # returns the inode for saving, if you want
  def create(self, name):
    self.name = name
    self.inode = 'create empty inode'

  # creates a new file object from an inode
  def createFromInode(self, inode):
    # if you forget about file (pretending it were persistent)
      # find it's inode
      # create a new file object from it
    pass

