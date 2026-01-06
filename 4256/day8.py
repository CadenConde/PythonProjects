class Node:
    def __init__(self, value, left_child = None, right_child = None):
        self.val = value
        self.left = left_child
        self.right = right_child
        
    def __str__(self):
        return str(self.val)
    
    #1
    def num_nodes(root):
        res = 1
        if root is None:
            return 0
        if root.left:
            res += root.left.num_nodes()
        if root.right:
            res += root.right.num_nodes()
        return res
    
    #2
    def num_leaves(root):
        res = 0
        if root.left is None and root.right is None:
            return 1
        if root.left:
            res += root.left.num_leaves()
        if root.right:
            res += root.right.num_leaves()
        return res
    
    #3
    def is_full(root):
        if root.left is None and root.right is None:
            return True
        if root.left is not None and root.right is not None:
            return root.left.is_full() and root.right.is_full()
        return False
    
    #5
    #from hw
    def height(root):
        res = 0
        if root is None:
            return 0
        if root.right:
            res = root.right.height()
        if root.left:
            res = max(res, root.left.height())
        return res + 1
    def is_perfect(root):
        if root.num_nodes() == (2**root.height()) - 1:
            return True
        return False
    
    #6
    def has_value_bst(root, val):
        if root.val == val:
            return True
        if root.val > val and root.left:
            return root.left.has_value_bst(val)
        elif root.right:
            return root.right.has_value_bst(val)
        return False
    
    #7
    def add_value_bst(bst, val):
        if bst.val > val:
            if bst.left is None:
                bst.left = Node(val, None, None)
            else:
                bst.left.add_value_bst(val)
        else:
            if bst.right is None:
                bst.right = Node(val, None, None)
            else:
                bst.right.add_value_bst(val)
        
def add(heap, val):
    heap.append(val)
    i = len(heap) - 1
    i2 = (i-1) // 2
    while i >= 0 and i2 >= 0 and heap[i] < heap[i2]:
        temp = heap[i2]
        heap[i2] = heap[i]
        heap[i] = temp
        i = i2
        i2 = (i-1) // 2
        
l = [1,2,4,5,6,7]
add(l, 0)
add(l, 8)
add(l, -1)
add(l, 4)
print(l)

    
    