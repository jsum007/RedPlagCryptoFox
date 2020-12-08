import re
import os

scope_depth = 0
is_comment = False
is_function = -1
is_class = False

from pygccxml import utils
from pygccxml import declarations
from pygccxml import parser

# Find out the c++ parser
generator_path, generator_name = utils.find_xml_generator()

# Configure the xml generator
xml_generator_config = parser.xml_generator_configuration_t(
    xml_generator_path=generator_path,
    xml_generator=generator_name)

decls, global_namespace, std = None, None, None


def keywords():
    keywords = [
    "break", "case", "catch", "word", "class", "const", "continue", "delete", "do", "else", "false", "for", "goto", "if", 
    "namespace", "not", "or", "private", "protected", "public", "return", "signed", "sizeof", "static", "struct", "switch", "true", "try", "unsigned", "void", "while",
    "endl", "cout", "cin", 
    ]
    #print(len(keywords)) = 36
    return keywords

def identifiers():
    identifiers = [
    "auto", "bool", "char", "double", "enum", "float", "int", "long", "short", "string" ]
    #print(len(identifiers)) = 10
    return identifiers

def operators():
    operators = {
    "+": "PLUS", "-": "MINUS", "*": "MUL", "/": "DIV", "%": "MOD", "+=": "PLUSEQ", "-=": "MINUSEQ", "*=": "MULEQ", "/=": "DIVEQ", "++": "INC", "--": "DEC", "|": "OR", "&&": "AND", "&": "REF",
    }
    #print(len(operators)) = 14
    return operators

def delimiters():
    delimiters = {
    "\t": "TAB", "\n": "NEWLINE","(": "LPAR", ")": "RPAR", "[": "LBRACE", "]": "RBRACE", "{": "LCBRACE", "}": "RCBRACE", "=": "ASSIGN",":": "COLON", ",": "COMMA", ";": "SEMICOL", "<<": "OUT", ">>": "IN",
    }
    #print(len(delimiters)) = 14
    return delimiters

def add_func(token, func_tokens):
    new_list = []
    for t in func_tokens[token]:
        if t != token:
            if t in func_tokens:
                new_list = new_list + add_func(t, func_tokens)
            else:
                new_list.append(t)

    return new_list



def basicCheck(token, tokens1, func_tokens, class_list):
    global scope_depth, is_function
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
            if is_function != -1 and scope_depth == 0:
                is_function = -1
            
        else:
            pass
    elif token in mysrc.keywords():
        
        if is_function != -1:
            pass
        else:
            tokens1.append(token)

    elif token in mysrc.identifiers():
        
        if is_function != -1:
            pass
        else:
            tokens1.append(token)

    elif token in mysrc.operators().keys():
        
        if is_function != -1:
            pass
        else:
            tokens1.append(token)
    
    elif re.search(headerPtrn, token):
        
        tokens1.append('head')

    elif token in func_tokens.keys() and token != 'main':
        tokens1.extend(add_func(token, func_tokens))
        

    elif token in class_list:
        tokens1.append('obj' )

    elif token == 'head':
        tokens1.append('he')

    elif token == 'num':
        tokens1.append('no')

    elif token == 'obj':
        tokens1.append('obj')

    elif re.match(varPtrn, token) or "'" in token or '"' in token:
        if is_function != -1:
            pass
        else:
            tokens1.append('v')
    elif re.match(digitPtrn, token):

        if is_function != -1:
            pass
        else:
            tokens1.append('num')

    return True

def funcCheck(token, func_tokens, func_list, class_list):
    global scope_depth, is_function
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
            if is_function != -1 and scope_depth == 0:
                is_function = -1
            
        else:
            pass
    elif token in mysrc.keywords():
        
        if is_function != -1:
            func_tokens[is_function].append(token)
        else:
            pass
    elif token in mysrc.identifiers():
        
        if is_function != -1:
            func_tokens[is_function].append(token)
        else:
            pass

    elif token in mysrc.operators().keys():
        
        if is_function != -1:
            func_tokens[is_function].append(token)
        else:
            pass
    elif token in func_list and token != is_function and is_function!= -1:
        func_tokens[is_function].append(token)

    elif token in class_list and is_function!= -1:
        func_tokens[is_function].append('obj' )

    elif re.search(headerPtrn, token):

        pass
    elif re.match(varPtrn, token) or "'" in token or '"' in token:

        if is_function != -1:
            func_tokens[is_function].append('v')
        else:
            pass
        

    elif re.match(digitPtrn, token):

        if is_function != -1:
            func_tokens[is_function].append('num')
            pass
        else:
            pass

    return True

def delimiterCorrection(line):

    for delim in mysrc.delimiters().keys():
        if delim in line:
            line = line.replace(delim, ' '+delim+' ') 
    
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


def remove_func_bodies(class_all_list, func_all_list):
    func_start = []
    func_list = []
    func_tokens = []
    class_tokens = {}
    f = open('work', 'r')
    txt = f.read()
    for func in func_all_list:
        pat = r"\s*"+str(func.name)+r"+\s*\("
        res = re.findall(pat, txt)
        if (len(res)>0):
            func_list.append(str(func.name))
            pat2 = r"\s*"+str(func.name)+r"+\s*\(([\w+\s+\w+])*\)\s*\{"
            pos = re.search(pat2, txt)
            if pos != None:
                line_no = len(re.findall('\n', txt[0:int(pos.start())]))
                func_start.append(line_no)

    class_list = []
    for class_ in reversed(class_all_list):
        pat = r"\s*"+str(class_.name)+r"+\s*\{"
        res = re.findall(pat, txt)
        if (len(res)>0):
            class_tokens[class_.name] = []
            for base in class_.bases:
                class_tokens[class_.name].extend(base.related_class.name.split())
                
            for derive in class_.derived:
                class_tokens[class_.name].extend(derive.related_class.name.spilt())

            for p in class_.constructors(allow_empty = True):
                if p is None:
                    break
                for a in p.argument_types:
                    class_tokens[class_.name].extend(str(a).split())
                
            for p in class_.operators(allow_empty = True):
                if p is not None:
                    p = re.sub(r'operator', r'ope', str(p.name))
                    class_tokens[class_.name].append(p)

            for p in class_.variables(allow_empty = True):
                class_tokens[class_.name].append(str(p.decl_type))

            for p in class_.member_functions(allow_empty = True):
                if p is None:
                    break
                for a in p.argument_types:
                    class_tokens[class_.name].append(str(a))

            class_list.append(str(class_.name))

    return func_list, func_start, class_list, class_tokens

def tokenize(path, tokens1, func_tokens, class_all_list, func_all_list):

    global is_function
    var_list = []
    try:
        file = open(path)
        f = file.read()
        

        lines = f.split("\n")
        file.close()

  
        # check if file exists 
        if os.path.exists("work"): 
            os.remove("work")
        file = open('work', 'a')

        for line in lines:
            line = line.strip()
            if line is not None and line is not '':
                file.write(line)
                file.write('\n')
        file.close()

        func_list, func_start, class_list, class_tokens = remove_func_bodies(class_all_list, func_all_list)

        count = -1
        for line in lines:
            line = line.strip()
            if line is not None and line is not '':
                count +=1
                if count in func_start:
                    
                    is_function = func_list[func_start.index(count)]
                    
                    func_tokens[is_function] = []
                tokens = delimiterCorrection(line)

                for token in tokens:
                    funcCheck(token, func_tokens, func_list, class_list)

        for token in func_tokens['main']:
            basicCheck(token, tokens1, func_tokens, class_list)

        for c in class_tokens.keys():
            for token in class_tokens[str(c)]:
                token = str(token)
                
                if (token[0:3] == 'ope'):
                    tokens1.append(token)
                else:
                    basicCheck(token, tokens1, func_tokens, class_list)

        return True
    except FileNotFoundError:
        print("\nInvald Path. Retry")
        run()

def run(path):

    decls = parser.parse([path], xml_generator_config)
    global_namespace = declarations.get_global_namespace(decls)
    std = global_namespace.namespace("std")

    func_all_list = []
    class_all_list = []

    for d in global_namespace.declarations:
        if isinstance(d, declarations.class_declaration_t):
            pass

        if isinstance(d, declarations.class_t) and d.parent == global_namespace:
            class_all_list.append(d)

        if isinstance(d, declarations.free_function_t):
            func_all_list.append(d)
    
    tokens1 = []
    tokens2 = []
    func_tokens = {}
    tokenize(path, tokens1, func_tokens, class_all_list, func_all_list)
    return tokens1, func_tokens


def tokenize_cpp(file):
    t1a, t1f = run(file)
    return ''.join(t1a)
