import ply.yacc as yacc
import re
from ast import *
from lexer import *


# Símbolo inicial

def p_inicio(p):
	'''INICIO :  TkWith DEC TkBegin INSTR TkEnd
			| TkBegin INSTR TkEnd'''
	if (len(p) == 6):
		p[0] = InstrTree("Inicio", [p[4]], "program")
	else:
		p[0] = InstrTree("Inicio", [p[2]], "program") 

# Lista de Declaraciones

def p_dec(p):
	'''DEC : DEC TkVar IDENT TkDosPuntos TIPO
		| TkVar IDENT TkDosPuntos TIPO '''
	if (len(p) == 6):
		p[0] = InstrTree("Lista de Varias Declaraciones", [p[1], p[3], p[5]], p[2])
	else:
		p[0] = InstrTree("Lista de Declaraciones", [p[2], p[4]], p[1])

# Identificadores

def p_ident(p):
	'''IDENT : TkId
			| ASIG_ID
			| IDENT TkComa TkId
			| IDENT TkComa ASIG_ID'''
	if (len(p) == 4):
		p[0] = InstrTree("Identificadores", [p[1], p[3]], [p[2]])
	else:
		if(p[1] is not InstrTree):
			p[0] = InstrTree("Identificador", None , [p[1]])
		else:
			p[0] = InstrTree("Asignacion", [p[1]])


# Tipos de variables

def p_tipo(p):
	'''TIPO : TkInt
			| TkChar
			| TkBool
			| TkArray TkCorcheteAbre ARIT TkCorcheteCierra TkOf TIPO '''
	if (len(p) == 2):
		p[0] = InstrTree("Tipo", None, [p[1]])
	else:
		p[0] = InstrTree("Tipo Arreglo", [p[3], p[6]], ["declaracion de array"])

# Instrucciones

def p_instr(p):
	'''INSTR :  ASIG
			| I_O
			| COND
			| DETER
			| INDETER
			| INICIO
			| ASIG INSTR
			| I_O INSTR
			| INICIO INSTR
			| DETER INSTR
			| INDETER INSTR'''
	p[0] = InstrTree("Instruccion General", [p[1]])

# Asignacion 

def p_asig(p):
	'''ASIG : TkId TkAsignacion EXPR TkPuntoYComa'''
	p[0] = InstrTree("Asignacion", [p[1],p[3]], [p[2]])

# Asignacion como identificador

def p_asig_id(p):
	'''ASIG_ID : TkId TkAsignacion EXPR'''
	p[0] = InstrTree("Declaracion de Asignacion", [p[1], p[3]], [p[2]])

# Expresiones Aritmeticas

def p_arit(p):
	'''ARIT : TkNum
			| TkParAbre ARIT TkParCierra
			| ARIT TkSuma ARIT
			| ARIT TkResta ARIT
			| ARIT TkMult ARIT
			| ARIT TkDiv ARIT
			| ARIT TkMod ARIT
			| TkValorAscii TkCaracter'''
	if (len(p) == 2):
		if (p[1] == 'TkNum'):
			p[0] = InstrTree("Numero", None, [p[1]])
		else:
			p[0] = InstrTree("Identificador", None, [p[1]])
	elif (len(p) == 4):
		if ((p[1] == '(') and (p[3] == ')')):
			p[0] = InstrTree("Expresion Aritmetica", [p[2]], "Parentesis")
		else:
			p[0] = InstrTree("Expresion Aritmetica", [p[1], p[3]], [p[2]])
	else:
		p[0] = InstrTree("Expresion Aritmetica", [p[3]], [p[2]])

# Negacion Aritmetica

def p_nega(p):
	'''ARIT :	  TkResta ARIT %prec NEGA'''
	p[0] = InstrTree("Negacion Aritmetica", [p[2]], [p[1]])

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
			| TkId'''

	if (len(p) == 4):
		if ((p[1] == '(') and (p[3] == ')')):
			p[0] = InstrTree("Expresion Booleana", p[2], "Parentesis")
		else:
			p[0] = InstrTree("Expresion Booleana", [p[1], p[3]], [p[2]])
	elif (len(p) == 3):
		p[0] = InstrTree("Expresion Booleana", [p[2]], [p[1]])
	else:
		if (p[1] == 'TkId'):
			p[0] = InstrTree("Identificador", None, [p[1]])
		else:
			p[0] == InstrTree("Booleano", None, [p[1]])


# Expresiones con caracteres

def p_char(p):
	'''CHAR : TkCaracter
			| TkCaracter TkSiguienteCar
			| TkCaracter TkAnteriorCar'''
	if (len(p) == 2):
		if (p[1] == 'TkId'):
			p[0] = InstrTree("Identificador", None, [p[1]])
		else:
			p[0] = InstrTree("Caracter", None, [p[1]])
	else:
		p[0] = InstrTree("Expresion con Caracteres", [p[1]], [p[2]])


# Condicionales general

def p_cond(p):
	'''COND : 	  TkIf BOOL TkHacer INSTR COND0'''
	p[0] = InstrTree("Condicional General", [p[2], p[4], p[5]], [p[3]])

# Condicionales 

def p_cond0(p):
	'''COND0 :    TkOtherwise TkHacer INSTR
				| TkEnd'''
	if ( len(p) == 4):
		p[0] = InstrTree("Condicional", [p[3]], [p[2]])
	else:
		p[0] =  InstrTree("Condicional End", None, [p[1]])

# Iteracion indeterminada

def p_indeter(p):
	'''INDETER : TkWhile BOOL TkHacer INSTR TkEnd'''
	p[0] = InstrTree("Iteracion Indeterminada", [p[2], p[4]], [p[1]])

# Iteracion determinada general

def p_deter(p):
	'''DETER :   TkFor TkId TkFrom ARIT TkTo ARIT DETER0'''
	p[0] = InstrTree("Iteracion Determinada General", [p[4], p[6], p[7]], [p[1]])

# Iteracion determinada

def p_deter0(p):
	'''DETER0 :  TkStep ARIT TkHacer INSTR TkEnd
			| TkHacer INSTR TkEnd'''
	if (len(p) == 6):
		p[0] = InstrTree("Iteracion Determinada Step", [p[2], p[4]], [p[1]])
	else:
		p[0] = InstrTree("Iteracion Determinada", [p[2]], [p[1]])

# Entrada y salida

def p_i_o(p):
	'''I_O :  TkRead TkId TkPuntoYComa
			| TkPrint EXPR TkPuntoYComa'''
	p[0] = InstrTree("Entrada o Salida", None, [p[1]])

# Expresiones en general

def p_expr(p):
	'''EXPR : CHAR
			| ARIT
			| ARRAY
			| BOOL
			| TkId'''
	if (len(p) == 2):
		if (p[1] == 'TkId'):
			InstrTree("Identificador", None, [p[1]])
		else:
			p[0] = InstrTree("Expresion", [p[1]])
	else:
		p[0] = InstrTree("Indexacion", [p[3]], "Indexacion")

# Arreglos

def p_array(p):
	'''ARRAY : ARRAY TkConcatenacion ARRAY
			 | TkShift ARRAY
			 | TkId TkCorcheteAbre ARIT TkCorcheteCierra'''
	if (len(p) == 4):
		p[0] = InstrTree("Arreglo", [p[1], p[3]],[p[2]])
	elif ( len(p) == 3) :
		p[0] = InstrTree("Shift", [p[1]], [p[2]])
	else:
		p[0] = InstrTree("Identificador", None, [p[1]])

# Detección de errores
def p_error(p):
    if (not p):
        return
    print("Error de sintaxis en la entrada.\nError: '" + str(p.value) +\
     "' ubicado en la fila {:d}, columna {:d}.".format(p.lineno,\
      find_column(content, p)))
    sys.exit()

precedence = (
	('nonassoc', 'TkMenor', 'TkMayor'),
	('nonassoc', 'TkMenorIgual', 'TkMayorIgual'),
	('left', 'NEGA', 'TkMult', 'TkDiv', 'TkMod', 'TkSuma', 'TkResta'),
	('left', 'TkNegacion', 'TkConjuncion', 'TkDisyuncion'),
	('left', 'TkValorAscii', 'TkAnteriorCar', 'TkSiguienteCar'),
	('left', 'TkCorcheteAbre', 'TkShift', 'TkConcatenacion')
	)