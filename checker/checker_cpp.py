import tokens12 as tk
import numpy as np
import mysrc

def check_cpp(file):
	t1a, t1f = tk.run(file)
	return ' '.join(t1a)


file2 = check_cpp('sample2.cpp')
file1 = check_cpp('sample4.cpp')


print(file1)
print(file2)