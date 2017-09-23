#Given a positive integer n, find the least number of perfect square numbers (for example, 1, 4, 9, 16, ...) which sum to n.
#For example, given n = 12, return 3 because 12 = 4 + 4 + 4; given n = 13, return 2 because 13 = 4 + 9.

class Solution(object):
    def numSquares(self, n):
        """
        :type n: int
        :rtype: int
        """
        # use queue or list(bfs we used to do) works, but in this problem there will be a lot duplicate number in the tree structure
        # so using the set will save a lot memory( can use set because the order of one level doesn't matter in this problem
        queue = {(n, 1)}    # saved the level with number using tuple
        while queue:
            tmp = set()
            for curr in queue:
                ns = math.sqrt(curr[0])
                if ns == int(ns):
                    return curr[1]            
                for i in range(int(ns), 0, -1):
                    tmp.add((curr[0] - i*i, curr[1] + 1))    
            queue = tmp
                           
                           
        # queue = collections.deque([(n, 1)])
        # while queue:
        #     curr = queue.popleft()
        #     ns = math.sqrt(curr[0])
        #     if ns == int(ns):
        #         return curr[1]            
        #     for i in range(int(ns), 0, -1):
        #         queue.append((curr[0] - i*i, curr[1] + 1))    
