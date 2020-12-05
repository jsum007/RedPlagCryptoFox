import mysrc

global comment
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

def delimiterCorrection(line,comment):
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

    print(tokens)
    # print('-----')

    return [comment,tokens]

# def removeComments(tokens,comment):
#     tokens = tokens
#     print(tokens)
#     k = 0
#     for i in range(len(tokens)):
#         if comment:
#             if '*/' in tokens[k]:
#                 comment = False
#             tokens.remove(tokens[k])
#             k = k-1
#         else:
#             for sym in ['//','/*']:
#                 if sym in tokens[k]:
#                     comment = True
#                 if sym in tokens[k]:
#                     words = tokens[k].split(sym)
#                     if not len(words[0]):
#                         tokens[k].replace(tokens[k],words[0])
#                     else:
#                         tokens.remove(tokens[k])
#                 k = k-1
#         k = k+1

#     print(tokens)

#     return tokens

path = "sample4.cpp"
f = open(path).read()
lines = f.split("\n")
count = 0
comment = False
for line in lines:
    count = count + 1
    comment,tokens = delimiterCorrection(line,comment)
    # print(comment)
    # tokens = removeComments(tokens)
    # for word in line()