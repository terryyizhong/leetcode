# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def kthSmallest(self, root, k):
        """
        :type root: TreeNode
        :type k: int
        :rtype: int
        """
        stack = []
        while stack or root:  
            while root:
                stack.append(root)
                root = root.left
            curr = stack.pop()
            if k == 1:
                return curr.val
            k -= 1
            root = curr.right

# brilliant solution use yield of python!

class Solution(object):
    def kthSmallest(self, root, k):
        """
        :type root: TreeNode
        :type k: int
        :rtype: int
        """
        def inorder(root):
            if root:
                for val in inorder(root.left):
                    yield val
                yield root.val
                for val in inorder(root.right):
                    yield val
                    
        for val in inorder(root):
            if k == 1:
                return val
            k -= 1
