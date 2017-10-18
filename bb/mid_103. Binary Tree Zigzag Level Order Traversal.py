'''

Given a binary tree, return the zigzag level order traversal of its nodes' values. (ie, from left to right, then right to left for the next level and alternate between).

For example:
Given binary tree [3,9,20,null,null,15,7],
    3
   / \
  9  20
    /  \
   15   7
return its zigzag level order traversal as:
[
  [3],
  [20,9],
  [15,7]
]
'''

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def zigzagLevelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if not root: return []
        ans = []
        l, level = 1, [root]
        while level:
            if l % 2:
                ans.append([node.val for node in level])            
            else:
                ans.append([node.val for node in level[::-1]])            
            tmp = []                
            for node in level:
                if node.left: tmp.append(node.left)
                if node.right: tmp.append(node.right)
            level, l = tmp, l + 1
        return ans

# modified faster
class Solution(object):
    def zigzagLevelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if not root: return []
        ans = []
        l, level = 1, [root]
        while level:          
            tmp, tmp_ans = [], []              
            for node in level:
                tmp_ans.append(node.val)
                if node.left: tmp.append(node.left)
                if node.right: tmp.append(node.right)
            if l % 2:
                ans.append(tmp_ans)
            else:
                ans.append(tmp_ans[::-1])
            level, l = tmp, l + 1
        return ans
                    
                                    
                    
                    
                    
                        
            
        
                    
                                    
                    
                    
                    
                        
            
        
