import re
import mysrc

scope_depth = 0
is_comment = False
is_function = False
is_class = False

def basicCheck(token, tokens1, tokens2):
    varPtrn = re.compile(r"[a-zA-Z_][a-zA-Z0-9_]")  # variables
    headerPtrn = re.compile(r"\w[a-zA-Z]+[.]h")  # header files
    digitPtrn = re.compile(r'\d')
    floatPtrn = re.compile(r'\d+[.]\d+')

    if token in mysrc.delimiters():
        description = mysrc.delimiters()[token]
        if description == 'LCBRACE':
            scope_depth += 1
        elif description == 'RCBRACE':
            scope_depth -= 1
        else:
            pass
    elif token in mysrc.keywords():
        #print(token + " KEYWORD")
        tokens1.append(token)
    elif token in mysrc.operators().keys():
        #print(token + " ", mysrc.operators()[token])
        tokens1.append(token)
    
    elif re.search(headerPtrn, token):
        #print(token + " HEADER")
        tokens2.append(token)
    elif re.match(varPtrn, token) or "'" in token or '"' in token:
        #print(token + ' IDENTIFIER' )
        tokens2.append(token)
    elif re.match(digitPtrn, token):
        if re.match(floatPtrn, token):
            #print(token + ' FLOAT')
            tokens2.append(token)
        else:
            #print(token + ' INT')
            tokens2.append(token)

    return True

def delimiterCorrection(line):
    
    #
    print(line)
    tokens = line.split(" ")
    for delimiter in mysrc.delimiters().keys():
        for token in tokens:

            if token == delimiter:
                pass
            elif delimiter in token:
                pos = token.find(delimiter)
                tokens.remove(token)
                token = token.replace(delimiter, " ")
                extra = token[:pos]
                token = token[pos + 1 :]
                tokens.append(delimiter)
                tokens.append(extra)
                tokens.append(token)
            else:
                pass
    for token in tokens:
        if isWhiteSpace(token):
            tokens.remove(token)
        elif ' ' in token:
            tokens.remove(token)
            token = token.split(' ')
            for d in token:
                tokens.append(d)
    return tokens

def isWhiteSpace(word):
    ptrn = [ " ", "\t", "\n"]
    for item in ptrn:
        if word == item:
            return True
        else:
            return False

def hasWhiteSpace(token):
    ptrn = ['\t', '\n']
    if isWhiteSpace(token) == False:
        for item in ptrn:
            if item in token:
                result = "'" + item + "'"
                return result
            else:
                pass
    return False

def tokenize(path, tokens1, tokens2):
    try:
        f = open(path).read()
        lines = f.split("\n")
        #file_token[len(lines)]

        for line in lines:
            line = line.strip()
            if line is not None and line is not '':
                tokens = delimiterCorrection(line)
                print(tokens)
                #print("\n#LINE ", count)
                #print("Tokens: ", tokens)
                for token in tokens:
                    basicCheck(token, tokens1, tokens2)
        #print(count)
        return True
    except FileNotFoundError:
        print("\nInvald Path. Retry")
        run()

def run(path):
    #path = input("Enter Source Code's Path: ")
    
    tokens1 = []
    tokens2 = []
    tokenize(path, tokens1, tokens2)
    return tokens1, tokens2

#run()