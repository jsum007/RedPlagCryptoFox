import javalang
import pygments.token
import pygments.lexers

filename = 'javatests/07.java'

file = open(filename, 'r')
text = file.read()


lexer = pygments.lexers.guess_lexer_for_filename(filename, text)
tokens = lexer.get_tokens(text)
tokens = list(tokens)
print('aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa')
for t in tokens:
	print(t)

print('aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaabbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb')

'''tree = javalang.parse.parse(text)

for path, node in tree:
	print (path)
	print(node)'''
