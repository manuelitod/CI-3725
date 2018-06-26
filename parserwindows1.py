 # ------------------------------------------------------------
# lexer.py
#
# tokenizer para las expresiones soportadas por nuestro lenguaje
# ------------------------------------------------------------

import ply.lex as lex
import ply.yacc as yacc
import sys


class InstrTree:
	def __init__(self, stamp, children = None, parent = None, tipo = None):
		self.stamp = stamp
		if children:
			self.children = children
		else:
			self.children = [ ]
		self.parent = parent
		self.tipo = tipo
	
	def print_tree(self, level = 0):
		if self.parent != None: 
			print ('\t' * level + str(self.parent))
		if self.children != None:
			for children in self.children:
				if children.parent != None: children.print_tree(level+1)
				else:
					children.print_tree(level)

# Lista para controlar errores
ListaTokensErrores = []
j = 0

# Lectura del archivo de entrada
try:
	with open(sys.argv[1], 'r') as content_file:
		content =   content_file.read()
	content_file.close()
except:
	print("Error al procesar el archivo de entrada")
	sys.exit()

# Lista del nombre de los tokens
tokens = ['TkNum', 'TkId', 'TkCaracter', 'TkComa', 'TkPunto', 'TkDosPuntos', 'TkParAbre', 'TkParCierra',
		 'TkCorcheteAbre', 'TkCorcheteCierra', 'TkLlaveAbre', 'TkLlaveCierra', 'TkAsignacion', 'TkSuma', 
		 'TkMult', 'TkResta', 'TkDiv', 'TkMod', 'TkConjuncion', 'TkDisyuncion', 'TkMenor', 'TkMenorIgual',
		  'TkMayor', 'TkMayorIgual', 'TkIgual', 'TkSiguienteCar', 'TkAnteriorCar', 'TkValorAscii',
		 'TkConcatenacion', 'TkShift', 'TkPuntoYComa', 'TkHacer', 'TkDesigual']

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
t_TkDesigual = r'\/\='
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
	if t.type == "TkTrue":
		t.value = True
	elif t.type == "TkFalse":
		t.value = False
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
	t.lex
import ply.yacc as yacc
import re
from lexer import *

variables =[]
dic = {}
total_variables = []
k = 0

# Simbolo inicial

def p_inicio(p):
	'''INICIO :  TkWith DEC TkBegin INSTR TkEnd
			| TkBegin INSTR TkEnd'''
	global dic
	global variables
	global total_variables
	global k
	if (len(p) == 4):
		p[0] = InstrTree("Inicio", [p[2]], "begin") 
	else:
		var = InstrTree("", [p[2]], "with")
		instr = InstrTree("", [p[4]], "begin")
		p[0] = InstrTree("Inicio", [var, instr], None, "inicio")
#		global j 
#		print(str(j) + " este es el diccionario " + str(total_variables[j]))
#		k =  k + 1

# Lista de Declaraciones

def p_dec(p):
	'''DEC : DEC1 TkVar DEC0
		| TkVar IDENT TkDosPuntos TIPO '''
	global variables
	global dic
	global k
	if (len(p) == 4):
		p[0] = InstrTree("Lista de Varias Declaraciones", [p[1], p[3]], None)
	else:
		p[0] = InstrTree("Lista de Declaraciones", [p[2], p[4]], p[1], str(k))
		for i in variables:
			dic.update({i:p[4].tipo})
		total_variables.append([dic, k])
		dic = {}
		variables = []
	k =  k + 1

# Lista de Declaraciones 1

def p_dec1(p):
	'''DEC1 : DEC1 TkVar DEC0
		| TkVar IDENT TkDosPuntos TIPO '''
	global variables
	global dic
	global k
	if (len(p) == 4):
		p[0] = InstrTree("Lista de Varias Declaraciones", [p[1], p[3]], None)
	else:
		p[0] = InstrTree("Lista de Declaraciones", [p[2], p[4]], p[1], str(k))
		for i in variables:
			dic.update({i:p[4].tipo})
		total_variables.append([dic, k])
		dic = {}
		variables = []
# Lista de varias declaraciones

def p_dec0(p):
	'''DEC0 : IDENT TkDosPuntos TIPO'''
	p[0] = InstrTree("Varias declaraciones", [p[1], p[3]], "var")
	global variables
	global dic
	global k
	for i in variables:
		if (p[3].tipo == "array de Caracter"):
			dic.update({i:'Caracter'})
		elif (p[3].tipo == "array de Entero"):
			dic.update({i:'Entero'})
		elif (p[3].tipo == "array de Booleano"):
			dic.update({i:'Booleano'})
		else:
			dic.update({i:p[3].tipo})
		total_variables.append([dic, k])
		dic = {}
		variables = []

# Identificadores

def p_ident(p):
	'''IDENT : TkId
			| ASIG_ID
			| IDENT TkComa TkId
			| IDENT TkComa ASIG_ID'''
	global variables
	if (len(p) == 4):
		if not(type(p[3]) is str):
			p[0] = InstrTree("Identificadores", [p[1], p[3]], None)
		else:
			variables.append(p[3]) 
			p[0] = InstrTree("Identificadores", [p[1], InstrTree("Identificador", None, p[3])], None)
	else:
		if (p[1] is not str):
			p[0] = InstrTree("Identificador", None, p[1])
			variables.append(p[1])
		else:
			p[0] = InstrTree("Asignacion", [p[1]], None)	


# Tipos de variables

def p_tipo(p):
	'''TIPO : TkInt
			| TkChar
			| TkBool
			| TkArray TkCorcheteAbre EXPR TkCorcheteCierra TkOf TIPO '''
	if (len(p) == 2):
		tipo =  InstrTree("", None, p[1])
		if (p[1] == "int"):
			p[0] = InstrTree("Tipo", [tipo], "tipo", "Entero")
		elif (p[1] == "char"):
			p[0] = InstrTree("Tipo", [tipo], "tipo", "Caracter")
		else:
			p[0] = InstrTree("Tipo", [tipo], "tipo", "Booleano")
	else:
		p[0] = InstrTree("Tipo Arreglo", [InstrTree("", [p[3]], "array"), p[6]], "tipo", "array de " + p[6].tipo)

# Instrucciones

def p_instr(p):
	'''INSTR :  ASIG
			| I_O
			| COND
			| DETER
			| INDETER
			| INICIO
			| PUNTO
			| ASIG INSTR
			| I_O INSTR
			| INICIO INSTR
			| DETER INSTR
			| INDETER INSTR
			| COND INSTR
			| PUNTO INSTR'''
	if len(p) == 2:
		p[0] = InstrTree("Instruccion General", [p[1]])
	else:
		p[0] = InstrTree("Instruccion General", [p[1], p[2]])

# Punto

def p_punto(p):
	'''PUNTO : TkId TkPunto EXPR'''
	p[0] = InstrTree("Punto", [InstrTree("", None, p[1]),p[3]], p[2])

# Asignacion 

def p_asig(p):
	'''ASIG : TkId TkAsignacion EXPR TkPuntoYComa'''
	p[0] = InstrTree("Asignacion", [InstrTree("Id", None, p[1]),p[3]], p[2])

# Asignacion como identificador

def p_asig_id(p):
	'''ASIG_ID : TkId TkAsignacion EXPR'''
	global variables
	p[0] = InstrTree("Declaracion de Asignacion", [InstrTree("Id", None, p[1]), p[3]], p[2])
	variables.append(p[1])

# Negacion Aritmetica

def p_nega(p):
	'''EXPR :     TkResta EXPR %prec NEGA'''
	p[0] = InstrTree("Negacion Aritmetica", [p[2]], p[1])


# Condicionales general

def p_cond(p):
	'''COND :  TkIf EXPR TkHacer INSTR TkEnd
			|  TkIf EXPR TkHacer INSTR TkOtherwise TkHacer INSTR TkEnd'''
	
	if len(p) == 6:
		p[0] = InstrTree("Condicional", 
		[InstrTree("", [p[2]], "condicion"),
		InstrTree("", [p[4]], "exito")], 
		"if")
	else:
		p[0] = InstrTree("Condicional and otherwise", 
		[InstrTree("", [p[2]], "condicion"),
		InstrTree("", [p[4]], "exito"),
		InstrTree("", [p[7]], "fracaso")], 
		"ifot")


# Iteracion indeterminada

def p_indeter(p):
	'''INDETER : TkWhile EXPR TkHacer INSTR TkEnd'''
	cond = InstrTree("", [p[2]], "condicion")
	instr = InstrTree("", [p[4]], "instruccion")
	p[0] = InstrTree("Iteracion Indeterminada", [cond, instr], p[1])

# Iteracion determinada general

def p_deter(p):
	'''DETER :   TkFor TkId TkFrom EXPR TkTo EXPR DETER0'''
	id = InstrTree("Identificador", None, p[2])
	p[0] = InstrTree("Iteracion Determinada General", [InstrTree("",[id],"variable"), 
	InstrTree("", [p[4]], "inicio"), 
	InstrTree("", [p[6]], "final"), p[7]], p[1])

# Iteracion determinada

def p_deter0(p):
	'''DETER0 :  TkStep EXPR TkHacer INSTR TkEnd
			| TkHacer INSTR TkEnd'''
	if (len(p) == 6):
		step = InstrTree("", [p[2]], "step")
		instr = InstrTree("", [p[4]], "instruccion")
		p[0] = InstrTree("Iteracion Determinada Step", [step, instr], None)
	else:
		instr = InstrTree("", [p[2]], None)
		p[0] = InstrTree("Iteracion Determinada", [instr], "instruccion")

# Entrada y salida

def p_i_o(p):
	'''I_O :  TkRead TkId TkPuntoYComa
			| TkPrint EXPR TkPuntoYComa'''
	if type(p[2]) is InstrTree:
		p[0] = InstrTree("Entrada o Salida", [p[2]], p[1])
	else:
		p[0] = InstrTree("Entrada o Salida", [InstrTree("Identificador", None, p[2])], p[1])

# Expresiones en general

def p_expr(p):
	'''EXPR : TkCaracter
			| TkCaracter TkSiguienteCar
			| TkCaracter TkAnteriorCar
			| TkNum
			| TkParAbre EXPR TkParCierra
			| EXPR TkSuma EXPR
			| EXPR TkResta EXPR
			| EXPR TkMult EXPR
			| EXPR TkDiv EXPR
			| EXPR TkMod EXPR
			| TkValorAscii TkCaracter
			| EXPR TkConcatenacion EXPR
			| TkShift EXPR
			| EXPR TkCorcheteAbre EXPR TkCorcheteCierra
			| EXPR TkConjuncion EXPR
			| EXPR TkDisyuncion EXPR
			| EXPR TkMenor EXPR
			| EXPR TkMenorIgual EXPR
			| EXPR TkMayor EXPR
			| EXPR TkMayorIgual EXPR
			| EXPR TkIgual EXPR
			| EXPR TkDesigual EXPR
			| TkFalse
			| TkTrue
			| TkNegacion EXPR
			| TkId'''
	if (len(p) == 2):
		if (p[1] == 'TkId'):
			p[0] = InstrTree("Identificador", None, p[1])
		elif (p[1] == 'TkNum'):
			p[0] = InstrTree("Numero", None, p[1])
		elif (p[1] == 'TkCaracter'):
			p[0] = InstrTree("Caracter", None, p[1])
		elif (p[1] == 'TkTrue'):
			p[0] = InstrTree("True", None, p[1])
		else:
			p[0] = InstrTree("False", None, p[1])
	elif (len(p) == 3):
		if (p[1] == "TkCaracter"):
			p[0] = InstrTree("Expresion con Caracteres", [p[1]], p[2])
		elif (p[1] == "TkValorAscii"):
			p[0] = InstrTree("Valor Ascii", [p[3]], p[2])
		elif (p[1] == "TkShift"):
			p[0] = InstrTree("Shift", [p[2]], p[1])
		else:
			p[0] = InstrTree("Negacion", [p[2]], p[1])
	elif (len(p) == 4):
		if (p[1] == "("):
			p[0] = InstrTree("Expresion", [p[2]], "()")
		else:
			p[0] = InstrTree("Operacion Binaria", [p[1], p[3]], p[2])
	else:
		p[0] = InstrTree("Indexacion", [p[1], p[3]], "[]")


# Deteccion de errores
def p_error(p):
	if (not p):
		print("Error de sintaxis")
		return
	print("Error de sintaxis en la entrada.\nError: '" + str(p.value) +\
	 "' ubicado en la fila {:d}, columna {:d}.".format(p.lineno,\
	  find_column(content, p)))
	sys.exit()

precedence = (
	('left', 'TkMayor', 'TkMenor', 'TkMayorIgual', 'TkMenorIgual', 'TkIgual', 'TkDesigual'),
	('left', 'TkSuma', 'TkResta'),
	('left', 'TkMult', 'TkDiv', 'TkMod'),
	('left', 'TkConjuncion', 'TkDisyuncion'),
	('left', 'TkNegacion', 'NEGA'),
	('left', 'TkConcatenacion'),
	('left', 'TkShift'),
	('left', 'TkCorcheteAbre')
)

# Inicializacion del lexer
lexer = lex.lex()
lexer.input(content)
lexer.lineno = 1
parser = yacc.yacc()
tree = parser.parse(content)
if tree != None:
	print("---AST---")
	tree.print_tree()
print("La longitud de total_variables es: " + str(len(total_variables)))
for i in total_variables:
	print("La longitud de dict es: " + str(len(i)))

print(total_variables)
