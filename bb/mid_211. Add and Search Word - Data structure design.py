'''
Design a data structure that supports the following two operations:

void addWord(word)
bool search(word)
search(word) can search a literal word or a regular expression string containing only letters a-z or .. A . means it can represent any one letter.

For example:

addWord("bad")
addWord("dad")
addWord("mad")
search("pad") -> false
search("bad") -> true
search(".ad") -> true
search("b..") -> true
'''
# based on trie 
class TrieNode(object):
    def __init__(self):
        self.child = {}
        self.is_word = False
        
class WordDictionary(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.root = TrieNode()
    
    
    def addWord(self, word):
        """
        Adds a word into the data structure.
        :type word: str
        :rtype: void
        """
        curr = self.root

        for l in word:
            if l not in curr.child:
                curr.child[l] = TrieNode()
            curr = curr.child[l]
        curr.is_word = True
                

    def search(self, word):
        """
        Returns if the word is in the data structure. A word could contain the dot character '.' to represent any one letter.
        :type word: str
        :rtype: bool
        """
        root = self.root
        if not word:    # if insert '', then '' should be True
            if root.is_word: return True
        self.ans = False    # must use this, cannot just return True false, because at last line 
        self.dfs(word, root)
        return self.ans
        
                
    def dfs(self, word, node):                
        if not word:
            if node.is_word:
                self.ans = True # any path reach here result will be True
            return
        if word[0] == '.':
            for l in node.child:
                self.dfs(word[1:], node.child[l])
        else:
            if word[0] in node.child:
                self.dfs(word[1:], node.child[word[0]])
            else:
                return    # cannot return False, cause we have several path, only one wrong path cannot return True
        

# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)
