'''
Given an input string, reverse the string word by word.

For example,
Given s = "the sky is blue",
return "blue is sky the".

Update (2015-02-12):
For C programmers: Try to solve it in-place in O(1) space.

click to show clarification.

Clarification:
What constitutes a word?
A sequence of non-space characters constitutes a word.
Could the input string contain leading or trailing spaces?
Yes. However, your reversed string should not contain leading or trailing spaces.
How about multiple spaces between two words?
Reduce them to a single space in the reversed string.
'''
#my slow solution:
class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        dic = " "
        words = ""
        i = 0
        while i < len(s):
            tmp = ""
            while i < len(s) and s[i] not in dic:
                tmp += s[i]
                i += 1
            if tmp: words = tmp + " " + words
            i+= 1
        return words.rstrip()
        
# actually just need one line:
        #return " ".join(s.split()[::-1])
        
        
        
