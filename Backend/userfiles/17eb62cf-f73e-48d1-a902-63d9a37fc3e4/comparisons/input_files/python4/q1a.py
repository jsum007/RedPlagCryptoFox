class Node(object):
    """
    Node contains two objects - a left and a right child, both may be a Node or both None,
    latter representing a leaf
    """
    def __init__(self, left=None, right=None):
        super(Node, self).__init__()
        self.left = left
        self.right = right

    def __str__(self):
        """
        Default inorder print
        """
        if self.left is None and self.right is None:
            return "(   )"
        else:
            return "( " + str(self.left) + " " + str(self.right) + " )"

    def __eq__(self, other):
        if self.left is None and self.right is None:
            return other.left is None and other.right is None
        elif other.left is None and other.right is None:
            return False
        else:
            return self.left == other.left and self.right == other.right

def Preorder(root):
    if root is None:
        return
    print(root.val, end =  " ")
    Preorder(root.left)
    Preorder(root.right)

def Convert_Tree(root):
    if (root is None) or ((root.left is None) and (root.right is None)):
        return
    Convert_Tree(root.left)
    Convert_Tree(root.right)
    root.val = root.left.val + root.right.val
    return root
    
def main(root):
    root = Node(50) 
    root.left = Node(7) 
    root.right = Node(2) 
    root.left.left = Node(3) 
    root.left.right = Node(5) 
    root.right.left = Node(1) 
    root.right.right = Node(30) 
    print('Preorder Traversal of arbitary binary tree:')
    Preorder(root)
    Convert_Tree(root)
    print('\nPreorder-Traversal after converting binary tree to a tree that holds children-sum-property:')
    Preorder(root)
    
if __name__ == "__main__":
    root = None
    main(root)