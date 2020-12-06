class point(object):
	"""
	point contains two objects - a left and a right child, both may be a point or both None,
	latter representing a leaf
	"""
	def __init__(self, left=None, right=None):
		super(point, self).__init__()
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


def mirrorRoot(node):
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


def allRoots(n):
	"""
	Returns a list of all unique trees with n internal nodes
	"""
	trees = []
	tot = 2*n+1
	if n==0:
		trees.append(point())
		return trees

'''jghftuugcdctgf;ho
jjbghbjhhlkj;lkpl;k;ljlhujshdgchshdvcksdva
alkfchjhfuacjanhfewiyeiuifjsnjlvbjshcigfief
ojddjdvjgwufuworurugwrisikajipfiqrqe8r6989r6yeury	2275uihsvnds
ahfuweeyf7yt7ry38632wfuuegfuciqfhuitqyiegfalhAKHFEF
egoiy723t37793r748249ptuwarlighsdlkkvnldvjhsdf;uhsf'''




	for i in range(0, n, 1):
		lRoot = allRoots(i)
		rRoot = allRoots(n-i-1)
		trees1 = [point(l,r) for l in lRoot for r in rRoot]
		trees= trees+trees1

	return trees


def allSymRoots(n):
	"""
	Returns a list of all unique symmetrical trees with n internal nodes
	"""
	trees = []
	if n==0:
		trees.append(point())
		return trees
	if(n%2 == 0):




		return trees

	lRoot = allRoots(int((n-1)/2))
	trees = [point(head,head) for head in lRoot if head==mirrorRoot(head)]

	return trees


if __name__ == '__main__':
	'''for x in allSymRoots(int(input())):
		print(x)
	node = point(point(point(), point()), point())
	print(node)'''
	for i in range(24):
		print(i, len(allSymRoots(i)))