'''

Given a string s, partition s such that every substring of the partition is a palindrome.

Return all possible palindrome partitioning of s.

For example, given s = "aab",
Return

[
  ["aa","b"],
  ["a","a","b"]
]

'''
# should familiar with backtracking more
class Solution(object):
    def partition(self, s):
        """
        :type s: str
        :rtype: List[List[str]]
        """
        def is_palindrome(st):
            i, j = 0, len(st) - 1
            while i <= j:
                if st[i] != st[j]:
                    return False
                i += 1
                j -= 1
            return True
        # back tracking part, pass with ans, and path
        def dfs(st, ans, path):
            if not st:
                ans.append(path)    # append path to ans at the end of search!
                return
            for i in range(1, len(st) + 1):   # whole str can also be a valid path
                if is_palindrome(st[:i]):
                    dfs(st[i:], ans, path + [st[:i]])
            
        ans = []
        dfs(s, ans, [])
        return ans
            
            
            
            
            
