import pygments.token
import pygments.lexers
import os, re

#Python module pygments is used to tokenize_py the code files. This module supports most of the popular languages
#http://pygments.org/languages/
#Hence this program can be used to clean up codes written in most languages


def tokenize_jav(filename):
    file = open(filename, "r")
    if os.path.exists("work"): 
        os.remove("work")
    work = open('work', 'a')
    func_text = {}
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
    file = open('work', 'r')
    text = file.read()

    lexer = pygments.lexers.guess_lexer_for_filename(filename, text)
    tokens = lexer.get_tokens(text)
    tokens = list(tokens)
    func_list = []
    lenT = len(tokens)
    tokens1 = []
    class_list = []

    scope_depth = 0

    key_names = {'String' : 'str', 'ArrayList' : 'array', 'List': 'list', 'LinkedList': 'linked', 'HashMap': 'hashma', 'HashSet':' hashse', 'BufferedReader': 'buffer', 
    'ArithmeticException' : 'arithmex', 'ArrayIndexOutOfBoundsException' : 'arrinoex', 'Iterator': 'iterat', 'Pattern': 'pater', 'Matcher': 'match', 'PatternSyntaxException': 'patsynex',
    'ClassNotFoundException': 'clasnoex', 'FileNotFoundException': 'filenoex', 'IOException': 'inpoutex', 'InterruptedException': 'intexex', 'NoSuchFieldException': 'nofileex', 
    'NoSuchMethodException': 'nomethex', 'NullPointerException': 'nulponex', 'NumberFormatException': 'numforex', 'RuntimeException': 'runtimex', 
    'StringIndexOutOfBoundsException': 'strioex', 'LocalDate': 'locdat', 'LocalTime': 'loctim', 'LocalDateTime': 'dattim', 'DateTimeFormatter': 'dtform',
    'Thread': 'thread', 'Main': 'main', 'Runnable': 'runble', 'Consumer': 'consum', 'private': 'scp', 'public': 'scp', 'protected': 'scp',
    'FileReader': 'filred', 'FileInputStream': 'fileinpstr', 'FileWriter': 'filewrit', 'BufferedWriter': 'bufwrit', 'FileOutputStream': 'filoutstr'}

    file_methods = ['File', 'canRead', 'canWrite', 'createNewFile', 'delete', 'exists', 'getName', 'length', 'list', 'mkdir', 'getAbsolutePath', 'FileWriter', 'write', 'close']
    

    string_methods = ['charAt', 'codePointAt', 'codePointBefore', 'codePointCount', 'compareTo', 'compareToIgnoreCase', 'concat', 'contains', 'contentEquals', 'copyValueOf', 'endsWith', 'equals',
        'equalsIgnoreCase', 'format', 'getBytes', 'getChars', 'hashCode', 'indexOf', 'intern', 'isEmpty', 'lastIndexOf', 'length', 'matches', 'offsetByCodePoints', 'regionMatches', 'replace', 'replaceFirst',
        'substring', 'toCharArray', 'toLowerCase', 'toString', 'toUpperCase', 'trim', 'valueOf']
    

    math_methods = ['abs', 'acos', 'asin', 'atan', 'atan2', 'cbrt', 'ceil', 'copySign', 'cos', 'cosh', 'exp', 'expm1', 'floor', 'getExponent', 'hypot', 'log', 'log10', 'log1p', 'max', 
    'min', 'nextAfter', 'nextUp', 'pow', 'random', 'round', 'rint', 'signum', 'sin', 'sinh', 'sqrt', 'tan', 'tanh', 'toDegrees', 'toRadians', 'ulp']

    some_keys = ['abstract', 'implements', 'enum', 'interface', 'final', 'extends', 'forEach']

    for i in range(lenT):
        if tokens[i][0] == pygments.token.Name.Function:
            func_list.append('function')

        elif tokens[i][0] == pygments.token.Name.Class:
            class_list.append(str(tokens[i][1]))


    for i in range(lenT):
        if tokens[i][0] in pygments.token.Punctuation :
            if str(tokens[i][1]) == '{':
                scope_depth+=1
            elif str(tokens[i][1]) == '}':
                scope_depth-=1
            else:
                pass
        
        elif tokens[i][0] in func_list or tokens[i][0] == pygments.token.Name.Function:
            tokens1.append('function')

        elif tokens[i][0] in class_list or tokens[i][0] == pygments.token.Name.Class:
            tokens1.append('class')


        elif (tokens[i][0] == pygments.token.Name or tokens[i][0] in pygments.token.Name) and not i == lenT - 1 and not tokens[i + 1][1] == '(':

            t = str(tokens[i][1])

            if tokens[i][0] == pygments.token.Name.Class:
                tokens1.append('class')

            elif str(tokens[i][1]) in class_list:
                tokens1.append('obj')

            elif tokens[i][0] in pygments.token.Name.Namespace:
                toks = t.split('.')[-1]
                if toks in key_names.keys():
                    tokens1.append(key_names[toks])

            elif tokens[i][0] in pygments.token.Name.Builtin or tokens[i][0] in pygments.token.Name.Decorator :
                tokens1.append(t)

            elif tokens[i][0] in pygments.token.Name.Attribute:
                tokens1.append('fun')

            else:
                if t in key_names.keys():
                    tokens1.append(key_names[t])
                elif t in some_keys:
                    tokens1.append(t)
                elif t in file_methods:
                    tokens1.append(t)
                elif t in string_methods:
                    tokens1.append(t)
                elif t in math_methods:
                    tokens1.append(t)
                else:
                    tokens1.append('var')

        elif tokens[i][0] == pygments.token.Name.Class:
            tokens1.append('class')

        elif tokens[i][0] == pygments.token.Name or tokens[i][0] in pygments.token.Name:
            tokens1.append('var')

        elif tokens[i][0] in pygments.token.Literal.String:
            pass

        elif tokens[i][0] == pygments.token.Text or tokens[i][0] in pygments.token.Comment:
            pass   #whitespaces and comments ignored

        elif str(tokens[i][1]) == 'import':
            pass
        else:
            t = str(tokens[i][1])
            if t in key_names.keys():
                tokens1.append(key_names[t])
            else:
                tokens1.append(t)

    if os.path.exists("work"):
        os.remove("work")
    return ''.join(tokens1)

