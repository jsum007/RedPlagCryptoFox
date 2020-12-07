import javalang

file = open('samp1.java', 'r')
text = file.read()

tokens = list(javalang.tokenizer.tokenize(text))

for t in tokens:
	print(t)