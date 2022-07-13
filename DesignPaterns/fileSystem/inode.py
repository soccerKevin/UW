from datetime import datetime
from config import BLOCK_SIZE

# Inodes are metadata for a file/directory
# fileName
# fileType (None = file (default), 'd' = directory)
# fileSize
# permissions (canRead, canWrite, canExecute (user, group, anyone))
#   ex: rwxr-x-r--
#   current user can read/write/execute,
#   the group can read/execute,
#   anyone can read
# createdAt
# updatedAt
class INode:
  def __init__(self, fileName, fileType, permissions):
    self.fileName = fileName
    self.fileType = fileType
    self.fileSize = fileSize
    self.uid = uid
    self.permissions = permissions
    # array of startingBitIndexes in memory (start of each block)
    self.address = []
    self.createdAt = datetime.now()
    self.updatedAt = datetime.now()

  # Adds a new memory location
  # saves where the block in memory starts
  def addMemoryAddress(self, startingBitIndex):
    self.address.push(startingBitIndex)

  # updates the size of the file
  def setFileSize(self, size):
    self.fileSize = size
