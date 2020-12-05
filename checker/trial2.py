a = ['a','b','c','d']
j = 0
for i in range(len(a)):
	if a[j] == 'c':
		a.remove(a[j])
		j = j-1
	else:
		print(a[j])
	j = j+1