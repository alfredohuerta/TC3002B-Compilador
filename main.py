import sys
from antlr4 import *
from patitoLexer import patitoLexer
from patitoParser import patitoParser

def main(argv):
    input_stream = FileStream(argv[1])  # Lee el archivo de entrada
    lexer = patitoLexer(input_stream)   # Crea el lexer
    stream = CommonTokenStream(lexer)   # Convierte los tokens en un flujo
    parser = patitoParser(stream)       # Crea el parser
    tree = parser.programa()            # Llama a la regla inicial (ajusta si es necesario)

    print(tree.toStringTree(recog=parser))  # Imprime el árbol de análisis

if __name__ == '__main__':
    main(sys.argv)
