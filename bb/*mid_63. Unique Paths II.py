'''
Follow up for "Unique Paths":

Now consider if some obstacles are added to the grids. How many unique paths would there be?

An obstacle and empty space is marked as 1 and 0 respectively in the grid.

For example,
There is one obstacle in the middle of a 3x3 grid as illustrated below.

[
  [0,0,0],
  [0,1,0],
  [0,0,0]
]
The total number of unique paths is 2.

Note: m and n will be at most 100.
'''
# dp solution using O(m*n) space
class Solution(object):
    def uniquePathsWithObstacles(self, obstacleGrid):
        """
        :type obstacleGrid: List[List[int]]
        :rtype: int
        """
        m, n = len(obstacleGrid), len(obstacleGrid[0])
        res = [[0 for i in range(n+1)] for j in range(m+1)]
        res[0][1] = 1
        
        for i in range(1, m+1):
            for j in range(1, n+1):
                if not obstacleGrid[i-1][j-1]:
                    res[i][j] = res[i-1][j] + res[i][j-1]
        return res[m][n]
                    
#in place solution：
class Solution(object):
    def uniquePathsWithObstacles(self, obstacleGrid):
        """
        :type obstacleGrid: List[List[int]]
        :rtype: int
        """
        m, n = len(obstacleGrid), len(obstacleGrid[0])
        obstacleGrid[0][0] = 1 - obstacleGrid[0][0]
        
        for i in range(1, m):
            obstacleGrid[i][0] = obstacleGrid[i-1][0] if obstacleGrid[i][0] == 0 else 0
        
        for j in range(1, n):
            obstacleGrid[0][j] = obstacleGrid[0][j-1] if obstacleGrid[0][j] == 0 else 0        
            
        for i in range(1, m):
            for j in range(1, n):
                obstacleGrid[i][j] = obstacleGrid[i-1][j] + obstacleGrid[i][j-1] if obstacleGrid[i][j] == 0 else 0
        return obstacleGrid[-1][-1]
            
