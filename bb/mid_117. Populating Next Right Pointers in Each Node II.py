'''
Follow up for problem "Populating Next Right Pointers in Each Node".

What if the given tree could be any binary tree? Would your previous solution still work?

Note:

You may only use constant extra space.
For example,
Given the following binary tree,
         1
       /  \
      2    3
     / \    \
    4   5    7
After calling your function, the tree should look like:
         1 -> NULL
       /  \
      2 -> 3 -> NULL
     / \    \
    4-> 5 -> 7 -> NULL
'''
# Definition for binary tree with next pointer.
# class TreeLinkNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
#         self.next = None

# my O(N) space ez solution use bfs
class Solution:
    # @param root, a tree link node
    # @return nothing
    def connect(self, root):
        if root:
            level = [root]
            while level:
                tmp = []
                for i in range(len(level)):
                    if level[i].left:
                        tmp.append(level[i].left)
                    if level[i].right:
                        tmp.append(level[i].right)                        
                    if i < len(level) - 1:
                        level[i].next = level[i+1]
                    else:
                        level[i].next = None
                level = tmp
                        
# my O(1) space iterative solution:
class Solution:
    # @param root, a tree link node
    # @return nothing
    def connect(self, root):
        if root: 
            root.next = None      # no need point next of the end of each level to None because default is None
        while root:
            while (root) and (not root.left) and (not root.right):
                root = root.next
            if not root:
                break
            next1 = root.left if root.left else root.right
            curr = None    # can change with a TreeLinkNode(0)
            while root:
                if root.left and root.right:
                    if curr:
                        curr.next = root.left
                    curr = root.left.next = root.right
                    root = root.next
                elif root.left:
                    if curr:
                        curr.next = root.left
                    curr, root = root.left, root.next
                elif root.right:
                    if curr:
                        curr.next = root.right
                    curr, root = root.right, root.next
                else:
                    root = root.next
            curr.next, root = None, next1   # no need point next of the end of each level to None because default is None
            
# same idea, really concise solution:
class Solution:
    # @param root, a tree link node
    # @return nothing
    def connect(self, root):
        while root:
            cur = tmp = TreeLinkNode(0)
            while root:
                if root.left:
                    cur.next, cur = root.left, root.left
                if root.right:
                    cur.next, cur = root.right, root.right
                root = root.next
            root = tmp.next
            
