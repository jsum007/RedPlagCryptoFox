class Node(object):
    """
    Node contains two objects - a left and a rchild child, both may be a Node or both None,
    latter representing a leaf
    """
    def __init__(self, left=None, rchild=None):
        super(Node, self).__init__()
        self.left = left
        self.rchild = rchild

    def __str__(self):
        """
        Default inorder print
        """
        if self.left is None and self.rchild is None:
            return "(   )"
        else:
            return "( " + str(self.left) + " " + str(self.rchild) + " )"

    def __eq__(self, other):
        if self.left is None and self.rchild is None:
            return other.left is None and other.rchild is None
        elif other.left is None and other.rchild is None:
            return False
        else:
            return self.left == other.left and self.rchild == other.rchild

def preeee(head):
    if head is None:
        return
    print(head.val, end =  " ")
    preeee(head.left)
    preeee(head.rchild)

    '''
ef mirrorTree(node):
    """
    Returns the mirror image of the tree rooted at node
    """
    revhead = node
    queue = []
    queue.append(revhead)
    while len(queue)>0 :
        now = queue[0]
        temp = now.right
        now.right = now.left
        now.left = temp
        if now.left is not None:
            queue.append(now.left)
        if now.right is not None:
            queue.append(now.right)
        queue.pop(0)
    return revhead

    '''

def changee(head):
    if (head is None) or ((head.left is None) and (head.rchild is None)):
        return
    changee(head.left)
    changee(head.rchild)
    head.val = head.left.val + head.rchild.val
    return head
    
def main(head):
    head = Node(50) 
    head.left =                      Node(7) 
    




    head.rchild =                                            Node(2) 
    head.left.                                                                                                      lattereft = Node(3) 
    head.left.rchild = Node(5) 



    head.rchild.                                                                left = Node(1) 
    head.rchild.rchild = Node(30) 
    print('preeee Traversal of arbitary binary tree:')
    preeee(head)
    changee(head)
    print('\npreeee-Tdfhcudauhcfudagwugdvfugfuhfdcuajshncajhfoiyefuhqedcjlnassjcjhufcgyigyg:')
    preeee(head)
    
if __name__ == "__main__":
    head = None
    main(head)