'''
Given a m x n matrix, if an element is 0, set its entire row and column to 0. Do it in place.

click to show follow up.

Follow up:
Did you use extra space?
A straight forward solution using O(mn) space is probably a bad idea.
A simple improvement uses O(m + n) space, but still not the best solution.
Could you devise a constant space solution?
'''
# simple O(m+n) solution
class Solution(object):
    def setZeroes(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: void Do not return anything, modify matrix in-place instead.
        """
        
        row_index, col_index = set(), set()
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j] == 0:
                    row_index.add(i)
                    col_index.add(j)
        for i in row_index:
            matrix[i] = [0] * len(matrix[0])
        for j in col_index:
            for i in range(len(matrix)):
                matrix[i][j] = 0
                
# beat %99.9 O(1) solution, use first col&row to save 0, if col or row has zero in the matrix                
class Solution(object):
    def setZeroes(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: void Do not return anything, modify matrix in-place instead.
        """
        if not matrix: return
        m, n = len(matrix), len(matrix[0])
        
        row1_0 = False
        for _ in matrix[0]:
            if _ == 0:
                row1_0 = True
        col1_0 = False                
        for i in range(m):
            if matrix[i][0] == 0:
                col1_0 = True                
        
        for i in range(1, m):
            for j in range(1, n):
                if matrix[i][j] == 0:
                    matrix[i][0] = matrix[0][j] = 0
        
        for i in range(1, m):
            if matrix[i][0] == 0:
                for j in range(1, n):
                    matrix[i][j] = 0
        for j in range(1, n):
            if matrix[0][j] == 0:
                for i in range(1, m):
                    matrix[i][j] = 0
        
        if row1_0: 
            matrix[0] = [0] * n
        if col1_0:
            for i in range(m):
                matrix[i][0] = 0
