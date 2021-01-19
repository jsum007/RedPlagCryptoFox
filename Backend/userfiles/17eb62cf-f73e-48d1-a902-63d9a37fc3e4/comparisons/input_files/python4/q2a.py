# Program to convert an aribitary binary tree 
# to a tree that holds children sum property 

# Helper function that allocates a new 
# node with the given data and None 
# left and right poers.									 
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

# This function changes a tree to 
# hold children sum property 
def convertTree(node): 

	left_data = 0
	right_data = 0
	diff=0

	# If tree is empty or it's a 
	# leaf node then return true 
	if (node == None or (node.left == None and
						node.right == None)): 
		return
	
	else: 
		
		""" convert left and right subtrees """
		convertTree(node.left) 
		convertTree(node.right) 

	""" If left child is not present then 0 
	is used as data of left child """
	if (node.left != None): 
		left_data = node.left.data 

	""" If right child is not present then 0 
	is used as data of right child """
	if (node.right != None): 
		right_data = node.right.data 

	""" get the diff of node's data 
		and children sum """
	diff = left_data + right_data - node.data 

	""" If node's children sum is greater 
		than the node's data """
	if (diff > 0): 
		node.data = node.data + diff 

	""" THIS IS TRICKY -. If node's data is 
	greater than children sum, then increment 
	subtree by diff """
	if (diff < 0): 
		increment(node, -diff) # -diff is used to 
							# make diff positive 

""" This function is used to increment 
	subtree by diff """
def increment(node, diff): 

	""" IF left child is not None 
		then increment it """
	if(node.left != None): 
		node.left.data = node.left.data + diff 

		# Recursively call to fix the 
		# descendants of node.left 
		increment(node.left, diff) 

	elif(node.right != None): # Else increment right child 
		node.right.data = node.right.data + diff 

		# Recursively call to fix the 
		# descendants of node.right 
		increment(node.right, diff) 

""" Given a binary tree, printInorder() 
prints out its inorder traversal"""
def printInorder(node): 

	if (node == None): 
		return

	""" first recur on left child """
	printInorder(node.left) 

	""" then print the data of node """
	print(node.data,end=" ") 

	""" now recur on right child """
	printInorder(node.right) 

# Driver Code 
if __name__ == '__main__': 
	root = newNode(50) 
	root.left	 = newNode(7) 
	root.right	 = newNode(2) 
	root.left.left = newNode(3) 
	root.left.right = newNode(5) 
	root.right.left = newNode(1) 
	root.right.right = newNode(30) 

	print("Inorder traversal before conversion") 
	printInorder(root) 

	convertTree(root) 

	print("\nInorder traversal after conversion ") 
	printInorder(root) 

# This code is contributed by 
# Shubham Singh(SHUBHAMSINGH10) 
