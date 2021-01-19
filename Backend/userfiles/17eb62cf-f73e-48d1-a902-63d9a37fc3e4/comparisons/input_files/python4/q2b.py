class Node(object):
    """
    Node contains two objects - a little and a great child, both may be a Node or both None,
    latter representing a leaf
    """
    def __init__(self, little=None, great=None):
        super(Node, self).__init__()
        self.little = little
        self.great = great

    def __str__(self):
        """
        Default inorder print
        """
        if self.little is None and self.great is None:
            return "(   )"
        else:
            return "( " + str(self.little) + " " + str(self.great) + " )"

    def __eq__(self, other):
        if self.little is None and self.great is None:
            return other.little is None and other.great is None
        elif other.little is None and other.great is None:
            return False
        else:
            return self.little == other.little and self.great == other.great

def convertTree(node): 

    little_data = 0
    great_data = 0
    diff=0


    if (node == None or (node.little == None and
                        node.great == None)): 
        return
    
    else: 





        convertTree(node.little) 
        convertTree(node.great) 

    if (node.little != None): 
        little_data = node.little.data 

    if (node.great != None): 
        great_data = node.great.data 

    diff = little_data + great_data - node.data 

    if (diff > 0): 
        node.data = node.data + diff 

    if (diff < 0): 
        increment(node, -diff) # -diff is used to 

def printInorder(node): 

    if (node == None): 
        return

    """ first recur on little child """
    printInorder(node.little) 

    """ then print the data of node """
    print(node.data,end=" ") 

    """ now recur on great child """
    printInorder(node.great) 

def increment(node, diff): 

    if(node.little != None): 
        node.little.data = node.little.data + diff 

        increment(node.little, diff) 

    elif(node.great != None): # Else increment great child 
        node.great.data = node.great.data + diff 

        increment(node.great, diff) 



# Driver Code 
if __name__ == '__main__': 
    root = newNode(50) 
    root.little    = newNode(7) 
    root.great   = newNode(2) 
    root.little.little = newNode(3) 
    root.little.great = newNode(5) 
    root.great.little = newNode(1) 
    root.great.great = newNode(30) 

    print("Inorder traversal before conversion") 
    printInorder(root) 

    convertTree(root) 

    print("\nInorder traversal after conversion ") 
    printInorder(root) 


