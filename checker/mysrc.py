def keywords():
    keywords = [
    "auto", "break", "case", "catch", "word", "class", "const", "continue", "delete", "do", "else", "false", "for", "goto", "if", "#include", 
    "namespace", "not", "or", "private", "protected", "public", "return", "signed", "sizeof", "static", "switch", "true", "try", "unsigned", "void", "while",
    "endl", "cout", "cin", "main"
    ]
    #print(len(keywords)) = 36
    return keywords

def identifiers():
    identifiers = [
    "bool", "char", "double", "enum", "float", "int", "long", "short", "struct", "string" ]
    #print(len(identifiers)) = 10
    return identifiers

def operators():
    operators = {
    "+": "PLUS", "-": "MINUS", "*": "MUL", "/": "DIV", "%": "MOD", "+=": "PLUSEQ", "-=": "MINUSEQ", "*=": "MULEQ", "/=": "DIVEQ", "++": "INC", "--": "DEC", "|": "OR", "&&": "AND",
    }
    #print(len(operators)) = 13
    return operators

def delimiters():
    delimiters = {
    "\t": "TAB", "\n": "NEWLINE","(": "LPAR", ")": "RPAR", "[": "LBRACE", "]": "RBRACE", "{": "LCBRACE", "}": "RCBRACE", "=": "ASSIGN",":": "COLON", ",": "COMMA", ";": "SEMICOL", "<<": "OUT", ">>": "IN",
    }
    #print(len(delimiters)) = 14
    return delimiters

#keywords()
#operators()
#delimiters()