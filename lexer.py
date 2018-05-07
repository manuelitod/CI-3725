# ------------------------------------------------------------
# lexer.py
#
# tokenizer para las expresiones soportadas por nuestro lenguaje
# ------------------------------------------------------------

import ply.lex as lex
import sys
import ast

# Lectura del archivo de entrada
with open(sys.argv[1], 'r') as content_file:
	content = 	content_file.read()
content_file.close()

# Lista del nombre de los tokens
tokens = ['TkNum', 'TkId', 'TkCaracter']

# tokens y su respectiva palabra reservada
reserved = {
    'begin': 'TkBegin',
    'with' : 'TkWith',
    'end' : 'TkEnd',
    'var' : 'TkVar', 
    'int' : 'TkInt',
    'bool' : 'TkBool',
    'char' : 'TkChar',
    'array' : 'TkArray',
    'of' : 'TkOf',
    'print' : 'TkPrint',
    'read' : 'TkRead',
    'for' : 'TkFor',
    'from' : 'TkFrom',
    'to' : 'TkTo',
    'if' : 'TkIf',
    'while' : 'TkWhile',
    'True' : 'TkTrue',
    'False' : 'TkFalse'
}

tokens +=  list(reserved.values())

# Expresiones regulares para la construccion de los tokens
def t_TkNum(t):
    r'\d+'
    t.value = int(t.value)    
    return t

def t_TkCaracter(t):
    r'\'.\''
    t.value = eval(t.value)
    return t

def t_ID(t):
    r'[a-zA-Z_][a-zA-Z_0-9]*'
    t.type = reserved.get(t.value,'TkId')    # Checkeo para palabras reservadas
    if t.type == "TkTrue" or t.type == "TkFalse":
        t.value = ast.literal_eval(t.value)
        return t
    else:
        return t

# Regla para detectar saltos de lineas
def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)

# Lista de caracteres ignorados
t_ignore = ' \t'

# Identificar columna del token
def find_column(input, token):
    line_start = input.rfind('\n', 0, token.lexpos) + 1
    return (token.lexpos - line_start) + 1


# Regla para manejar error
def t_error(t):
    print("Error: Caracter inesperado '%s' en la fila " % t.value[0], t.lineno,",columna", find_column(content, t))
    t.lexer.skip(1)

# Se construye el lexer
lexer = lex.lex()


