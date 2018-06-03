import ply.yacc as yacc
import re
from structs import *
from lexNEO import *

global Tree

Tree = InstrTree()

# Símbolo inicial

def p_inicio(p):
	'''INICIO :  TkWith DEC TkBegin INSTR TkEnd
			| TkBegin INSTR TkEnd'''

# Lista de Declaraciones

def p_dec(p):
	'''DEC : DEC TkVar IDENT TkDosPuntos TIPO
		| TkVar IDENT TkDosPuntos TIPO'''

# Identificadores

def p_ident(p):
	'''IDENT :   IDENT TkComa TkId
			| TkId
			| ASIG'''

# Tipos de variables

def p_tipo(p):
	'''TIPO :    TkInt
			| TkChar
			| TkBool
			| TkArray'''

# Instrucciones generales

def p_instr(p):
	'''INSTR :   SEC
			| INSTR1'''
# Secuenciacion

def p_sec(p):
	'''SEC : INSTR INSTR1'''

# Instrucciones

def p_instr1(p):
	'''INSTR1 :  ASIG
			| I_O
			| COND
			| DETER
			| INDETER
			| INICIO'''

# Asignacion 

def p_asig(p):
	'''ASIG :    TkId TkAsignacion ARIT TkPuntoYComa
			| TkId TkAsignacion BOOL TkPuntoYComa'''

# Expresiones Aritmeticas

def p_arit(p):
	'''ARIT :    TkNum
			| TkId
			| TkParAbre ARIT TkParCierra
			| ARIT TkSuma ARIT
			| ARIT TkResta ARIT
			| ARIT TkMult ARIT
			| ARIT TkDiv ARIT
			| ARIT TkMod ARIT
			| TkValorAscii TkCaracter
			| TkNum TkSiguienteCar
			| TkNum TkAnteriorCar'''

def p_nega(p):
	'''ARIT :	  TkResta ARIT %prec NEGA'''

# Expresiones Booleanas

def p_bool(p):
	'''BOOL : 	  BOOL TkConjuncion BOOL
			| BOOL TkDisyuncion BOOL
			| BOOL TkMenor BOOL
			| BOOL TkMenorIgual BOOL
			| BOOL TkMayor BOOL
			| BOOL TkMayorIgual BOOL
			| BOOL TkIgual BOOL
			| TkParAbre BOOL TkParCierra
			| TkNegacion BOOL
			| TkFalse
			| TkTrue'''

# Expresiones con caracteres

def p_char(p):
	'''CHAR : 	  TkId
			| TkCaracter
			| CHAR TkConcatenacion CHAR
			| TkCaracter TkSiguienteCar
			| TkCaracter TkAnteriorCar'''

# Condicionales general

def p_cond(p):
	'''COND : 	  TkIf TkHacer INSTR COND0'''

# Condicionales 

def p_cond0(p):
	'''COND0 :   TkOtherwise TkHacer INSTR
			| TkEnd'''

# Iteracion indeterminada

def indeter(p):
	'''INDETER : TkWhile BOOL TkHacer INSTR TkEnd'''

# Iteracion determinada general

def deter(p):
	'''DETER :   TkFor TkId TkFrom ARIT TkTo ARIT DETER0'''

# Iteracion determinada

def deter0(p):
	'''DETER0 :  TkStep ARIT TkHacer INSTR TkEnd
			| TkHacer INSTR TkEnd'''

# Entrada y salida

def i_o(p):
	'''I_O : 	  TkRead TkId
			| TkBegin EXPR'''

# Expresiones en general

def expr(p):
	'''EXPR : 	  CHAR
			| BOOL
			| ARIT'''

precedence = (
	('left', 'TkConjuncion', 'TkDisyuncion', 'TkSiguienteCar', 'TkAnteriorCar', 'TkConcatenacion'),
	('left' , 'TkMult', 'TkDiv', 'TkMod', 'TkSuma', 'TkResta'),
	('right', 'NEGA', 'TkNegacion', 'TkValorAscii'),
	)