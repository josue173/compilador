import ply.lex as lex

# Lista de tokens
tokens = [
    'NUMBER', 'IDENTIFIER', 'PLUS', 'MINUS', 'TIMES', 'DIVIDE', 
    'LPAREN', 'RPAREN', 'ASSIGN', 'NEWLINE', 'FOR', 'WHILE', 
    'INT', 'FLOAT', 'BOOL', 'COMMENT'
]

# Reglas de tokens con expresiones regulares
t_PLUS    = r'\+'
t_MINUS   = r'-'
t_TIMES   = r'\*'
t_DIVIDE  = r'/'
t_LPAREN  = r'\('
t_RPAREN  = r'\)'
t_ASSIGN  = r'='

def t_NUMBER(t):
    r'\d+(\.\d+)?'  # Acepta enteros y flotantes
    if '.' in t.value:
        t.value = float(t.value)  # Convierte a float si tiene punto decimal
    else:
        t.value = int(t.value)  # Convierte a int si es entero
    return t


def t_IDENTIFIER(t):
    r'[a-zA-Z_][a-zA-Z0-9_]*'
    t.type = reserved.get(t.value, 'IDENTIFIER')  # Verificar si es palabra reservada
    return t

# Palabras reservadas
reserved = {
    'for': 'FOR',
    'while': 'WHILE',
    'int': 'INT',
    'float': 'FLOAT',
    'bool': 'BOOL'
}

# Ignorar espacios y tabulaciones
t_ignore = ' \t'

# Manejo de comentarios
def t_COMMENT(t):
    r'\#.*'
    pass  # Se ignoran los comentarios

# Manejo de saltos de línea
def t_NEWLINE(t):
    r'\n+'
    t.lexer.lineno += len(t.value)

# Manejo de errores
def t_error(t):
    print(f"Caracter ilegal: {t.value[0]}")
    t.lexer.skip(1)

# Construcción del analizador léxico
lexer = lex.lex()
