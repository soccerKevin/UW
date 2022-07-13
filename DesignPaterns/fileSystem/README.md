# A Simple in memory file system design

## Classes
- bitmap
- config
- directory
- file
- fileSystem
- inode
- inodeTable
- memory
- stream

### directory
A special type of file.  It's contents it's a list of inodes, ie files

### file
Handles file crud
uses streams to write to memory

### fileSystem
Takes commands from the user
allows users to manipulate files/directories
allows users to search for files/directories
manages permissions

### inode
Information about a file

### inodeTable
Table of inodes

### memory
Free/used bits of space
Has a bitmap
- bitmap
An array of bits to easily find the next open block in memory

### stream
A Portal into the memory
Makes reading and writing to memory easier
Gives permissions to write to other objects
