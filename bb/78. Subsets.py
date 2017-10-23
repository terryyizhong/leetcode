'''
Given a set of distinct integers, nums, return all possible subsets (the power set).

Note: The solution set must not contain duplicate subsets.

For example,
If nums = [1,2,3], a solution is:

[
  [3],
  [1],
  [2],
  [1,2,3],
  [1,3],
  [2,3],
  [1,2],
  []
]
'''
class Solution(object):
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        ans = []
        level = [nums]
        while level:
            for i in level:
                ans.append(i)
            tmp = []
            for s in level:
                for i in range(len(s)):
                    del_1 = s[:i] + s[i+1:]
                    if del_1 not in tmp:
                        tmp.append(del_1)
            level = tmp
        return ans
#back tracking!
class Solution(object):
    def subsets(self, nums):
        ans = []
        self.dfs(sorted(nums), 0, [], ans)
        return ans
    
    def dfs(self, nums, start, tmp, ans):
        ans.append(copy.deepcopy(tmp))    #must use deep copy otherwise will only append reference of tmp in ans
        for i in range(start, len(nums)):
            tmp.append(nums[i])
            self.dfs(nums, i+1, tmp, ans)
            tmp.pop()
    def dfs(self, nums, start, path, ans):
    ans.append(path)
    for i in range(start, len(nums)):
        self.dfs(nums, i+1, path+[nums[i]], ans)  #pass new list not reference each time

#iterative
def subsets(self, nums):
    res = [[]]
    for num in sorted(nums):
        res += [item+[num] for item in res]
    return res
