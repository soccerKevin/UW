from __future__ import annotations
from typing import List, Union


class Trie:
    kAlphabetSize = 26

    class TrieNode:
        def __init__(self):
            self.nodeCollection = [None for _ in range(Trie.kAlphabetSize)]
            self.isWordEnd = False

        def IsWordEnd(self):
            return self.isWordEnd

        def SetWordEnd(self):
            self.isWordEnd = True

    def __init__(self, keys):
        self.root = Trie.TrieNode()
        for key in keys:
            self.Add(key)

    @staticmethod
    def Output(strings: List[str], initialMsg: str = "", endMsg: str = "", separator: str = " "):
        if initialMsg:
            print(initialMsg)
        for string in strings:
            print(string, end=separator)
        if endMsg:
            print(endMsg)

    @staticmethod
    def Run():
        Trie.DoTest1()

    @staticmethod
    def DoTest1():
        # Generate some strings
        strings = ["washington", "washing", "washingmachine", "university",
                    "washer", "web", "sanitation", "sanctuary", "water"]
        Trie.Output(strings, "", "\n")

        t = Trie(strings)

        # Test prefixes
        Trie.TestPrefix(t, "")
        Trie.TestPrefix(t, "w")
        Trie.TestPrefix(t, "wash")
        Trie.TestPrefix(t, "washing")
        Trie.TestPrefix(t, "washington")

    @staticmethod
    def TestPrefix(t: Trie, prefix: str):
        words = t.GetWordsWithPrefix(prefix)
        Trie.Output(words, f"Words with prefix {prefix} ({len(words)})", "\n")

        prefixes = t.GetStringsWithPrefix(prefix)
        Trie.Output(prefixes, f"Strings with prefix {prefix} ({len(prefixes)})", "\n")
        print("-------------------------------------------------------------------\n")

    def Add(self, string: str):
        currentNode = self.root

        for ii in range(len(string)):
            if currentNode is None:
                break

            currCharIndex = ord(string[ii].lower()) - ord('a')

            if currentNode.nodeCollection[currCharIndex] is None:
                # if None, it means this char path is new, so, create a new node ( note that we don’t store the character )
                currentNode.nodeCollection[currCharIndex] = Trie.TrieNode()
            currentNode = currentNode.nodeCollection[currCharIndex]
        currentNode.SetWordEnd()

    def __GetNode(self, string: str):
        strIndexFound = -1
        currentNode = self.root

        for ii in range(len(string)):
            if currentNode is None:
                break

            currentNode = currentNode.nodeCollection[ord(string[ii].lower()) - ord('a')]
            if currentNode is not None:
                strIndexFound = ii
        # currentNode is either None or points to the node we have.
        return currentNode, strIndexFound

    def Contains(self, string: str):
        node, ignoreStrIndexFound = self.__GetNode(string)
        return False if node is None else node.IsWordEnd()
        # ///// Above return is same as below  /////////////
        #  if node is not None:
        #      return node.IsWordEnd()
        #  else:
        #      return False

    def GetWordsWithPrefix(self, string: str):
        # pass in true for isWord, since we want only words, not just any string
        return self.__GetStringsWithPrefix(string, True)

    def GetStringsWithPrefix(self, string: str):
        # pass in false for isWord, since we dont care if the string is a word or not
        return self.__GetStringsWithPrefix(string, False)

    def __GetStringsWithPrefix(self, string: str, isWord: bool):
        keys = []
        node, strIndexFound = self.__GetNode(string)

        if node is not None:
            if not isWord or node.IsWordEnd():
                keys.append(string[:strIndexFound+1])  # add the string we found so far
            prefix = string
            self.__GetAllStringsStartingAtNode(node, keys, prefix, isWord)
        return keys

    def __GetAllStringsStartingAtNode(self, node: TrieNode, keys: List[str], prefix: str, isWord: bool):
        myNodes = node.nodeCollection

        for index in range(len(myNodes)):
            if myNodes[index] is not None:
                newPrefix = prefix + (chr(ord('a') + index))  # prefix + char represented by myNodes[index]

                # if we want any prefix OR only words
                if (not isWord) or myNodes[index].IsWordEnd():
                    keys.append(newPrefix)
                self.__GetAllStringsStartingAtNode(myNodes[index], keys, newPrefix, isWord)

