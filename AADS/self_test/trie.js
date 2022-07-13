class TrieNode {
  constructor(word=null) {
    this.alphabet  = new Array(TrieNode.alphabetSize)
    this.endOfWord = false

    if (word !== null) {
      this.add(word)
    }
  }

  add(word) {
    if (word.length < 1) {
      this.endOfWord = true
      return
    }

    const i = word.charCodeAt(0) - TrieNode.aIndex
    const w = word.slice(1)

    if (this.alphabet[i])
      this.alphabet[i].add(w)
    else
      this.alphabet[i] = new TrieNode(w)
  }

  contains(word) {
    if (word.length < 1) return this.endOfWord

    const i = word.charCodeAt(0) - TrieNode.aIndex

    if (this.alphabet[i])
      return this.alphabet[i].contains(word.slice(1))
    else
      return false
  }

  getWordsWithPrefix(prefix) {
    return this.getStringsWithPrefix(prefix, true)
  }

  getStringsWithPrefix(prefix, lookingForWord=false) {
    return this.#privateGetStringsWithPrefix(prefix, lookingForWord)
  }

  #privateGetStringsWithPrefix(prefix, lookingForWord=false, strings = [], foundPrefix='') {
    // Found prefix
    if (prefix.length < 1) {
      // Add each character in this node to the found prefix
      this.alphabet.forEach((node, i) => {
        if (node) {
          const char = String.fromCharCode(i + TrieNode.aIndex)
          const newFoundPrefix = foundPrefix + char
          const nextNode = this.alphabet[i]

          if ((lookingForWord && nextNode.endOfWord) || !lookingForWord) strings.push(newFoundPrefix)

          nextNode.#privateGetStringsWithPrefix('', lookingForWord, strings, newFoundPrefix)
        }
      })

      return strings
    }

    const i = prefix.charCodeAt(0) - TrieNode.aIndex
    if (this.alphabet[i]) {
      // Traversing through Trie to get through prefix
      foundPrefix += prefix[0]
      return this.alphabet[i].#privateGetStringsWithPrefix(prefix.slice(1), lookingForWord, strings, foundPrefix)
    } else {
      // Trie does not contain prefix
      return []
    }
  }
}

TrieNode.alphabetSize = 26
TrieNode.aIndex = 'a'.charCodeAt(0)

const trie = new TrieNode('word')
trie.add('worker')
trie.add('worm')
trie.add('work')
trie.add('wordle')
trie.add('wombat')
trie.add('wookie')

console.log('contains word: ', trie.contains('word'))
console.log('contains work: ', trie.contains('work'))
console.log('contains worker: ', trie.contains('worker'))
console.log('strings with prefix "wor": ', trie.getStringsWithPrefix('wor'))
console.log('words with prefix "wor": ', trie.getWordsWithPrefix('wor'))
