from winnowing import winnow
import sys

from .checker_cpp import tokenize_cpp
from .checker_py import tokenize_py


'''with open(sys.argv[1], 'r') as fh:
	data = fh.read()

fpr= winnow(data)
print(fpr)
'''


def plagRatio(data1,data2, kval=5):
	
	fpr1= winnow(data1, kval)
	fpr2= winnow(data2, kval)

	fpr_wopos1 = []
	fpr_wopos2 = []

	for f1 in fpr1:
		fpr_wopos1.append(f1[1])

	for f1 in fpr2:
		fpr_wopos2.append(f1[1])

	comfpr=list(set(fpr_wopos1) & set(fpr_wopos2))

	ratio= len(comfpr)/min(len(fpr_wopos2),len(fpr_wopos1))

	#print(fpr_wopos2)

	return ratio

#print(plagCheck('sample2.cpp', 'sample1.cpp',5))

def plagCheck(file1,file2, kval=5):

	if file1.endswith(".cpp") and file2.endswith(".cpp"):
		data1 = tokenize_cpp(file1)
		data2 = tokenize_cpp(file2)

	if file1.endswith(".py") and file2.endswith(".py"):
		data1 = tokenize_py(file1)
		data2 = tokenize_py(file2)


	result = plagRatio(data1, data2, kval)

	return result

