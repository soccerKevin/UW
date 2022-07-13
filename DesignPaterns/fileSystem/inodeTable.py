from inode import INode
from uuid import uuid

# Singleton table to save inodes
class INodeTable:
  # intantiate a table
  # table must have fields
  # fileName
  # fileType
  # fileSize
  # uid
  # addresses (starting bits to blocks in memory)
  # createdAt
  # updatedAt
  def __init__(self)
    self.indexes = [self.createIndex('uid')]
    self.table = Table()
    pass

  # Creates a binary tree based on the field
  # adds all current entries if any exist
  def createUidIndex(self, fieldName):
    pass

  # add an INode to the table
  def addINode(self, inode):
    inode.uid = uuid()
    # check for uid uniqueness
    # throw error if props are invalid
    # - wrong format
    # - missing when should be present
    pass

  # returns all iNodes with the given ids
  def getInodes(self, ids):
    pass
