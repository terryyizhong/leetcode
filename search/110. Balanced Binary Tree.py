'''
Given a binary tree, determine if it is height-balanced.

For this problem, a height-balanced binary tree is defined as a binary tree in which the depth of the two
subtrees of every node never differ by more than 1.
'''
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def isBalanced(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        def check(root):
            if not root:
                return 0
            l = check(root.left)
            r = check(root.right)
            if abs(l-r) > 1 or l == -1 or r == -1:
                return -1
            else:
                return max(l, r) + 1
        return check(root) != -1

#dfs version
class Solution(object):
    def isBalanced(self, root):
        stack, node, last, depths = [], root, None, {}
        while stack or node:
            if node:
                stack.append(node)
                node = node.left
            else:
                node = stack[-1]
                if not node.right or last == node.right:
                    node = stack.pop()
                    left, right  = depths.get(node.left, 0), depths.get(node.right, 0)
                    if abs(left - right) > 1: return False
                    depths[node] = 1 + max(left, right)
                    last = node
                    node = None
                else:
                    node = node.right
        return True
