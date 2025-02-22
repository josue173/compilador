import ply.yacc as yacc
from lexer import tokens  # Importa los tokens desde el analizador léxico

# Reglas de prioridad para operadores
precedence = (
    ('left', 'PLUS', 'MINUS'),
    ('left', 'TIMES', 'DIVIDE'),
)

# Reglas gramaticales
def p_statement_expr(p):
    """statement : expression
                 | assignment"""
    p[0] = p[1]

def p_expression_binop(p):
    """expression : expression PLUS expression
                  | expression MINUS expression
                  | expression TIMES expression
                  | expression DIVIDE expression"""
    p[0] = (p[2], p[1], p[3])

def p_expression_number(p):
    """expression : NUMBER"""
    p[0] = p[1]

def p_expression_identifier(p):
    """expression : IDENTIFIER"""
    p[0] = p[1]

def p_assignment(p):
    """assignment : IDENTIFIER ASSIGN expression"""
    p[0] = ('=', p[1], p[3])

def p_grouped_expression(p):
    """expression : LPAREN expression RPAREN"""
    p[0] = p[2]

def p_error(p):
    if p:
        print(f"Error de sintaxis en '{p.value}'")
    else:
        print("Error de sintaxis en la entrada")

# Construcción del analizador sintáctico
parser = yacc.yacc()
