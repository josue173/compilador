import ply.lex as lex
import ply.yacc as yacc
from lexer import tokens  # Importa la lista de tokens desde lexer.py

class SymbolTable:
    def __init__(self):
        self.symbols = {}
    
    def add_symbol(self, name, symbol_type):
        if name in self.symbols:
            raise Exception(f"Error: '{name}' ya está declarado.")
        self.symbols[name] = symbol_type
    
    def get_type(self, name):
        return self.symbols.get(name, None)
    
    def exists(self, name):
        return name in self.symbols

symbol_table = SymbolTable()

precedence = (
    ('left', 'PLUS', 'MINUS'),
    ('left', 'TIMES', 'DIVIDE'),
)

def p_statement_declaration(p):
    """statement : INT IDENTIFIER
                  | FLOAT IDENTIFIER
                  | BOOL IDENTIFIER"""
    symbol_table.add_symbol(p[2], p[1])
    p[0] = f"Declaración: {p[1]} {p[2]}"

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
    if not symbol_table.exists(p[1]):
        raise Exception(f"Error semántico: Variable '{p[1]}' no declarada.")
    p[0] = p[1]

def p_assignment(p):
    """assignment : IDENTIFIER ASSIGN expression"""
    if not symbol_table.exists(p[1]):
        raise Exception(f"Error semántico: Variable '{p[1]}' no declarada antes de su asignación.")
    p[0] = ('=', p[1], p[3])

def p_grouped_expression(p):
    """expression : LPAREN expression RPAREN"""
    p[0] = p[2]

def p_error(p):
    if p:
        print(f"Error de sintaxis en '{p.value}'")
    else:
        print("Error de sintaxis en la entrada")

parser = yacc.yacc()