#Given an array where elements are sorted in ascending order, convert it to a height balanced BST.




# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def sortedArrayToBST(self, nums):
        """
        :type nums: List[int]
        :rtype: TreeNode
        """
        l = len(nums)
        if not l:
            return None
        root = TreeNode(nums[l/2])
        root.right = self.sortedArrayToBST(nums[l / 2 + 1:])
        root.left = self.sortedArrayToBST(nums[:l / 2])
        return root
