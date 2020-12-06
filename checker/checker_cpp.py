import tokens12 as tk
import numpy as np
import mysrc

t1a, t1b, t1f = tk.run('sample3.cpp')

t2a, t2b, t2f = tk.run('sample2.cpp')

file1 = ''.join(t1a)
file2 = ''.join(t2a)

print(file1)
print(file2)