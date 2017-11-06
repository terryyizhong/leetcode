'''
Serialization is the process of converting a data structure or object into a sequence of bits so that it can be stored in a file or memory buffer, or transmitted across a network connection link to be reconstructed later in the same or another computer environment.

Design an algorithm to serialize and deserialize a binary tree. There is no restriction on how your serialization/deserialization algorithm should work. You just need to ensure that a binary tree can be serialized to a string and this string can be deserialized to the original tree structure.

For example, you may serialize the following tree

    1
   / \
  2   3
     / \
    4   5
as "[1,2,3,null,null,4,5]", just the same as how LeetCode OJ serializes a binary tree. You do not necessarily need to follow this format, so please be creative and come up with different approaches yourself.
Note: Do not use class member/global/static variables to store states. Your serialize and deserialize algorithms should be stateless.


'''
# my solution based on leetcode idea

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        if not root: return ''
        bfs = [root]
        level = []
        while bfs:
            for i in bfs:
                    level.append(i.val) if i else level.append(None)
            tmp = []
            for node in bfs:
                if node:
                    tmp.append(node.left)
                    tmp.append(node.right)
            bfs = tmp
        last = len(level) - 1
        while level[last] is None:      # must aware of the case 0 together with None, can't use while not level[last]
            last -= 1
        return str(level[:last+1])
        

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        if not data: return None
        data = data[1:-1].split(', ')
        for i in range(len(data)):
            data[i] = None if data[i] == 'None' else int(data[i])   #you can int('0') can not int('None')
            
        root = TreeNode(data[0])
        i, l = 1, len(data)
        level = [root]
        while level and i < l:
            tmp = []
            for node in level:
                if data[i] is not None:     # also should use ' is not None '  cant not only use 'if data[i]' beacause 0 not pass
                    node.left = TreeNode(data[i])  
                    tmp.append(node.left)
                i += 1                      # need add 1 no matter data[i] is None or not
                if i >= l: break
                if data[i] is not None:
                    node.right = TreeNode(data[i])
                    tmp.append(node.right)    
                i += 1
                if i >= l: break
            level = tmp
        return root
        
# stephen's brilliant solution:
    def serialize(self, root):
        def doit(node):
            if node:
                vals.append(str(node.val))
                doit(node.left)
                doit(node.right)
            else:
                vals.append('#')
        vals = []
        doit(root)
        return ' '.join(vals)

    def deserialize(self, data):
        def doit():
            val = next(vals)
            if val == '#':
                return None
            node = TreeNode(int(val))
            node.left = doit()
            node.right = doit()
            return node
        vals = iter(data.split())
        return doit()
