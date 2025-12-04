# errors.py

class LexicalError(Exception):
    """Error cuando un carácter es inválido para el lenguaje."""
    pass

class SyntaxError(Exception):
    """Error cuando la estructura del comando es sintácticamente incorrecta."""
    pass
