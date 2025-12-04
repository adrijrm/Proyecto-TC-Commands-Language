# lexer.py
import string
from errors import LexicalError

TOKEN_FIND = "FIND"
TOKEN_REPLACE = "REPLACE"
TOKEN_DELETE = "DELETE"
TOKEN_COLON = "COLON"
TOKEN_ALNUM = "ALNUM"
TOKEN_DIGIT = "DIGIT"
TOKEN_EOF = "EOF"

class Lexer:
    """Lexer que convierte una cadena en tokens."""

    def __init__(self, text):
        self.text = text
        self.pos = 0

    def peek(self):
        if self.pos >= len(self.text):
            return None
        return self.text[self.pos]

    def advance(self):
        self.pos += 1

    def lex(self):
        tokens = []

        while True:
            ch = self.peek()

            if ch is None:
                tokens.append((TOKEN_EOF, None))
                break

            if ch == ":":
                tokens.append((TOKEN_COLON, ":"))
                self.advance()

            elif ch in string.ascii_lowercase + string.digits:
                if self.text.startswith("find", self.pos):
                    tokens.append((TOKEN_FIND, "find"))
                    self.pos += 4
                elif self.text.startswith("replace", self.pos):
                    tokens.append((TOKEN_REPLACE, "replace"))
                    self.pos += 7
                elif self.text.startswith("delete", self.pos):
                    tokens.append((TOKEN_DELETE, "delete"))
                    self.pos += 6
                else:
                    if ch.isdigit():
                        tokens.append((TOKEN_DIGIT, ch))
                    else:
                        tokens.append((TOKEN_ALNUM, ch))
                    self.advance()

            else:
                raise LexicalError(f"Invalid character: {ch}")

        return tokens
