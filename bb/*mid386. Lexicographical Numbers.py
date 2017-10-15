'''
Given an integer n, return 1 - n in lexicographical order.

For example, given 13, return: [1,10,11,12,13,2,3,4,5,6,7,8,9].

Please optimize your algorithm to use less time and space. The input size may be as large as 5,000,000.
'''
class Solution(object):
    def lexicalOrder(self, n):
        """
        :type n: int
        :rtype: List[int]
        """
        ans, i, curr = [], 0, 1
        while i < n:    # append n number
            ans.append(curr)
            curr *= 10
            while curr > n:     # cant be if because for example 13 -> 130 -> 14 cant be append
                curr = curr/10 + 1
                while curr % 10 == 0: # deal with case like 199+1=200 when we need to restart from 2 and 109+1=110, we should append 11
                    curr /= 10
            i += 1
        return ans
            
        
