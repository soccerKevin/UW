from directory import Directory

class FileSystem:
  def __init__(self):
    self.rootDirectory = Directory('/', 'rw-r--r--')
    self.currentDirectory = self.rootDirectory
    pass

  # Find directory and make it the current one
  def cd(self, path):
    pass

  # makes a directory in this one
  def mkdir(self, name):
    pass

  # Updates the UpdatedAt field of a file
  # If no file exists in the current directory, create one
  def touch(self, name):
    pass

  # If file exists remove it
  # Or try to remove directory (under the correct conditions)
  def rm(self, path):
    pass

  # Outputs file contents to stdout
  def cat(self, path):
    pass

  # returns current Directory
  def pwd(self):
    return self.currentDirectory

  # Lists directories and files (all inodes) in current directory
  def ls(self, path=''):
    pass

  # Creates a new inode
  # Copies contents of file
  def cp(self, name):
    pass

  # Moves file from filePath to toPath
  def mv(self, filePath, toPath):
    pass

  # Update the permissions on a file
  def chmod(self, filePath, permissions):
    pass

filySystem = FileSystem()
