from inode import INode

# Singleton table to save inodes
class INodeTable:
  def __init__(self)
    # intantiate a table
    # table must have fields
    # fileType
    # uid
    # duid (directory uid)
    # fileSize
    # addresses (starting bits to blocks in memory)
    # createdAt
    # updatedAt
    pass

  # add an INode to the table
  def addINode(self, inode):
    pass

  # returns all iNodes with the given ids
  def getInodes(self, ids):
    pass
