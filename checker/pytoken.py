import pygments.token
import pygments.lexers

#Python module pygments is used to tokenize the code files. This module supports most of the popular languages
#http://pygments.org/languages/
#Hence this program can be used to clean up codes written in most languages

# given a file path this file returns tokens
def tokenize(filename):
	file = open(filename, "r")
	text = file.read()
	file.close()
	lexer = pygments.lexers.guess_lexer_for_filename(filename, text)
	tokens = lexer.get_tokens(text)
	tokens = list(tokens)
	# print(tokens)
	result = []
	lenT = len(tokens)
	imports = False
	is_func = False
	func_replace = False
	var = 0
	func = 0
	functions = {}
	function_replacement = {}
	parath = 0
	variables = {}

	for i in range(lenT):
		if func_replace:
			if tokens[i][1] == '(':
				parath += 1
			elif tokens[i][1] == ')':
				parath -= 1
			if parath == 0:
				func_replace = False
			continue
		if tokens[i][1] == 'from' or tokens[i][1] == 'import':
			imports = True
		if imports:
			if tokens[i][1] == '\n':
				imports = False
			continue
		if is_func:
			if tokens[i][1] == '\n' and (i == lenT-1 or (tokens[i+1][1][0] != '\t' and tokens[i+1][1] != '\n')):
				is_func = False

			if tokens[i][0] not in pygments.token.Comment and tokens[i][0] != pygments.token.Text:
				if tokens[i][0] == pygments.token.Name and not i == lenT - 1:
					if tokens[i][1] in function_replacement.keys():
						functions[list(functions.keys())[-1]].append(function_replacement[tokens[i][1]])
					elif tokens[i][1] in variables.keys():
						functions[list(functions.keys())[-1]].append(variables[tokens[i][1]])
					else:
						var += 1
						variables[tokens[i][1]] = 'Var'+str(var)
						functions[list(functions.keys())[-1]].append(variables[tokens[i][1]])
				elif tokens[i][0] in pygments.token.Literal.String:
					functions[list(functions.keys())[-1]].append('S')
				elif tokens[i][0] in pygments.token.Number:
					functions[list(functions.keys())[-1]].append('N')
				else:	
					functions[list(functions.keys())[-1]].append(tokens[i][1])

		if tokens[i][0] == pygments.token.Name and not i == lenT - 1: 
			if tokens[i + 1][1] == '(' and tokens[i][1] in functions.keys():
				if not is_func:
					func_replace = True
					result.extend(functions[tokens[i][1]])
					continue
				else:
					if tokens[i][1] in function_replacement.keys():
						result.append(function_replacement[tokens[i][1]])
			else:
				if tokens[i][1] in variables.keys():
					result.append(variables[tokens[i][1]])
				else:
					var += 1
					variables[tokens[i][1]] = 'Var'+str(var)
					result.append(variables[tokens[i][1]])

		elif tokens[i][0] in pygments.token.Literal.String:
			result.append('S')
		elif tokens[i][0] in pygments.token.Name.Function and not is_func:
			func+=1
			functions[tokens[i][1]] = []
			is_func = True
			function_replacement[tokens[i][1]] = 'Func'+str(func)
			functions[list(functions.keys())[-1]].extend([tokens[i-2][1],'Func'+str(func)])

			result.append('Func'+str(func))
		elif tokens[i][0] in pygments.token.Number:
			result.append('N')
		elif tokens[i][0] == pygments.token.Text or tokens[i][0] in pygments.token.Comment:
			pass
		else:
			result.append(tokens[i][1])

	return toText(result)

def toText(arr):
	cleanText = ''.join(str(x) for x in arr)
	return cleanText

# tokens = tokenize('sample6.py')
# print(tokens)