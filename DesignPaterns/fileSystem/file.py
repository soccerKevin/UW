from inode import inode

# A File is an inode for basic information and some data in memory
class File:
  def __init__(self, inode):
    self.inode = inode

  def update(self):
    pass

  def write(self):
    pass

  def read(self):
    pass

  def delete(self):
    pass
