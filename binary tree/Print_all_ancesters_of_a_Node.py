class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
    
    
    
def dfs(root, path, target):
    print root.val
    if root.val == target:
        return True
    if root.left and dfs(root.left, path, target):
        path.append(root.val)
        return True
    if root.right and dfs(root.right, path , target):
        path.append(root.val)
        return True

    
def output_ancester(root, target):

            
    if not root: return None
    ans = []
    dfs(root, ans, target)
    return ans
    

def ancester(root, target):
    if not root: return None
    stack = [(root, [])]
    while stack:
        curr = stack.pop()
        node, path = curr[0], curr[1]
        if node.val == target:
            return path
        if node.left:
            stack.append((node.left, path + [node.val]))
        if node.right:
            stack.append((node.right, path + [node.val]))            
    return None

root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)
root.right.right = TreeNode(6)

print ancester(root, 4)
