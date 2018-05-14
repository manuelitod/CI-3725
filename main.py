# ------------------------------------------------------------
# main.py
#
# Programa que ejecuta el lexer dada un archivo de entrada
# ------------------------------------------------------------

from lexer import *

lexer = lex.lex()

# Inicializacion del lexer
lexer.input(content)

# Lista que contiene todos los tokens hallados
ListaTokens = []

# Tokenizar
while True:
    tok = lexer.token()
    if not tok: 
        break      # No more input
    ListaTokens.append(tok)

j = 1

# En caso de estar vacia la lista de errores se procede a mostrar en consola los tokens hallados

if (len(ListaTokensErrores) == 0):
	for i in ListaTokens:
		if (i.type == "TkId"):
			print(i.type + '("' + i.value + '")' + " " + str(i.lineno) + " " + str(find_column(content, i)), end = '')
		else:
			print(i.type +" " + str(i.lineno) + " " + str(find_column(content, i)), end = '')
		if (j != len(ListaTokens)):
			print(",")
		else:
			print()
		j += 1