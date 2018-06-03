import ply.yacc as yacc
import re

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
		| TkVar IDENT TkDosPuntos TIPO'''
	if (len(p) == 6):
		p[0] = InstrTree("Lista de Declaraciones", [p[1], p[3], p[5]])
	else:
		p[0] = InstrTree("Lista de Declaraciones", [p[2], p[4]])

# Identificadores

def p_ident(p):
	'''IDENT :   IDENT TkComa TkId
			| TkId
			| ASIG'''
	if (len(p) == 4):
		p[0] = InstrTree("Identificador", p[2])
	else:
		p[0] = InstrTree("Identificador", p[1])


# Tipos de variables

def p_tipo(p):
	'''TIPO :    TkInt
			| TkChar
			| TkBool
			| TkArray'''
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
	'''ASIG :    TkId TkAsignacion ARIT TkPuntoYComa
			| TkId TkAsignacion BOOL TkPuntoYComa'''
	p[0] = InstrTree("Asignacion", p[3])

# Expresiones Aritmeticas

def p_arit(p):
	'''ARIT : TkNum
			| TkId
			| TkParAbre ARIT TkParCierra
			| ARIT TkSuma ARIT
			| ARIT TkResta ARIT
			| ARIT TkMult ARIT
			| ARIT TkDiv ARIT
			| ARIT TkMod ARIT
			| TkValorAscii TkCaracter'''
	if (len(p) == 2):
		if (p[1].type == 'TkNum'):
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
			| BOOL TkMenor BOOL
			| BOOL TkMenorIgual BOOL
			| BOOL TkMayor BOOL
			| BOOL TkMayorIgual BOOL
			| BOOL TkIgual BOOL
			| TkParAbre BOOL TkParCierra
			| TkFalse
			| TkTrue
			| TkId
			| TkNegacion BOOL'''
	if (len(p) == 4):
		if ((p[1] == '(') and (p[3] == ')')):
			p[0] = InstrTree("Expresion Booleana", p[2])
		else:
			p[0] = BinOp(p[1], p[2], p[3], "Expresion Booleana")
	elif (len(p) == 3):
		p[0] = UniOp("Expresion Booleana", p[2], p[1])
	else:
		if (p[1].type == 'TkId'):
			p[0] = Ident(p[1])
		else:
			p[0] == Bool(p[1])


# Expresiones con caracteres

def p_char(p):
	'''CHAR : TkId
			| TkCaracter
			| TkCaracter TkSiguienteCar
			| TkCaracter TkAnteriorCar'''
	if (len(p) == 2):
		if (p[1].type == 'TkId'):
			p[0] = Ident(p[1])
		else:
			p[0] == Char(p[1])
	else:
		p[0] = UniOp("Expresion con Caracteres", p[2], p[1])


# Condicionales general

def p_cond(p):
	'''COND : 	  TkIf TkHacer INSTR COND0'''
	p[0] = InstrTree("Condicional General", [p[3], p[4]])

# Condicionales 

def p_cond0(p):
	'''COND0 :   TkOtherwise TkHacer INSTR
			| TkEnd'''
	p[0] = InstrTree("Condicional", p[3])

# Iteracion indeterminada

def indeter(p):
	'''INDETER : TkWhile BOOL TkHacer INSTR TkEnd'''
	p[0] = InstrTree("Iteracion Indeterminada", [p[2], p[4]])

# Iteracion determinada general

def deter(p):
	'''DETER :   TkFor TkId TkFrom ARIT TkTo ARIT DETER0'''
	p[0] = InstrTree("Iteracion Determinada General", [p[4], p[6], p[7]])

# Iteracion determinada

def deter0(p):
	'''DETER0 :  TkStep ARIT TkHacer INSTR TkEnd
			| TkHacer INSTR TkEnd'''
	p[0] = InstrTree("Iteracion Determinada", [p[2], p[4]])

# Entrada y salida

def i_o(p):
	'''I_O :  TkRead TkId
			| TkBegin EXPR'''
	p[0] = UniOp("Entrada o Salida", p[1], p[2])

# Expresiones en general

def expr(p):
	'''EXPR : 	  CHAR
			| BOOL
			| ARIT'''
	p[0] = InstrTree("Expresion", p[1])

precedence = (
	('left', 'NEGA', 'TkMul', 'TkDiv', 'TkMod', 'TkSuma', 'TkResta')
	('left', 'TkNegacion', 'TkConjuncion', 'TkDisyuncion')
	('left', 'TkValorAscii', 'TkAnteriorCar', 'TkSiguienteCar')
	('left', 'TkIndexacion', 'TkShift', 'TkConcatenacion')
	)