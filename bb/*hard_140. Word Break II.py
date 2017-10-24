'''

Given a non-empty string s and a dictionary wordDict containing a list of non-empty words, add spaces in s to construct a sentence where each word is a valid dictionary word. You may assume the dictionary does not contain duplicate words.

Return all such possible sentences.

For example, given
s = "catsanddog",
dict = ["cat", "cats", "and", "sand", "dog"].

A solution is ["cats and dog", "cat sand dog"].

'''
class Solution(object):
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: List[str]
        """
        tails = {len(s): ['']}

        def combine(i):
            if i not in tails:
                tmp = []
                for word in wordDict:    
                    j = i + len(word)
                    if s[i:j] == word:  
                        for tail in combine(j):
                            tmp.append(s[i:j] + (tail and ' ' + tail))    
                tails[i] = tmp
            return tails[i]
        return combine(0)
        
# different in search, use dict and scan only the length if wordDict
class Solution(object):
    def wordBreak(self, s, wordDict):
        memo = {len(s): ['']}
        wordDict=set(wordDict)
        len_w=set(len(w) for w in wordDict)
        def sentences(i):
            if i not in memo:
                memo[i] = [s[i:i+j] + (tail and ' ' + tail)
                           for j in len_w
                           if s[i:i+j] in wordDict
                           for tail in sentences(i+j)]
            return memo[i]
        return sentences(0)
