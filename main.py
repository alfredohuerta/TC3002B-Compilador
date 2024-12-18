import sys
from antlr4 import *
from antlr_files.patitoLexer import patitoLexer
from antlr_files.patitoParser import patitoParser
from semantic_analyzer import SemanticAnalyzer
from virtual_machine import VirtualMachine

def main(argv):
    if len(argv) < 2:
        print("Uso: python main.py <archivo_entrada>")
        return

    # Leer el archivo de entrada con codificación UTF-8
    input_stream = FileStream(argv[1], encoding='utf-8')

    # Crear el lexer y parser
    lexer = patitoLexer(input_stream)
    stream = CommonTokenStream(lexer)
    parser = patitoParser(stream)

    # Llamar a la regla inicial de la gramática
    tree = parser.programa()

    # Imprimir el árbol de análisis
    # print(tree.toStringTree(recog=parser))

    # Crear e iniciar el analizador semántico
    semantic_analyzer = SemanticAnalyzer()
    walker = ParseTreeWalker()
    walker.walk(semantic_analyzer, tree)

    # Imprimir las tablas para verificación
    # Print the variables of each function
    # print("\nDirectorio de Funciones:")
    # for func_name, func_info in semantic_analyzer.function_directory.functions.items():
    #     print(f"Función '{func_name}':")
    #     print(f"  Retorno: {func_info['return_type']}")
    #     print(f"  Parámetros: {func_info['parameters']}")
    #     print(f"  Variables Locales:")
    #     for var_name, var_info in func_info['variables'].variables.items():
    #         print(f"    {var_name}: {var_info}")
    #
    # print("\nVariables Globales:")
    # for var_name, var_info in semantic_analyzer.global_variables.variables.items():
    #     print(f"{var_name}: {var_info}")
    #
    # # Imprimir las constantes
    # print("\nTabla de Constantes:")
    # for const_value, const_info in semantic_analyzer.constant_table.constants.items():
    #     print(f"{const_value}: {const_info}")
    #
    # # Imprimir los cuádruplos generados
    # print("\nCuádruplos generados:")
    # for i, quad in enumerate(semantic_analyzer.quadruples):
    #     print(f"{i}: {quad}")

    # Corremos la máquina virtual
    quadruples = semantic_analyzer.quadruples
    constant_table = semantic_analyzer.constant_table.constants
    function_addresses = semantic_analyzer.function_addresses
    vm = VirtualMachine(quadruples, constant_table, function_addresses)
    vm.execute()


if __name__ == '__main__':
    main(sys.argv)
