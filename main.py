# ------------------------------------------------------------
# main.py
#
# Programa que ejecuta el lexer dada un archivo de entrada
# ------------------------------------------------------------

from lexer import *

# Inicializacion del lexer
lexer.input(content)

# Tokenizar
while True:
    tok = lexer.token()
    if not tok: 
        break      # No more input
    print(tok)