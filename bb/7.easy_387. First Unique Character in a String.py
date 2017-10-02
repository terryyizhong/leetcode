'''

Given a string, find the first non-repeating character in it and return it's index. If it doesn't exist, return -1.

Examples:

s = "leetcode"
return 0.

s = "loveleetcode",
return 2.
Note: You may assume the string contain only lowercase letters.
'''
class Solution(object):
    def firstUniqChar(self, s):
        """
        :type s: str
        :rtype: int
        """
        c = {}
        for i in s:
            count = c.get(i, 0) + 1
            c[i] = count
#        collections.Counter(s)
        for idx, i in enumerate(s):
            if c[i] == 1:
                return idx
        return -1
        
# 3-line
def firstUniqChar(self, s):
    """
    :type s: str
    :rtype: int
    """

    letters='abcdefghijklmnopqrstuvwxyz'
    index=[s.index(l) for l in letters if s.count(l) == 1]
    return min(index) if len(index) > 0 else -1
