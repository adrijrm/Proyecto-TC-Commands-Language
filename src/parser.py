# parser.py
from lexer import *
from errors import SyntaxError

class Parser:
    """Parser descendente recursivo"""

    def __init__(self, tokens):
        self.tokens = tokens
        self.index = 0

    def current(self):
        return self.tokens[self.index]

    def consume(self, expected_type):
        tok_type, tok_value = self.current()
        if tok_type != expected_type:
            raise SyntaxError(f"Expected {expected_type}, got {tok_type}")
        self.index += 1
        return tok_value

    # ARGUMENTS --------------------------------------------------------------

    def parse_alnum_arg(self):
        tok_type, _ = self.current()
        if tok_type not in (TOKEN_ALNUM, TOKEN_DIGIT):
            raise SyntaxError("Expected alphanumeric argument")

        while tok_type in (TOKEN_ALNUM, TOKEN_DIGIT):
            self.index += 1
            tok_type, _ = self.current()

    def parse_digit_arg(self):
        tok_type, _ = self.current()

        if tok_type != TOKEN_DIGIT:
            raise SyntaxError("Expected digit argument")

        while tok_type == TOKEN_DIGIT:
            self.index += 1
            tok_type, _ = self.current()

    # COMMANDS ---------------------------------------------------------------

    def parse_find(self):
        self.consume(TOKEN_FIND)
        self.consume(TOKEN_COLON)
        self.parse_alnum_arg()

    def parse_replace(self):
        self.consume(TOKEN_REPLACE)
        self.consume(TOKEN_COLON)
        self.parse_alnum_arg()
        self.consume(TOKEN_COLON)
        self.parse_alnum_arg()

    def parse_delete(self):
        self.consume(TOKEN_DELETE)
        self.consume(TOKEN_COLON)
        self.parse_digit_arg()

    def parse(self):
        tok, _ = self.current()

        if tok == TOKEN_FIND:
            self.parse_find()
        elif tok == TOKEN_REPLACE:
            self.parse_replace()
        elif tok == TOKEN_DELETE:
            self.parse_delete()
        else:
            raise SyntaxError("Unknown command prefix")

        if self.current()[0] != TOKEN_EOF:
            raise SyntaxError("Unexpected extra characters")

        return True
