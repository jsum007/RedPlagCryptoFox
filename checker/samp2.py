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


def mirrorTree(node):
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


def allTrees(n):
	"""
	Returns a list of all unique trees with n internal nodes
	"""
	trees = []
	tot = 2*n+1
	if n==0:
		trees.append(Node())
		return trees






	for i in range(0, n, 1):
		lTree = allTrees(i)
		rTree = allTrees(n-i-1)
		trees1 = [Node(l,r) for l in lTree for r in rTree]
		trees= trees+trees1

	return trees


def allSymTrees(n):
	"""
	Returns a list of all unique symmetrical trees with n internal nodes
	"""
	trees = []
	if n==0:
		trees.append(Node())
		return trees
	if(n%2 == 0):




		return trees

	lTree = allTrees(int((n-1)/2))
	trees = [Node(head,head) for head in lTree if head==mirrorTree(head)]

	return trees


if __name__ == '__main__':
	'''for x in allSymTrees(int(input())):
		print(x)
	node = Node(Node(Node(), Node()), Node())
	print(node)'''
	for i in range(24):
		print(i, len(allSymTrees(i)))