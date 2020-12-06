import re
import mysrc

global comment
def basicCheck(token, tokens1, tokens2):
    varPtrn = re.compile(r"[a-zA-Z_][a-zA-Z0-9_]")  # variables
    headerPtrn = re.compile(r"\w[a-zA-Z]+[.]h")  # header files
    digitPtrn = re.compile(r'\d')
    floatPtrn = re.compile(r'\d+[.]\d+')

    if token in mysrc.keywords():
        #print(token + " KEYWORD")
        tokens1.append(token)
    elif token in mysrc.operators().keys():
        #print(token + " ", mysrc.operators()[token])
        tokens1.append(token)
    elif token in mysrc.delimiters():
        description = mysrc.delimiters()[token]
        if description == 'TAB' or description == 'NEWLINE':
            #print(description)
            pass
        else:
            pass
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

    # print(tokens1)

    return True

def removeComments(line,comment):

    tokens = line.split(" ")
    # print('-----')
    # print(tokens)
    k = 0
    ln = len(tokens)
    for i in range(ln):
        if k<0:
            k = 0
        if '//' in tokens[k]:
            tokens[k] = tokens[k].split('//')[0]
            tokens = tokens[:k+1]
            if len(tokens[k]) == 0:
                tokens.remove(tokens[k])
            break
        if comment:
            if '*/' in tokens[k]:
                tokens[k] = tokens[k].replace(tokens[k].split('*/')[0]+'*/','')
                comment = False
            else:
                tokens.remove(tokens[k])
            k = k-1
        elif '/*' in tokens[k]:
            comment = True
            word1 = tokens[k].split('/*')[0]
            tokens[k] = tokens[k].replace(tokens[k].split('/*')[0]+'/*','')
            tokens.insert(k,word1)
            if '*/' in tokens[k+1]:
                comment = False
                tokens[k+1] = tokens[k+1].replace(tokens[k+1].split('*/')[0]+'*/','')
                if len(tokens[k+1]) == 0:
                    tokens.remove(tokens[k+1])
                else:
                    k = k+1
            else:
                tokens.remove(tokens[k+1])
        if len(tokens[k]) == 0:
            tokens.remove(tokens[k])
            k = k-1
        if len(tokens) == 0:
            tokens = ['']
        k = k+1
        if k >= len(tokens):
            break
    return [comment,tokens]

def delimiterCorrection(tokens):
    
    # print(tokens)
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

    # print(tokens)

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
        count = 0
        comment = False
        for line in lines:
            count = count + 1
            comment,tokens = removeComments(line,comment)
            tokens = delimiterCorrection(tokens)
            #print("\n#LINE ", count)
            #print("Tokens: ", tokens)
            for token in tokens:
                basicCheck(token, tokens1, tokens2)
        #print(count)
        return True
    except FileNotFoundError:
        print("\nInvalid Path. Retry")
        # run()

def run(path):
    #path = input("Enter Source Code's Path: ")
    
    tokens1 = []
    tokens2 = []
    tokenize(path, tokens1, tokens2)
    return tokens1, tokens2

#run()