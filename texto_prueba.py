from simbolos_validos import lexer

# Código a analizar
data = """
for i in range(5)

"""

lexer.input(data)

# Mostrar los tokens generados
for token in lexer:
    print(token)