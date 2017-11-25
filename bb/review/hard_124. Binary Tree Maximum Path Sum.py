'''
Given a binary tree, find the maximum path sum.

For this problem, a path is defined as any sequence of nodes from some starting node to any node in the tree along the parent-child connections. The path must contain at least one node and does not need to go through the root.

For example:
Given the below binary tree,

       1
      / \
     2   3
Return 6.

'''

#

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def maxPathSum(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root: return None
        self.Max = float('-inf')
        self.dfs(root)
        return self.Max
    def dfs(self, node):
        l = r = 0
        if node.left:
            l = max(0, self.dfs(node.left))
        if node.right:
            r = max(0, self.dfs(node.right))
        self.Max = max(self.Max, node.val + l + r)  # for each node, cal the max possible if in the path (only need cal 2                                                           side here cause one side already cal by parent.
        return node.val + max(l, r) # one side max possible path
