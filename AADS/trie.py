class ArrayTrieNode:
  alphabetSize = 26
  aIndex = ord('a')

  def __init__(self, word=None):
    self.alphabet = [None] * ArrayTrieNode.alphabetSize
    self.isEndOfWord = False

    if word is not None:
      self.add(word)

  def add(self, word):
    if len(word) < 1: return

    self.isEndOfWord = self.isEndOfWord or len(word) < 2

    char = word[0]
    i = ord(char.lower()) - ArrayTrieNode.aIndex
    w = word[1:]

    if self.alphabet[i]:
      self.alphabet[i].add(w)
    else:
      self.alphabet[i] = ArrayTrieNode(w)

  def contains(self, word):
    if len(word) < 1:
      return self.isEndOfWord

    char = word[0]
    i = ord(char.lower()) - ArrayTrieNode.aIndex
    w = word[1:]

    if self.alphabet[i] is None:
      return False
    else:
      return self.alphabet[i].contains(w)

  def getWordsWithPrefix(self, prefix):
    return self.getStringsWithPrefix(prefix, True)

  def getStringsWithPrefix(self, prefix, isWord=False):
    words = []
    for word in self.__getStrings(prefix, isWord):
      if '*' in word:
        word = word[:-1]

      if prefix in word:
        words.append(word)
    return words

  def __getStrings(self, prefix, isWord=False):
    strings = []
    items = []

    if not prefix:
      for i, node in enumerate(self.alphabet):
        if not node: continue

        char = chr(i + ArrayTrieNode.aIndex)
        items.append([char, node])

    else:
      char = prefix[0].lower()
      i = ord(char) - ArrayTrieNode.aIndex
      nextNode = self.alphabet[i]

      if nextNode:
        items = [[char, nextNode]]

    for char, node in items:
      for s in (['*' if self.isEndOfWord else ''] + node.__getStrings(prefix[1:] if prefix else '', isWord)):
        if not isWord or '*' in s:
          strings.append(char + s)

    return strings

arrayTrie = ArrayTrieNode('smurf')
arrayTrie.add('ted')
arrayTrie.add('tender')
print('smurf: ', arrayTrie.contains('smurf'))
print('sm: ', arrayTrie.contains('sm'))
print('ted: ', arrayTrie.contains('ted'))
print('ten: ', arrayTrie.contains('ten'))



class HashTrieNode:
  def __init__(self, word=None):
    self.alphabet = {}
    self.isEndOfWord = False

    if word is not None:
      self.add(word)

  def add(self, word):
    if len(word) < 1: return

    self.isEndOfWord = self.isEndOfWord or len(word) < 2

    char = word[0]
    c = char.lower()
    w = word[1:]

    if self.alphabet.get(c):
      self.alphabet[c].add(w)
    else:
      self.alphabet[c] = HashTrieNode(w)

  def contains(self, word):
    if len(word) < 1:
      return self.isEndOfWord

    c = word[0]
    c.lower()
    w = word[1:]

    if self.alphabet.get(c) is None:
      return False
    else:
      return self.alphabet[c].contains(w)

  def getWordsWithPrefix(self, prefix):
    return self.getStringsWithPrefix(prefix, True)

  def getStringsWithPrefix(self, prefix, isWord=False):
    words = []
    for word in self.__getStrings(prefix, isWord):
      if '*' in word:
        word = word[:-1]

      if prefix in word:
        words.append(word)
    return words

  def __getStrings(self, prefix, isWord=False):
    strings = []
    items = []

    if not prefix:
      items = self.alphabet.items()
    else:
      char = prefix[0].lower()
      nextNode = self.alphabet.get(char)

      if nextNode:
        items = [[char, nextNode]]

    for char, node in items:
      for s in (['*' if self.isEndOfWord else ''] + node.__getStrings(prefix[1:] if prefix else '', isWord)):
        if not isWord or '*' in s:
          strings.append(char + s)

    return strings

strings = ["washington", "washing", "washingmachine", "university",
                    "washer", "web", "sanitation", "sanctuary", "water"]
atn = ArrayTrieNode()

for s in strings: atn.add(s)

withPrefixes = atn.getStringsWithPrefix('was')
print('withPrefixes: ', withPrefixes)

words = atn.getWordsWithPrefix('was')
print('words: ', words)

