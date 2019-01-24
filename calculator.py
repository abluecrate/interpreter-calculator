# 1. Gather string input
# 2. Convert into token stream --> Lexical Analysis
# 3. Find expected token sequence and confirm structure
# 4. Perform addition and substraion of single-digit integers

# https://ruslanspivak.com/lsbasi-part1/

INTEGER, OPERATOR, EOF = 'INTEGER', 'OPERATOR', 'EOF'


class Token(object):

    def __init__(self, type, value):
        self.type = type    # Token Type
        self.value = value  # Token Value

    def __str__(self):      # String representation of class instance
        return 'Token({type},{value})'.format(type = self.type, value = repr(self.value))

    def __repr__(self):
        return self.__str__()


class Interpreter(object):

    def __init__(self, text):
        self.text = text            # Client String Input
        self.pos = 0                # Index into self.text
        self.currentToken = None    # Current Token Instance
        self.currentChar = self.text[self.pos]

    def error(self):
        raise Exception('Error Parsing Input')

    def advance(self):
        self.pos += 1
        if self.pos > len(self.text) - 1:
            self.currentChar = None
        else:
            self.currentChar = self.text[self.pos]

    def skipSpace(self):
        while self.currentChar is not None and self.currentChar.isspace():
            self.advance()

    def integer(self):

        result = ''

        while self.currentChar is not None and self.currentChar.isdigit():
            result += self.currentChar
            self.advance()

        return int(result)

    def getNextToken(self):             # Lexical Analyzer: breaking sentence into tokens

        while self.currentChar is not None:

            if self.currentChar.isspace():
                self.skipSpace()
                continue

            if self.currentChar.isdigit():
                return Token(INTEGER, self.integer())

            if self.currentChar in ['+','-','*','x','/']:                           # Check if character is operator
                token = Token(OPERATOR, self.currentChar)             # Create OPERATOR token
                self.advance()
                return token
                
            self.error()

        return Token(EOF, None)

    def eat(self, tokenType):
        if self.currentToken.type == tokenType:
            self.currentToken = self.getNextToken()
        else:
            self.error()

    def expr(self):                                     # INTEGER + INTEGER
        self.currentToken = self.getNextToken()         # Set current token to first token from input

        left = self.currentToken                        # Expect single-digit integer token
        self.eat(INTEGER)

        op = self.currentToken                          # Expect operator token
        self.eat(OPERATOR)

        right = self.currentToken                       # Expect single-digit integer token
        self.eat(INTEGER)

        if op.value == '+':
            result = left.value + right.value               # Add integers
        elif op.value == '-':
            result = left.value - right.value               # Subtract integers
        elif op.value in ['*','x']:
            result = left.value * right.value               # Multiply integers
        elif op.value == '/':
            result = left.value / right.value               # Divide integers
        else:
            raise Exception('OPERATION NOT SUPPORTED')
        return result


def main():
    print('------------')
    while True:
        try:    
            text = input('Calculator > ')    # Gather input
        except EOFError:
            break
        if not text:
            continue
        interpreter = Interpreter(text)     # Initialize interpreter
        result = interpreter.expr()         # Get result
        print(result)
        print('------------')

if __name__ == '__main__':
    main()  # Run Calculator