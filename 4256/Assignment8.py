#1
def postorder(node):
    if node is not None:
        postorder(node.left)
        postorder(node.right)
        print(node, " ")

#2
def height(root):
    if root is None:
        return 0
    return max(height(root.right),height(root.left)) + 1