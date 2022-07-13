from file import File

# Directories are just files
# The data of a directory is a list of inode uids
class Directory(File):
  def __init__(self, inode):
    super().__init__(inode)
