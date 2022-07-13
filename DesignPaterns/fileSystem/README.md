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

### bitmap
An array of bits to easily find the next open block in memory

### directory
A special type of file

### file
Handles file crud

### fileSystem
Takes commands from the user

### inode
Information about a file

### inodeTable
Table of inodes

### memory
Free/used bits of space

### stream
A Portal into the memory
