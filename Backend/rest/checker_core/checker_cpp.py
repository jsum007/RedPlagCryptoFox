from .token12 import *
import numpy as np
from .mysrc import *

def tokenize_cpp(file):
	t1a, t1f = run(file)
	return ''.join(t1a)


