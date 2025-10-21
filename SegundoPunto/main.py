from antlr4 import *
from CrudEspañolLexer import CrudEspañolLexer
from CrudEspañolParser import CrudEspañolParser
import sys

def main():
    if len(sys.argv) < 2:
        print("Uso: python main.py <archivo.crud>")
        sys.exit(1)

    archivo = sys.argv[1]
    input_stream = FileStream(archivo, encoding='utf-8')

    lexer = CrudEspañolLexer(input_stream)
    stream = CommonTokenStream(lexer)
    parser = CrudEspañolParser(stream)
    
    tree = parser.programa()
    print(tree.toStringTree(recog=parser))

if __name__ == '__main__':
    main()
