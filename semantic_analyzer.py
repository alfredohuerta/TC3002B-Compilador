from antlr_files.patitoParser import patitoParser
from antlr_files.patitoListener import patitoListener
from function_directory import FunctionDirectory
from variable_table import VariableTable
from semantic_cube import Cube

class SemanticAnalyzer(patitoListener):
    def __init__(self):
        self.function_directory = FunctionDirectory()
        self.global_variables = VariableTable()
        self.current_function = None
        self.current_scope = 'global'
        self.cube = Cube()
        self.operand_stack = []
        self.operator_stack = []
        self.type_stack = []

    # Punto neurálgico: Inicio del programa
    def enterPrograma(self, ctx: patitoParser.ProgramaContext):
        self.current_scope = 'global'
        print("Inicio del análisis semántico del programa.")

    # Punto neurálgico: Declaración de variables
    def enterVars(self, ctx: patitoParser.VarsContext):
        if self.current_scope == 'global':
            print("Procesando declaración de variables globales.")
        else:
            print(f"Procesando declaración de variables locales en la función '{self.current_function}'.")

    def enterCycle(self, ctx: patitoParser.CycleContext):
        var_ids = [id_token.getText() for id_token in ctx.ID()]
        var_type = ctx.tipo(0).getText()
        for var_name in var_ids:
            self.add_variable(var_name, var_type)

    def add_variable(self, var_name, var_type):
        if self.current_scope == 'global':
            if self.global_variables.get_variable(var_name):
                raise Exception(f"Error: La variable global '{var_name}' ya ha sido declarada.")
            else:
                self.global_variables.add_variable(var_name, var_type, 'global')
                print(f"Variable global '{var_name}' de tipo '{var_type}' agregada.")
        else:
            if self.function_directory.variable_exists_in_function(self.current_function, var_name):
                raise Exception(f"Error: La variable '{var_name}' ya ha sido declarada en la función '{self.current_function}'.")
            else:
                self.function_directory.add_variable_to_function(self.current_function, var_name, var_type)
                print(f"Variable local '{var_name}' de tipo '{var_type}' agregada a la función '{self.current_function}'.")

    # Punto neurálgico: Declaración de funciones
    def enterFuncs(self, ctx: patitoParser.FuncsContext):
        func_name = ctx.ID(0).getText()
        return_type = 'void'  # O ajusta según tu gramática si las funciones pueden tener tipos de retorno distintos

        # Extraer el parámetro directamente
        parameters = []
        param_name = ctx.ID(1).getText()
        param_type = ctx.tipo().getText()
        parameters.append((param_name, param_type))

        if self.function_directory.get_function(func_name):
            raise Exception(f"Error: La función '{func_name}' ya ha sido declarada.")
        else:
            self.function_directory.add_function(func_name, return_type, parameters)
            self.current_function = func_name
            self.current_scope = 'local'
            print(f"Función '{func_name}' agregada al Directorio de Funciones.")

            # Agregar el parámetro a la tabla de variables locales de la función
            self.function_directory.add_variable_to_function(self.current_function, param_name, param_type)
            print(f"Parámetro '{param_name}' de tipo '{param_type}' agregado a la función '{self.current_function}'.")

    def exitFuncs(self, ctx: patitoParser.FuncsContext):
        self.current_scope = 'global'
        self.current_function = None

    # Punto neurálgico: Uso de variables y expresiones
    def enterFactor(self, ctx: patitoParser.FactorContext):
        if ctx.ID():
            var_name = ctx.ID().getText()
            var_info = self.get_variable_info(var_name)
            if not var_info:
                raise Exception(f"Error: La variable '{var_name}' no ha sido declarada.")
            else:
                self.operand_stack.append(var_name)
                self.type_stack.append(var_info['type'])
                print(f"Uso de la variable '{var_name}' de tipo '{var_info['type']}'.")
        elif ctx.cte():
            cte_node = ctx.cte()
            if cte_node.CTE_ENT():
                value = cte_node.CTE_ENT().getText()
                self.operand_stack.append(value)
                self.type_stack.append('int')
                print(f"Constante entera '{value}' detectada.")
            elif cte_node.CTE_FLOT():
                value = cte_node.CTE_FLOT().getText()
                self.operand_stack.append(value)
                self.type_stack.append('float')
                print(f"Constante flotante '{value}' detectada.")

    def enterOp(self, ctx: patitoParser.OpContext):
        operator = ctx.getText()
        if operator:
            self.operator_stack.append(operator)
            print(f"Operador '{operator}' detectado.")

    def exitExp(self, ctx: patitoParser.ExpContext):
        if self.operator_stack:
            operator = self.operator_stack.pop()
            right_operand = self.operand_stack.pop()
            right_type = self.type_stack.pop()
            left_operand = self.operand_stack.pop()
            left_type = self.type_stack.pop()
            result_type = self.cube.get_result_type(operator, left_type, right_type)
            if result_type == 'error':
                raise Exception(f"Error semántico: Operación '{operator}' no permitida entre '{left_type}' y '{right_type}'.")
            else:
                temp_var = f"t{len(self.operand_stack)}"
                self.operand_stack.append(temp_var)
                self.type_stack.append(result_type)
                print(f"Operación: {left_operand} {operator} {right_operand} => {temp_var} (tipo {result_type})")

    def get_variable_info(self, var_name):
        # Primero, buscar en las variables locales (incluyendo parámetros)
        if self.current_scope == 'local':
            function = self.function_directory.get_function(self.current_function)
            if function:
                if var_name in function['variables']:
                    return function['variables'][var_name]
        # Luego, buscar en las variables globales
        return self.global_variables.get_variable(var_name)

