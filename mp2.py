# vars = x, y, z
# operations = add, sub and unary
# terminator = $

# BNF grammar definition:
# <expression> ::= <term> <expression_tail> $
# <expression_tail> ::= <op> <term> <expression_tail> | ε
# <term> ::= <factor> | ~<factor>
# <factor> ::= <identifier> | (<inner_expr>)
# <inner_expr> ::= <term> <expression_tail>
# <op> ::= "+" | "-"
# <identifier> ::= "x" | "y" | "z"

class ParseInput:
    def __init__(self, input_string):
        self.input_string = input_string
        self.position = 0

    def current_char(self):
        if self.position < len(self.input_string):
            return self.input_string[self.position]
        return None

    def is_expected(self, expected = None):
        print(f"expecting {expected}, got {self.current_char()}")
        if expected and self.current_char() != expected:
            print(f"no match for expected char")
        self.position += 1

    def parse_expression(self):
        # <expression> ::= <term> <expression_tail> $
        if not self.parse_term():
            return False
        if not self.parse_expression_tail():
            return False
        return True
    
    def parse_expression_tail(self):
        # <expression_tail> ::= <op> <term> <expression_tail> | ε
        if self.current_char() in ('+', '-'):
            self.is_expected()  # consume the operator
            if not self.parse_term():
                return False
            if not self.parse_expression_tail():
                return False
        return True  # ε case
    
    def parse_term(self):
        # <term> ::= <factor> | ~<factor>
        if self.current_char() == '~':
            self.is_expected("~")  # consume '~'
            if not self.parse_factor():
                return False
        else:
            if not self.parse_factor():
                return False
        return True
    
    def parse_factor(self):
        # <factor> ::= <identifier> | (<inner_expr>)
        if self.current_char() in ('x', 'y', 'z'):
            self.is_expected()  # consume identifier
        elif self.current_char() == '(':
            self.is_expected("(")  # consume '('
            if not self.parse_inner_expr():
                return False
            if self.current_char() == ')':
                self.is_expected(")")  # consume ')'
            else:
                print("missing closing parenthesis")
                return False
        else:
            print("invalid factor")
            return False
        return True
    
    def parse_inner_expr(self):
        # <inner_expr> ::= <term> <expression_tail>
        if not self.parse_term():
            return False
        if not self.parse_expression_tail():
            return False
        return True
    

# -------------- Main -------------- 
if __name__ == "__main__":
    input_string = input("Enter an expression (end with $): ")
    parser = ParseInput(input_string)
    
    if parser.parse_expression() and parser.current_char() == '$':
        print("Valid expression")
    else:
        print("Invalid expression")
    

