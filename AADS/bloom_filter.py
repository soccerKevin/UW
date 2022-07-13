import hashlib

class BloomFilter:
  def __init__(self, size):
    self.size = size
    self.digestDictionary = {
      'sha256':  [0] * size,
      'md5':     [0] * size,
      'blake2b': [0] * size,
    }

  def callHash(self, function, value):
    if hasattr(hashlib, function):
      func = getattr(hashlib, function)

      if callable(func):
        return func(value)

  def hash(self, function, value):
    h = self.callHash(function, value.encode())
    hexCode = h.hexdigest()
    return int(hexCode, 16)

  def get_i(self, digest):
    return int(digest % self.size)

  def get_bit(self, digest):
    bitI = int(digest % 32)
    return 2 ** (bitI - 1)

  def add(self, value):
    for hashFunc in self.digestDictionary.keys():
      digest = self.hash(hashFunc, value)
      hashList = self.digestDictionary[hashFunc]
      i = self.get_i(digest)
      bit = self.get_bit(digest)
      integer = hashList[i]
      bitOr = integer | bit
      self.digestDictionary[hashFunc][i] = bitOr

  def contains(self, value):
    for hashFunc in self.digestDictionary.keys():
      digest = self.hash(hashFunc, value)
      hashList = self.digestDictionary[hashFunc]
      i = self.get_i(digest)
      bit = self.get_bit(digest)
      integer = hashList[i]
      contains = integer & bit

      if not contains:
        return False
    return True

  def print(self):
    for hashFunc in self.digestDictionary.keys():
      print(hashFunc, self.digestDictionary[hashFunc])


bf = BloomFilter(1000)
bf.add('hello')
bf.add('starcraft 2')
bf.add('chess')
bf.add('twitch')

print('hello: ', bf.contains('hello'))
print('smurf: ', bf.contains('smurf'))
