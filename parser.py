import ply.yacc as yacc
import re
from ast import *
from lexer import *

global Tree


# Símbolo inicial

def p_inicio(p):
	'''INICIO :  TkWith DEC TkBegin INSTR TkEnd
			| TkBegin INSTR TkEnd'''
	if (len(p) == 6):
		p[0] = InstrTree("Inicio", p[2], p[4])
	else:
		p[0] = InstrTree("Inicio", p[2])



# Lista de Declaraciones

def p_dec(p):
	'''DEC : DEC TkVar IDENT TkDosPuntos TIPO
		| TkVar IDENT TkDosPuntos TIPO
		| TkVar '''
	if (len(p) == 6):
		p[0] = InstrTree("Lista de Declaraciones", [p[1], p[3], p[5]])
	else:
		p[0] = InstrTree("Lista de Declaraciones", [p[2], p[4]])

# Identificadores

def p_ident(p):
	'''IDENT : TkId
			| ASIG
			| IDENT TkComa IDENT'''
	if (len(p) == 4):
		p[0] = InstrTree("Identificador", p[2])
	else:
		p[0] = InstrTree("Identificador", p[1])


# Tipos de variables

def p_tipo(p):
	'''TIPO :    TkInt
			| TkChar
			| TkBool
			| TkArray TkCorcheteAbre ARIT TkCorcheteCierra TkOf TIPO '''
	p[0] = InstrTree("Tipo", p[1])

# Instrucciones generales

def p_instr(p):
	'''INSTR :   SEC
			| INSTR1'''
	p[0] = InstrTree("Instruccion General", p[1])

# Secuenciacion

def p_sec(p):
	'''SEC : INSTR INSTR1'''
	p[0] = InstrTree("Secuenciacion", [p[1], p[2]])

# Instrucciones

def p_instr1(p):
	'''INSTR1 :  ASIG
			| I_O
			| COND
			| DETER
			| INDETER
			| INICIO'''
	p[0] = InstrTree("Instruccion", p[1])

# Asignacion 

def p_asig(p):
	'''ASIG : TkId TkAsignacion EXPR TkPuntoYComa
 	| TkId TkAsignacion EXPR'''
	p[0] = InstrTree("Asignacion", p[3])

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
			| TkId'''
	if (len(p) == 2):
		if (p[1] == 'TkNum'):
			p[0] = Number(p[1])
		else:
			p[0] = Ident(p[1])
	elif (len(p) == 4):
		if ((p[1] == '(') and (p[1] == ')')):
			p[0] = InstrTree("Expresion Aritmetica", p[2])
		else:
			p[0] = InstrTree("Expresion Aritmetica", [p[1], p[3]])
	else:
		p[0] = UniOp("Expresion Aritmetica", p[2], p[3])

# Negacion Aritmetica

def p_nega(p):
	'''ARIT :	  TkResta ARIT %prec NEGA'''
	p[0] = UniOp("Negacion Aritmetica", p[1], p[2])

# Expresiones Booleanas

def p_bool(p):
	'''BOOL : BOOL TkConjuncion BOOL
			| BOOL TkDisyuncion BOOL
			| ARIT TkMenor ARIT
			| ARIT TkMenorIgual ARIT
			| ARIT TkMayor ARIT
			| ARIT TkMayorIgual ARIT
			| EXPR TkIgual EXPR
			| TkParAbre BOOL TkParCierra
			| TkFalse
			| TkTrue
			| TkNegacion BOOL'''
	if (len(p) == 4):
		if ((p[1] == '(') and (p[3] == ')')):
			p[0] = InstrTree("Expresion Booleana", p[2])
		else:
			p[0] = BinOp(p[1], p[2], p[3], "Expresion Booleana")
	elif (len(p) == 3):
		p[0] = UniOp("Expresion Booleana", p[2], p[1])
	else:
		if (p[1] == 'TkId'):
			p[0] = Ident(p[1])
		else:
			p[0] == Bool(p[1])


# Expresiones con caracteres

def p_char(p):
	'''CHAR : TkCaracter
			| TkCaracter TkSiguienteCar
			| TkCaracter TkAnteriorCar'''
	if (len(p) == 2):
		if (p[1] == 'TkId'):
			p[0] = Ident(p[1])
		else:
			p[0] == Char(p[1])
	else:
		p[0] = UniOp("Expresion con Caracteres", p[2], p[1])


# Condicionales general

def p_cond(p):
	'''COND : 	  TkIf BOOL TkHacer INSTR COND0'''
	p[0] = InstrTree("Condicional General", [p[2], p[4], p[5]])

# Condicionales 

def p_cond0(p):
	'''COND0 :   TkOtherwise TkHacer INSTR
			| TkEnd'''
	p[0] = InstrTree("Condicional", p[3])

# Iteracion indeterminada

def p_indeter(p):
	'''INDETER : TkWhile BOOL TkHacer INSTR TkEnd'''
	p[0] = InstrTree("Iteracion Indeterminada", [p[2], p[4]])

# Iteracion determinada general

def p_deter(p):
	'''DETER :   TkFor TkId TkFrom ARIT TkTo ARIT DETER0'''
	p[0] = InstrTree("Iteracion Determinada General", [p[4], p[6], p[7]])

# Iteracion determinada

def p_deter0(p):
	'''DETER0 :  TkStep ARIT TkHacer INSTR TkEnd
			| TkHacer INSTR TkEnd'''
	if (len(p) == 6):
		p[0] = InstrTree("Iteracion Determinada", [p[2], p[4]])
	else:
		p[0] = InstrTree("Iteracion Determinada", p[2])
# Entrada y salida

def p_i_o(p):
	'''I_O :  TkRead TkId TkPuntoYComa
			| TkPrint EXPR TkPuntoYComa'''
	p[0] = UniOp("Entrada o Salida", p[1], p[2])

# Expresiones en general

def p_expr(p):
	'''EXPR : CHAR
			| ARIT
			| ARRAY
			| TkId TkCorcheteAbre ARIT TkCorcheteCierra
			| TkId'''
	if (len(p) == 2):
		p[0] = InstrTree("Expresion", p[1])
	else:
		p[0] = InstrTree("Indexacion", p[3])

# Arreglos

def p_array(p):
	'''ARRAY : ARRAY TkConcatenacion ARRAY
			 | TkShift ARRAY
			 | TkId'''
	if (len(p) == 4):
		p[0] = InstrTree("Arreglo", [p[1], p[3]])
	else:
		p[0] = UniOp("Shift", p[1], p[2])

# Detección de errores
def p_error(p):
    if (not p):
        return
    print("Error de sintaxis en la entrada.\nError: '" + str(p.value) +\
     "' ubicado en la fila {:d}, columna {:d}.".format(p.lineno,\
      find_column(content, p)))
    sys.exit()

precedence = (
	('left', 'NEGA', 'TkMult', 'TkDiv', 'TkMod', 'TkSuma', 'TkResta'),
	('left', 'TkNegacion', 'TkConjuncion', 'TkDisyuncion'),
	('left', 'TkValorAscii', 'TkAnteriorCar', 'TkSiguienteCar'),
	('left', 'TkCorcheteAbre', 'TkShift', 'TkConcatenacion')
	)