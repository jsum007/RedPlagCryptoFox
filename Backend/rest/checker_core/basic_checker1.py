from .code2 import * 
import numpy as np
from .mysrc import *
import sys

#file1 = sys.argv[1]
#file2 = sys.argv[2]


def compare(file1, file2):
	t1a, t1b = run(str(file1))
 	
	t2a, t2b = run(str(file2))

	word_to_onehot = {}
	num_to_word = {}

	vocab_list = keywords() + list(operators().keys())
	size_onehot = len(vocab_list)
	#print(vocab_list)

	for i in range(len(vocab_list)):
		word_to_onehot[vocab_list[i]] = np.zeros((1, size_onehot))
		word_to_onehot[vocab_list[i]][0, i] = 1;

		num_to_word[str(i)] = vocab_list[i]

	num_tokens = max(len(t1a), len(t2a))

	file1_onehot = np.zeros((num_tokens, size_onehot))
	file2_onehot = np.zeros((num_tokens, size_onehot))

	for i in range(len(t1a)):
		file1_onehot[i, :] = word_to_onehot[t1a[i]]

	for i in range(len(t2a)):
		file2_onehot[i, :] = word_to_onehot[t2a[i]]


	ans1 = np.sum(np.dot(file1_onehot, file2_onehot.T))/np.sum(np.dot(file1_onehot, file1_onehot.T))
	ans2 = np.sum(np.dot(file1_onehot, file2_onehot.T))/np.sum(np.dot(file2_onehot, file2_onehot.T))
	ans = np.sqrt(ans2*ans1)

	return ans
	



