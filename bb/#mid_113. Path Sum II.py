'''
Given a binary tree and a sum, find all root-to-leaf paths where each path's sum equals the given sum.

For example:
Given the below binary tree and sum = 22,
              5
             / \
            4   8
           /   / \
          11  13  4
         /  \    / \
        7    2  5   1
return
[
   [5,4,11,2],
   [5,8,4,5]
]
'''
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def pathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: List[List[int]]
        """
        
        return [_ for _ in self.path_sum(root, sum, [])] if root else []
            
    
    def path_sum(self, root, sum, path): 
        if sum == root.val and (not root.left) and (not root.right):
            yield path + [root.val]
        if root.left:
            for i in self.path_sum(root.left, sum - root.val, path + [root.val]):
                yield i
        if root.right:
            for i in self.path_sum(root.right, sum - root.val, path + [root.val]):
                yield i
