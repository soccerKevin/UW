from file import File

# Directories are just files
# The data of a directory is a list of inode uids
# Liskovs principle
#  does not override superclass functionality
class Directory(File):
  def __init__(self, name):
    super().__init__(name)

  # Adds an inode to the content
  def addINode(self, inode):
    # literally just adds ', inodeId' to content
    pass

  def addFile(self, file):
    self.addINode(file.inode)

