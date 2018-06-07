# --------------------

#Integrantes: 
#Manuel Rodriguez 13-11223
#Ian Goldberg 14-10406

# ---------------------

import ply.yacc as yacc
import re
from ast import *
from lexer import *


# Símbolo inicial

def p_inicio(p):
	'''INICIO :  TkWith DEC TkBegin INSTR TkEnd
			| TkBegin INSTR TkEnd'''
	if (len(p) == 6):
		var = InstrTree("", [p[2]], "with")
		instr = InstrTree("", [p[4]], "begin")
		p[0] = InstrTree("Inicio", [var, instr], None)
	else:
		p[0] = InstrTree("Inicio", [p[2]], "begin") 

# Lista de Declaraciones

def p_dec(p):
	'''DEC : DEC TkVar DEC0
		| TkVar IDENT TkDosPuntos TIPO '''
	if (len(p) == 4):
		p[0] = InstrTree("Lista de Varias Declaraciones", [p[1], p[3]], None)
	else:
		p[0] = InstrTree("Lista de Declaraciones", [p[2], p[4]], p[1])

# Lista de varias declaraciones

def p_dec0(p):
	'''DEC0 : IDENT TkDosPuntos TIPO'''
	p[0] = InstrTree("Varias declaraciones", [p[1], p[3]], "var")

# Identificadores

def p_ident(p):
	'''IDENT : TkId
			| ASIG_ID
			| IDENT TkComa TkId
			| IDENT TkComa ASIG_ID'''
	if (len(p) == 4):
		if (type(p[3]) is InstrTree):
			p[0] = InstrTree("Identificadores", [p[1], p[3]], None)
		else:
			p[0] = InstrTree("Identificadores", [p[1], 
		InstrTree("Identificador", None, p[3])], None)
	else:
		if(type(p[1]) is not InstrTree):
			p[0] = InstrTree("Identificador", None, p[1])
		else:
			p[0] = InstrTree("Asignacion", [p[1]], None)


# Tipos de variables

def p_tipo(p):
	'''TIPO : TkInt
			| TkChar
			| TkBool
			| TkArray TkCorcheteAbre ARIT TkCorcheteCierra TkOf TIPO '''
	if (len(p) == 2):
		tipo = 	InstrTree("", None, p[1])
		p[0] = InstrTree("Tipo", [tipo], "tipo")
	else:
		p[0] = InstrTree("Tipo Arreglo", [InstrTree("",[p[3]], "size"), p[6]], "array")

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
	'''PUNTO : TkId TkPunto ARIT'''
	p[0] = InstrTree("Punto", [InstrTree("", None, p[1]),p[3]], p[2])

# Asignacion 

def p_asig(p):
	'''ASIG : TkId TkAsignacion EXPR TkPuntoYComa'''
	p[0] = InstrTree("Asignacion", [InstrTree("Id", None, p[1]),p[3]], p[2])

# Asignacion como identificador

def p_asig_id(p):
	'''ASIG_ID : TkId TkAsignacion EXPR'''
	p[0] = InstrTree("Declaracion de Asignacion", [InstrTree("Id", None, p[1]), p[3]], p[2])

# Expresiones Aritmeticas

def p_arit(p):
	'''ARIT : TkNum
			| TkParAbre ARIT TkParCierra
			| ARIT TkSuma ARIT
			| ARIT TkResta ARIT
			| ARIT TkMult ARIT
			| ARIT TkDiv ARIT
			| ARIT TkMod ARIT
			| TkValorAscii TkCaracter
			| TkId
			| ARRAY TkCorcheteAbre ARIT TkCorcheteCierra'''
	if (len(p) == 2):
		if (type(p[1]) is int):
			p[0] = InstrTree("Numero", None, p[1])
		else:
			p[0] = InstrTree("Identificador", None, p[1])
	elif (len(p) == 4):
		if ((p[1] == '(') and (p[3] == ')')):
			p[0] = InstrTree("Expresion Aritmetica", [p[2]], "()")
		else:
			p[0] = InstrTree("Expresion Aritmetica", [p[1], p[3]], p[2])
	elif (len(p) == 5):
		p[0] = InstrTree("Indexacion", [p[1], p[3]], "[]")
	else:
		p[0] = InstrTree("Expresion Aritmetica", [p[3]], p[2])

# Negacion Aritmetica

def p_nega(p):
	'''ARIT :	  TkResta ARIT %prec NEGA'''
	p[0] = InstrTree("Negacion Aritmetica", [p[2]], p[1])

# Expresiones Booleanas

def p_bool(p):
	'''BOOL : BOOL TkConjuncion BOOL
			| BOOL TkDisyuncion BOOL
			| ARIT TkMenor ARIT
			| ARIT TkMenorIgual ARIT
			| ARIT TkMayor ARIT
			| ARIT TkMayorIgual ARIT
			| ARIT TkIgual ARIT
			| ARIT TkDesigual ARIT
			| TkParAbre BOOL TkParCierra
			| TkFalse
			| TkTrue
			| TkNegacion BOOL
			| TkId
			| ARRAY TkCorcheteAbre ARIT TkCorcheteCierra'''

	if (len(p) == 4):
		if ((p[1] == '(') and (p[3] == ')')):
			p[0] = InstrTree("Expresion Booleana", [p[2]], "()")
		else:
			p[0] = InstrTree("Expresion Booleana", [p[1], p[3]], p[2])
	elif (len(p) == 3):
		p[0] = InstrTree("Expresion Booleana", [p[2]], p[1])
	elif (len(p) == 5):
		p[0] = InstrTree("Indexacion", [p[1], p[3]], "[]")
	else:
		p[0] = InstrTree("Condicion simple", None, p[1])


# Expresiones con caracteres

def p_char(p):
	'''CHAR : TkCaracter
			| CHAR TkSiguienteCar
			| CHAR TkAnteriorCar
			| TkId
			| ARRAY TkCorcheteAbre ARIT TkCorcheteCierra'''
	if (len(p) == 2):
		p[0] = InstrTree("Caracter", None, p[1])
	elif (len(p) == 5):
		p[0] = InstrTree("Indexacion", [p[1], p[3]], "[]")
	else:
		p[0] = InstrTree("Expresion con Caracteres", [p[1]], p[2])


# Condicionales general

def p_cond(p):
	'''COND :  TkIf BOOL TkHacer INSTR TkEnd
			|  TkIf BOOL TkHacer INSTR TkOtherwise TkHacer INSTR TkEnd'''
	
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
	'''INDETER : TkWhile BOOL TkHacer INSTR TkEnd'''
	cond = InstrTree("", [p[2]], "condicion")
	instr = InstrTree("", [p[4]], "instruccion")
	p[0] = InstrTree("Iteracion Indeterminada", [cond, instr], p[1])

# Iteracion determinada general

def p_deter(p):
	'''DETER :   TkFor TkId TkFrom ARIT TkTo ARIT DETER0'''
	id = InstrTree("Identificador", None, p[2])
	p[0] = InstrTree("Iteracion Determinada General", [InstrTree("",[id],"variable"), 
	InstrTree("", [p[4]], "inicio"), 
	InstrTree("", [p[6]], "final"), p[7]], p[1])

# Iteracion determinada

def p_deter0(p):
	'''DETER0 :  TkStep ARIT TkHacer INSTR TkEnd
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
	'''EXPR : CHAR
			| ARIT
			| ARRAY
			| BOOL
			| TkId'''
	if (len(p) == 2):
		if (type(p[1]) is not InstrTree):
			p[0] = InstrTree("Identificador", None, p[1])
		else:
			p[0] = InstrTree("Expresion", [p[1]])
	else:
		p[0] = InstrTree("Indexacion", [p[3]], "Indexacion")

# Arreglos

def p_array(p):
	'''ARRAY : ARRAY TkConcatenacion ARRAY
			 | TkShift ARRAY
			 | ARRAY TkCorcheteAbre ARIT TkCorcheteCierra
			 | TkId
			 | TkParAbre ARRAY TkParCierra'''
	if (len(p) == 4):
		if ((p[1] == '(') and (p[3] == ')')):
			p[0] = InstrTree("Expresion array", [p[2]], "()")
		else:
			p[0] = InstrTree("Concatenacion array", [p[1], p[3]], p[2])
	elif ( len(p) == 3 ) :
		p[0] = InstrTree("Shift", [p[2]], p[1])
	elif ( len(p) == 5 ):
		p[0] = InstrTree("Indexacion", [p[1], p[3]], "[]")
	else:
		p[0] = InstrTree("Identificador", None, p[1])

# Detección de errores
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