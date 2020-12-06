import pytoken
import cpptoken
import numpy as np
import mysrc
import sys

# file1 = sys.argv[1]
# file2 = sys.argv[2]
file1 = 'sample6.py'
file2 = 'sample7.py'
filetype = file1.split('.')[-1]

if filetype == 'cpp':
	tokeniser = cpptoken
elif filetype == 'py':
	tokeniser = pytoken
	
t1a, t1b = tokeniser.run(file1)
t2a, t2b = tokeniser.run(file2)

print(t1a)
print(t1b)
word_to_onehot = {}
num_to_word = {}

vocab_list = mysrc.keywords() + list(mysrc.operators().keys())
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



#print("t1a: ", t1a)
#print("t1b: ", t1b)
#print("t2a: ", t2a)
#print("t2b: ", t2b)
#print("file2_onehot: ", file2_onehot)
#print("file1_onehot: ", file1_onehot)

ans1 = np.sum(np.dot(file1_onehot, file2_onehot.T))/np.sum(np.dot(file1_onehot, file1_onehot.T))
ans2 = np.sum(np.dot(file1_onehot, file2_onehot.T))/np.sum(np.dot(file2_onehot, file2_onehot.T))
ans = np.sqrt(ans2*ans1)

print("ans: ", ans)



