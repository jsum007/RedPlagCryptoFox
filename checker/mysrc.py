def keywords():
    keywords = [
    "auto", "bool", "break", "case", "catch", "char", "word", "class", "const", "continue", "delete", "do", "double", "else", "enum", "false", "float", "for", "goto", "if", "#include", 
    "int", "long", "namespace", "not", "or", "private", "protected", "public", "return", "short", "signed", "sizeof", "static", "struct", "switch", "true", "try", "unsigned", "void", "while",
    "endl", "cout", "cin", "main"
    ]
    #print(len(keywords)) = 45
    return keywords

def operators():
    operators = {
    "+": "PLUS", "-": "MINUS", "*": "MUL", "/": "DIV", "%": "MOD", "+=": "PLUSEQ", "-=": "MINUSEQ", "*=": "MULEQ", "/=": "DIVEQ", "++": "INC", "--": "DEC", "|": "OR", "&&": "AND",
    }
    #print(len(operators)) = 13
    return operators

def delimiters():
    delimiters = {
    "\t": "TAB", "\n": "NEWLINE","(": "LPAR", ")": "RPAR", "[": "LBRACE", "]": "RBRACE", "{": "LCBRACE", "}": "RCBRACE", "=": "ASSIGN",":": "COLON", ",": "COMMA", ";": "SEMICOL", "<<": "OUT", ">>": "IN", ".": "PERIOD",
    }
    #print(len(delimiters)) = 14
    return delimiters

#keywords()
#operators()
#delimiters()
