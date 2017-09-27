#Given a binary tree, find its minimum depth.

#The minimum depth is the number of nodes along the shortest path from the root node down to the nearest leaf node.

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def minDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        depth = 0
        if root:
            level = [root]
            while level:
                depth += 1  # if root, already 1
                tmp = []
                for node in level:
                    if not node.left and not node.right:  # leaf condition
                        return depth
                    for kid in (node.left, node.right):
                        if kid:
                            tmp.append(kid)
                level = tmp
        return depth

#3-line recursively
def minDepth(self, root):
    if not root: return 0
    d = map(self.minDepth, (root.left, root.right))
    return 1 + (min(d) or max(d))
    
# remove redundant testing by introducing a helper func
def minDepth(self, root):
    return 0 if not root else self.dfs(root)
def dfs(self, root):
    return 1 + min([self.dfs(x) for x in (root.left,root.right) if x] or [0])

# original version
def minDepth1(self, root):
    if not root: return 0
    return 1 + min([self.minDepth(x) for x in (root.left,root.right) if x] or [0])  
