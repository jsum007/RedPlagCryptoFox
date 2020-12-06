import pygments.token
import pygments.lexers
import os, re

#Python module pygments is used to tokenize the code files. This module supports most of the popular languages
#http://pygments.org/languages/
#Hence this program can be used to clean up codes written in most languages

#def func_lexer(filename, text)

def func_adder(filename, name, func_text, func_tokens):
    text = func_text[name]
    lexer = pygments.lexers.guess_lexer_for_filename(filename, text)
    tokens = lexer.get_tokens(text)
    tokens = list(tokens)
    result = []
    lenT = len(tokens)
    tokens1 = []

    for i in range(lenT):
        #print(tokens[i])
        if tokens[i][0] == pygments.token.Name and not i == lenT - 1 and not tokens[i + 1][1] == '(':
            tokens1.append('v')
            
        elif tokens[i][0] in pygments.token.Literal.String:
            pass
        elif str(tokens[i][1]) in func_tokens.keys():
            tokens1.extend(func_tokens[str(tokens[i][1])])

        elif str(tokens[i][1]) in func_text.keys():
            if str(tokens[i][1]) != name:
                func_tokens[str(tokens[i][1])] = func_adder(filename, str(tokens[i][1]), func_text, func_tokens)
                tokens1.extend(func_tokens[str(tokens[i][1])])
            else:
                pass
        elif tokens[i][0] == pygments.token.Text or tokens[i][0] in pygments.token.Comment or tokens[i][0] in pygments.token.Punctuation:
            pass   #whitespaces and comments ignored
        else:  
            tokens1.append(str(tokens[i][1]))
            #tuples in result-(each element e.g 'def', its position in original code file, position in cleaned up code/text) 
    return tokens1



def tokenize(filename):
    file = open(filename, "r")
    if os.path.exists("work"): 
        os.remove("work")
    work = open('work', 'a')
    func_text = {}
    pat = '^def +\w*\(.*?\):'
    line_no = 0
    func_pos = []
    in_func = -1

    for l in file:
        if l == '' or l.isspace():
            pass
        elif l[0] == '\t' and in_func != -1:
            func_text[name] += l

        else:
            match = re.search(pat, l)
            in_func = -1
        
            if match is not None:
                name = match.string.split()[1]
                name = name.split('(')[0]
                #print(name)
                func_pos.append(line_no)
                in_func = name
                func_text[name] = ''
        
            else:
                work.write(l.rstrip())
                work.write('\n')
        line_no += 1
    
    file.close()
    work.close()
    #print(len(func_text))
    file = open('work', 'r')
    text = file.read()

    lexer = pygments.lexers.guess_lexer_for_filename(filename, text)
    tokens = lexer.get_tokens(text)
    tokens = list(tokens)
    result = []
    lenT = len(tokens)
    tokens1 = []
    func_tokens = {}

    #print(tokens)
    #print('ggggggggggggggg')
    #count1 = 0    #tag to store corresponding position of each element in original code file
    #count2 = 0    #tag to store position of each element in cleaned up code text
    # these tags are used to mark the plagiarized content in the original code files.

    for i in range(lenT):
        #print(tokens[i])
        if tokens[i][0] == pygments.token.Name and not i == lenT - 1 and not tokens[i + 1][1] == '(':
            #result.append(('N', count1, count2))  #all variable names as 'N'
            if tokens[i][0] in pygments.token.Name.Builtin:
                tokens1.append(str(tokens[i][1]))

            elif tokens[i][0] in pygments.token.Name.Function:
                #result.append(('F', count1, count2))   #user defined function names as 'F'
                #count2 += 1
                tokens1.append(str(tokens[i][1]))
            else:
                tokens1.append('v')
            #count2 += 1

        elif tokens[i][0] in pygments.token.Literal.String:
            pass
            #result.append(('S', count1, count2))  #all strings as 'S'
            #count2 += 1

        elif str(tokens[i][1]) in func_tokens.keys():
            tokens1.extend(func_tokens[str(tokens[i][1])])

        elif str(tokens[i][1]) in func_text.keys():
            func_tokens[str(tokens[i][1])] = func_adder(filename, str(tokens[i][1]), func_text, func_tokens)
            tokens1.extend(func_tokens[str(tokens[i][1])])


        elif str(tokens[i][1]) in func_text.keys():
            tokens1.extend(func_adder(filename, str(tokens[i][1]), func_text, func_tokens))

        elif tokens[i][0] == pygments.token.Text or tokens[i][0] in pygments.token.Comment or tokens[i][0] in pygments.token.Punctuation:
            pass   #whitespaces and comments ignored
        else:
            #result.append((tokens[i][1], count1, count2))  
            tokens1.append(str(tokens[i][1]))
            #tuples in result-(each element e.g 'def', its position in original code file, position in cleaned up code/text) 
            #count2 += len(tokens[i][1])
        #count1 += len(tokens[i][1])

    print(''.join(tokens1))

    return result

def toText(arr):
    cleanText = ''.join(str(x[0]) for x in arr)
    return cleanText

tokenize('samp2.py')