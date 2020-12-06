import tokens12 as tk
import numpy as np
import mysrc

t1a, t1f = tk.run('sample1.cpp')

t2a, t2f = tk.run('sample2.cpp')

print(t1a)
print(t2a)

word_to_onehot = {}
num_to_word = {}

vocab_list = mysrc.keywords() + list(mysrc.operators().keys())
size_onehot = len(vocab_list)
#print(vocab_list)

for i in range(len(vocab_list)):
	word_to_onehot[vocab_list[i]] = np.zeros((1, size_onehot+3))
	word_to_onehot[vocab_list[i]][0, i] = 1;

	num_to_word[str(i)] = vocab_list[i]

num_to_word[str(size_onehot)] = 'num'
num_to_word[str(size_onehot+1)] = 'v'
num_to_word[str(size_onehot+2)] = 'head'

word_to_onehot['num'] = np.zeros((1, size_onehot+3))
word_to_onehot[vocab_list[i]][0, size_onehot] = 1;
word_to_onehot['v'] = np.zeros((1, size_onehot+3))
word_to_onehot[vocab_list[i]][0, size_onehot+1] = 1;
word_to_onehot['head'] = np.zeros((1, size_onehot+3))
word_to_onehot[vocab_list[i]][0, size_onehot+2] = 1;

size_onehot += 3;


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



