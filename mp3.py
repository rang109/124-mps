# Grammar:
# <palindrome> :: = <char> | <low_pal> | <upper_pal> | <digit_pal> | e
# <low_pal> ::= a<space><palindrome><space>a | b<space><palindrome><space>b | … | z<palindrome>z
# <upper_pal> ::= A<space><palidrome><space>A | B<space><palindrome><space>B | … | Z<space><palindrome><space>Z
# <digit_pal> ::= 0<space><palidrome><space>0 | 1<space><palindrome><space>1 | … | 9<space><palindrome><space>9
# <char> ::= <lower_case> | <upper_case> | <digit>
# <lower_case> ::= a | b | c | d | … | z 
# <upper_case> ::=  A | B | C | D | … | Z
# <digit> ::= 0 | 1 | 2 | … | 9
# <space> ::= “ ” | e

class ParseInput:
    def __init__(self, input_string):
        self.input_string = input_string
        self.start = 0
        self.end = len(input_string) - 1

    def current_start_char(self):
        if self.start <= self.end:
            # print(f"current start char: {self.input_string[self.start]}")
            return self.input_string[self.start] 
        return None
    
    def current_end_char(self):
        if self.start <= self.end:
            # print(f"current end char: {self.input_string[self.end]}")
            return self.input_string[self.end] 
        return None
    
    def consume_start(self):
        self.start += 1
    
    def consume_end(self):
        self.end -= 1
    
    def parse_string(self):
        # print(f"is empty? {self.start > self.end}")
        return self.parse_palindrome() and self.start > self.end
    
    def parse_palindrome(self):
        # <palindrome> ::= <char> | <low_pal> | <upper_pal> | <digit_pal> | e
        if self.start > self.end:
            return True  # ε case
        elif self.parse_low_pal():
            # print("low pal matched")
            return True
        elif self.parse_upper_pal():
            # print("upper pal matched")
            return True
        elif self.parse_digit_pal():
            # print("digit pal matched")
            return True
        
        else:
            return False
        
    def parse_low_pal(self):
        # <low_pal> ::= a<space><palindrome><space>a | b<space><palindrome><space>b | … | z<palindrome>z
        
        # print(f"checking low pal for {self.current_start_char()} and {self.current_end_char()}")
        if self.current_start_char() == self.current_end_char() and self.parse_char():
            # save positions
            saved_start = self.start
            saved_end = self.end

            # consume the first char and last char if match
            self.consume_start()
            self.consume_end()

            # self.parse_space()  # consume space (if any)
            if self.parse_palindrome():
                return True
            
            # rollback to saved positions if not match
            self.start = saved_start
            self.end = saved_end
            
        return False
    
    def parse_upper_pal(self):
        # <upper_pal> ::= A<space><palidrome><space>A | B<space><palindrome><space>B | … | Z<space><palindrome><space>Z
        
        # print(f"checking upper pal for {self.current_start_char() and {self.current_end_char()}")
        if self.current_start_char() == self.current_end_char() and self.parse_char():
            
            # save positions
            saved_start = self.start
            saved_end = self.end

            # consume the first char and last char if match
            self.consume_start()
            self.consume_end()

            # self.parse_space()  # consume space (if any)
            if self.parse_palindrome():
                return True
            
            # rollback to saved positions if not match
            self.start = saved_start
            self.end = saved_end
            
        return False
    
    def parse_digit_pal(self):
        # <digit_pal> ::= 0<space><palidrome><space>0 | 1<space><palindrome><space>1 | … | 9<space><palindrome><space>9
    
        # print(f"checking digit pal for {self.current_start_char()}")
        if self.current_start_char() == self.current_end_char() and self.parse_char():
            # save positions
            saved_start = self.start
            saved_end = self.end

            # consume the first char and last char if match
            self.consume_start()
            self.consume_end()

            # self.parse_space()  # consume space (if any)
            if self.parse_palindrome():
                return True
            
            # rollback to saved positions if not match
            self.start = saved_start
            self.end = saved_end
            
        return False
    
    def parse_lower_case(self):
        # <lower_case> ::= a | b | c | d | … | z 
        if self.current_start_char() in 'abcdefghijklmnopqrstuvwxyz':
            return True

        print("lower case no match")
        return False
    
    def parse_upper_case(self):
        # <upper_case> ::=  A | B | C | D | … | Z
        if self.current_start_char() in 'ABCDEFGHIJKLMNOPQRSTUVWXYZ':
            return True
        
        print("upper case no match")
        return False
    
    def parse_digit(self):
        # <digit> ::= 0 | 1 | 2 | … | 9
        if self.current_start_char() in '0123456789':
            return True
        
        print("digit no match")
        return False
    
    def parse_char(self):
        # <char> ::= <lower_case> | <upper_case> | <digit>
        if self.parse_lower_case():
            return True
        elif self.parse_upper_case():
            return True
        elif self.parse_digit():
            return True
        return False
    
    # def parse_space(self):
    #     # <space> ::= “ ” | e
    #     if self.current_char() == ' ':
    #         self.is_expected(' ')  # consume the space
    #     return True  # ε case
    
    
    

# -------------- Main -------------- 
if __name__ == "__main__":
    input_string = input("Enter an expression: ")
    input_string = input_string.replace(" ", "")  # remove spaces for simplicity

    # print("Parsing:", input_string)
    parser = ParseInput(input_string)
    
    if parser.parse_string():
        print("Palindrome") 
    else:
        print("Not a palindrome")
    