    # ------------------------------------------------------------
# lexer.py
#
# tokenizer para las expresiones soportadas por nuestro lenguaje
# ------------------------------------------------------------

import ply.lex as lex
import sys
import ast

# Lista para controlar errores
ListaTokensErrores = []

# Lectura del archivo de entrada
try:
    with open(sys.argv[1], 'r') as content_file:
        content = 	content_file.read()
    content_file.close()
except:
    print("Error al procesar el archivo de entrada")
    sys.exit()

# Lista del nombre de los tokens
tokens = ['TkNum', 'TkId', 'TkCaracter', 'TkComa', 'TkPunto', 'TkDosPuntos', 'TkParAbre', 'TkParCierra',
         'TkCorcheteAbre', 'TkCorcheteCierra', 'TkLlaveAbre', 'TkLlaveCierra', 'TkAsignacion', 'TkSuma', 
         'TkMult', 'TkResta', 'TkDiv', 'TkMod', 'TkConjuncion', 'TkDisyuncion', 'TkMenor', 'TkMenorIgual',
          'TkMayor', 'TkMayorIgual', 'TkIgual', 'TkSiguienteCar', 'TkAnteriorCar', 'TkValorAscii',
         'TkConcatenacion', 'TkShift', 'TkPuntoYComa', 'TkHacer']

# tokens y su respectiva palabra reservaEda
reserved = {
    'step' : 'TkStep',
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
    'true' : 'TkTrue',
    'false' : 'TkFalse',
    'not' : 'TkNegacion',
    'otherwise' : 'TkOtherwise'
}

# tokens de simbolos

t_TkComa = r'\,'
t_TkPunto = r'\.'
t_TkPuntoYComa = r'\;'
t_TkDosPuntos = r'\:'
t_TkParAbre = r'\('
t_TkParCierra = r'\)'
t_TkCorcheteAbre = r'\['
t_TkCorcheteCierra = r'\]'
t_TkLlaveAbre = r'\{'
t_TkLlaveCierra = r'\}'
t_TkAsignacion = r'\<\-'
t_TkHacer = r'\-\>'

# tokens de operadores aritmeticos

t_TkSuma = r'\+'
t_TkMult = r'\*'
t_TkResta = r'\-'
t_TkDiv = r'\/'
t_TkMod = r'\%'
t_TkConjuncion = r'\/\\'
t_TkDisyuncion = r'\\\/'
t_TkMenor = r'\<'
t_TkMenorIgual = r'\<\='
t_TkMayor = r'\>'
t_TkMayorIgual = r'\>\='
t_TkIgual = r'\='
t_TkSiguienteCar = r'\+\+'
t_TkAnteriorCar = r'\-\-'
t_TkValorAscii = r'\#'
t_TkConcatenacion = r'\:\:'
t_TkShift = r'\$'


tokens +=  list(reserved.values()) # Las palabras reservadas se agregan como tokens

# Expresiones regulares para la construccion de los tokens
def t_TkNum(t):
    r'\d+'
    t.value = int(t.value)    
    return t

# Regla para los caracteres
def t_TkCaracter(t):
    r'\'.\''
    t.value = eval(t.value)
    return t

# Regla para los identificadores
def t_ID(t):
    r'[a-zA-Z][a-zA-Z_0-9]*'
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
    ListaTokensErrores.append(t)
    print("Error: Caracter inesperado '%s' en la fila" % t.value[0], t.lineno,", columna", find_column(content, t))
    t.lexer.skip(1)


