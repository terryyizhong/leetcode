def dfs(root):
    pre = []
    stack = [root]
    while stack:
        curr = stack.pop()
        pre.append(curr.value)
        stack.append(curr.right)
        stack.append(curr.left)
    return pre


def pre_order(root):
    result = []
    dfs2(root, result)
    return result


def dfs2(root, pre):
    if root:
        pre.append(root.val)
        dfs2(root.left, pre)
        dfs2(root.right, pre)
