 '''
 
Given a binary tree, check whether it is a mirror of itself (ie, symmetric around its center).

For example, this binary tree [1,2,2,3,4,4,3] is symmetric:

    1
   / \
  2   2
 / \ / \
3  4 4  3
But the following [1,2,2,null,3,null,3] is not:
    1
   / \
  2   2
   \   \
   3    3
Note:
Bonus points if you could solve it both recursively and iteratively.
'''

##########recursively
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        return self.is_Sym(root, root)
    def is_Sym(self, root1, root2):
        if not root1 and not root2:
            return True
        if root1 and root2 and root1.val == root2.val:
            return self.is_Sym(root1.left, root2.right) and self.is_Sym(root1.right, root2.left)
        return False
        
#Great idea to use a stack to keep track of the nodes, but insert and pop(0) is probably not a good idea for stack. Here is the fix for it:

  def isSymmetric(self, root):
      if root is None:
          return True
      stack = [(root.left, root.right)]
      while stack:
          left, right = stack.pop()
          if left is None and right is None:
              continue
          if left is None or right is None:
              return False
          if left.val == right.val:
              stack.append((left.left, right.right))
              stack.append((left.right, right.left))
          else:
              return False
      return True

#Also below is my solution with level order traversal:

def isSymmetric(self, root):
    last = [root]
    while True:
        if not any(last):
            return True
        current = []
        for node in last:
            if node is not None:
                current.append(node.left)
                current.append(node.right)
        if not self.is_list_symmetric(current):
            return False
        else:
            last = current
    
def is_list_symmetric(self, lst):
    head, tail = 0, len(lst) - 1
    while head < tail:
        h, t = lst[head], lst[tail]
        head += 1
        tail -= 1
        if h == t == None:
            continue
        if None in (h, t) or h.val != t.val:
            return False
    return True

        
