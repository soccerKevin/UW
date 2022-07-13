from datetime import datetime

class INode:
  def __init__(self, fileType, permissions):
    self.fileType = fileType
    self.permissions = permissions
    self.createdAt = datetime.now()
    self.updatedAt = datetime.now()


