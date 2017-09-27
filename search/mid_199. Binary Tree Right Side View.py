'''

Given a binary tree, imagine yourself standing on the right side of it, return the values of the nodes you can see ordered from top to bottom.

For example:
Given the following binary tree,
   1            <---
 /   \
2     3         <---
 \     \
  5     4       <---
You should return [1, 3, 4].
'''
class Solution(object):
    def rightSideView(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if not root:
            return []
        ans = []
        deque = collections.deque([root])
        while deque:
            tmp = collections.deque([])
            for i in range(len(deque)):
                curr = deque.popleft()
                if len(deque) == 0:
                    ans.append(curr.val)
                if curr.left:                 #can not append None to the queue
                    tmp.append(curr.left)
                if curr.right:    
                    tmp.append(curr.right)
            deque = tmp
        return ans
   
# shorter way
class Solution(object):
    def rightSideView(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
    
        ans = []
        if root:
            deque = collections.deque([root])
            while deque:
                ans.append(deque[-1].val)
                tmp = collections.deque([])
                for node in deque:
                    for kid in (node.left, node.right):
                        if kid:
                            tmp.append(kid)
                deque = tmp
        return ans
        
