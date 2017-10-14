'''
A robot is located at the top-left corner of a m x n grid (marked 'Start' in the diagram below).

The robot can only move either down or right at any point in time. The robot is trying to reach the bottom-right corner of the grid (marked 'Finish' in the diagram below).

How many possible unique paths are there?


Above is a 3 x 7 grid. How many possible unique paths are there?

Note: m and n will be at most 100.
'''

#DP solution from https://discuss.leetcode.com/topic/15265/0ms-5-lines-dp-solution-in-c-with-explanations
class Solution(object):
    def uniquePaths(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        if m >= n: m, n = n, m
        curr = [1] * m
        for _ in range(1, n):
            for i in range(1, m):
                curr[i] += curr[i-1]
        return curr[-1]
# math       
class Solution(object):
    def uniquePaths(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        # just m-1 or n-1 Combination of (m+n-2)
        if m >= n: m, n = n, m
        ans = 1
        for i in range(1, m):
            ans = ans * (m + n - 1 - i) / i
        return ans
        
               
        
