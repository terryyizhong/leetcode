'''
Given a column title as appear in an Excel sheet, return its corresponding column number.

For example:

    A -> 1
    B -> 2
    C -> 3
    ...
    Z -> 26
    AA -> 27
    AB -> 28 
'''
#my normal sol
class Solution(object):
    def titleToNumber(self, s):
        """
        :type s: str
        :rtype: int
        """
        ans = 0
        for i, n in enumerate(s[::-1]):
            ans += (ord(n) - 64) * pow(26, i) ## 64 == ord('A')
        return ans
        
########bravo one-line map-reduce sol
def titleToNumber(self, s):
    return reduce(lambda x,y:x*26+y,map(lambda x:ord(x)-ord('A')+1,s))
