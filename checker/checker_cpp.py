import tokens12 as tk
import numpy as np
import mysrc

def tokenize_cpp(file):
	t1a, t1f = tk.run(file)
	return ''.join(t1a)


file2 = tokenize_cpp('sample2.cpp')
file1 = tokenize_cpp('sample4.cpp')


print(file1)
print(file2)