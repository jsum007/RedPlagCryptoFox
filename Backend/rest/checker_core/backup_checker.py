import pygments.token
import pygments.lexers
import os, re

#Python module pygments is used to tokenize_py the code files. This module supports most of the popular languages
#http://pygments.org/languages/
#Hence this program can be used to clean up codes written in most languages


def backup_tokenize(filename):
    file = open(filename, "r")
    if os.path.exists("work"): 
        os.remove("work")
    work = open('work', 'a')
    func_text = {}
    #pat = '(\w*\s*\w*\s*\w+\s+\w+\s*\([^\)]\))'
    line_no = 0
    func_pos = []
    in_func = -1

    for l in file:
        if l == '' or l.isspace():
            pass
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
    #tok_ex = []
    class_list = []

    scope_depth = 0

    #print(tokens)
    #print('ggggggggggggggg')
    #count1 = 0    #tag to store corresponding position of each element in original code file
    #count2 = 0    #tag to store position of each element in cleaned up code text
    # these tags are used to mark the plagiarized content in the original code files.

    for i in range(lenT):
        #print(tokens[i])

        if tokens[i][0] == pygments.token.Name.Function:
            #print(scope_depth)
            tokens1.append('function')

        elif tokens[i][0] == pygments.token.Name.Class or str(tokens[i][1]) in class_list:
            class_list.append(str(tokens[i][1]))
            tokens1.append('class')

        elif (tokens[i][0] == pygments.token.Name or tokens[i][0] in pygments.token.Name) and not i == lenT - 1 and not tokens[i + 1][1] == '(':
            #result.append(('N', count1, count2))  #all variable names as 'N'
            
            if str(tokens[i][1]) in class_list:
                tokens1.append('obj')

            elif tokens[i][0] in pygments.token.Name.Namespace:
                tokens1.extend(str(tokens[i][0]).split())

            elif tokens[i][0] in pygments.token.Name.Builtin or tokens[i][0] in pygments.token.Name.Attribute or tokens[i][0] in pygments.token.Name.Decorator :
                tokens1.append(str(tokens[i][1]))

            else:
                tokens1.append('v')
            #count2 += 1

        elif tokens[i][0] in pygments.token.Literal.String:
            pass
            #result.append(('S', count1, count2))  #all strings as 'S'
            #count2 += 1
        elif tokens[i][0] == pygments.token.Text or tokens[i][0] in pygments.token.Comment or tokens[i][0] in pygments.token.Punctuation:
            pass   #whitespaces and comments ignored

        else:
            tokens1.append(str(tokens[i][1]))

    if os.path.exists("work"):
        os.remove("work")

    return ''.join(tokens1)

