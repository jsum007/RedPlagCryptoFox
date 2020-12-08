import pygments.token
import pygments.lexers
import os, re

#Python module pygments is used to tokenize_py the code files. This module supports most of the popular languages
#http://pygments.org/languages/
#Hence this program can be used to clean up codes written in most languages

def func_adder(filename, name, func_text, func_tokens, class_list):
    text = func_text[name]
    lexer = pygments.lexers.guess_lexer_for_filename(filename, text)
    tokens = lexer.get_tokens(text)
    tokens = list(tokens)
    result = []
    lenT = len(tokens)
    tokens1 = []

    for i in range(lenT):
        if tokens[i][0] == pygments.token.Name.Class:
            class_list.append(str(tokens[i][1]))

    for i in range(lenT):
        
        if (tokens[i][0] == pygments.token.Name or tokens[i][0] in pygments.token.Name) and not i == lenT - 1 and not tokens[i + 1][1] == '(':
            
            if tokens[i][0] == pygments.token.Name.Class or str(tokens[i][1]) in class_list:
                tokens1.append('class')

            elif tokens[i][0] in pygments.token.Name.Builtin or tokens[i][0] in pygments.token.Name.Function \
                    or tokens[i][0] in pygments.token.Name.Attribute or tokens[i][0] in pygments.token.Name.Decorator \
                    or tokens[i][0] in pygments.token.Name.Namespace:
                tokens1.append(str(tokens[i][1]))
                if tokens[i][0] in pygments.token.Name.Function:
                    print(tokens[i][1])
            else:
                tokens1.append('v')
            

        elif tokens[i][0] == pygments.token.Name.Class:
            class_list.append(str(tokens[i][1]))
            tokens1.append('class')
            
        elif tokens[i][0] in pygments.token.Literal.String:
            pass
        elif str(tokens[i][1]) in func_tokens.keys():
            tokens1.extend(func_tokens[str(tokens[i][1])])

        elif str(tokens[i][1]) in func_text.keys():
            if str(tokens[i][1]) != name:
                func_tokens[str(tokens[i][1])] = func_adder(filename, str(tokens[i][1]), func_text, func_tokens, class_list)
                tokens1.extend(func_tokens[str(tokens[i][1])])
            else:
                pass
        elif tokens[i][0] == pygments.token.Text or tokens[i][0] in pygments.token.Comment or tokens[i][0] in pygments.token.Punctuation:
            pass   #whitespaces and comments ignored
        else: 

            tokens1.append(str(tokens[i][1]))
    return tokens1



def tokenize_py(filename):
    file = open(filename, "r")
    if os.path.exists("work"): 
        os.remove("work")
    work = open('work', 'a')
    func_text = {}
    pat = r'^def +(\w)*\(.*?\):'
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
                func_pos.append(line_no)
                in_func = name
                func_text[name] = ''
        
            else:
                work.write(l.rstrip())
                work.write('\n')
        line_no += 1
    
    file.close()
    work.close()
    file = open('work', 'r')
    text = file.read()

    lexer = pygments.lexers.guess_lexer_for_filename(filename, text)
    tokens = lexer.get_tokens(text)
    tokens = list(tokens)
    result = []
    lenT = len(tokens)
    tokens1 = []
    func_tokens = {}
    class_list = []

    for i in range(lenT):
        if tokens[i][0] == pygments.token.Name.Class:
            class_list.append(str(tokens[i][1]))

    for i in range(lenT):
        if tokens[i][0] == pygments.token.Name.Class:
            class_list.append(str(tokens[i][1]))
            tokens1.append('class')

        elif (tokens[i][0] == pygments.token.Name or tokens[i][0] in pygments.token.Name) and not i == lenT - 1 and not tokens[i + 1][1] == '(':
            if tokens[i][0] == pygments.token.Name.Class or str(tokens[i][1]) in class_list:
                tokens1.append('class')

            elif tokens[i][0] in pygments.token.Name.Builtin or tokens[i][0] in pygments.token.Name.Function \
                    or tokens[i][0] in pygments.token.Name.Attribute or tokens[i][0] in pygments.token.Name.Decorator \
                    or tokens[i][0] in pygments.token.Name.Namespace:
                tokens1.append(str(tokens[i][1]))

            else:
                tokens1.append('v')

        elif tokens[i][0] in pygments.token.Literal.String:
            pass

        elif str(tokens[i][1]) in func_tokens.keys():
            tokens1.extend(func_tokens[str(tokens[i][1])])

        elif str(tokens[i][1]) in func_text.keys():
            func_tokens[str(tokens[i][1])] = func_adder(filename, str(tokens[i][1]), func_text, func_tokens, class_list)
            tokens1.extend(func_tokens[str(tokens[i][1])])

        elif tokens[i][0] == pygments.token.Text or tokens[i][0] in pygments.token.Comment or tokens[i][0] in pygments.token.Punctuation:
            pass   #whitespaces and comments ignored
        else:
            tokens1.append(str(tokens[i][1]))

    if os.path.exists("work"):
        os.remove("work")

    print(str(' '.join(tokens1)))
    print('\n')
    return ' '.join(tokens1)
