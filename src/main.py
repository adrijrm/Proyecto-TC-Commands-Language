# main.py
from lexer import Lexer
from parser import Parser
from errors import LexicalError, SyntaxError

def validate(command):
    try:
        tokens = Lexer(command).lex()
        Parser(tokens).parse()
        return "VALID"
    except (LexicalError, SyntaxError) as e:
        return f"INVALID: {str(e)}"

def main():
    print("Simple Command Validator (find / replace / delete)")
    print("Type 'exit' to quit.\n")

    while True:
        cmd = input("> ")

        if cmd.lower() == "exit":
            break

        print(validate(cmd))

if __name__ == "__main__":
    main()
