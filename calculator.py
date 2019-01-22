# 1. Gather string input
# 2. Convert into token stream --> Lexical Analysis
# 3. Find expected token sequence and confirm structure
# 4. Perform addition and substraion of single-digit integers

INTEGER, OPERATOR, EOF = 'INTEGER', 'OPERATOR', 'EOF'


class Token(object):

    def __init__(self, type, value):
        self.type = type    # Token Type
        self.value = value  # Token Value

    def __str__(self):      # String representation of class instance
        return 'Token({type},{value})'.format(type = self.type, value = repr(self.value))

    def __repr__(self):
        return(self.__str__())


class Interpreter(object):

    def __init__(self, text):
        self.text = text            # Client String Input
        self.pos = 0                # Index into self.text
        self.currentToken = None    # Current Token Instance

    def error(self):
        raise Exception('Error Parsing Input')

    def getNextToken(self):             # Lexical Analyzer: breaking sentence into tokens
        text = self.text                
        if self.pos > len(text) - 1:    # Check if index is past end
            return Token(EOF, None)     # Return EOF
        currentChar = text[self.pos]    # Get character at position
        if currentChar.isdigit():                       # Check if character is digit
            token = Token(INTEGER, int(currentChar))    # Create INTEGER token
            self.pos += 1                               # Move one position
            return token
        elif currentChar == '+' or currentChar == '-':                          # Check if character is plus
            token = Token(OPERATOR, currentChar)        # Create OPERATOR token
            self.pos += 1                               # Move one position
            return token
        self.error()

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
            return result
        elif op.value == '-':
            result = left.value - right.value               # Subtract integers
            return result


def main():
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


if __name__ == '__main__':
    main()  # Run Calculator