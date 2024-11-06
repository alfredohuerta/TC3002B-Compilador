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
        self.cube = Cube()        # Cubo semántico
        self.operand_stack = []   # Pila de operandos
        self.operator_stack = []  # Pila de operadores
        self.type_stack = []      # Pila de tipos
        self.jump_stack = []      # Pila de saltos
        self.quadruples = []      # Fila de cuádruplos
        self.temp_counter = 0     # Contador para variables temporales


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

        # Process each var_decl individually
        for var_decl_ctx in ctx.var_decl():
            self.process_var_decl(var_decl_ctx)

    def process_var_decl(self, ctx):
        var_ids = [id_token.getText() for id_token in ctx.ID()]
        var_type = ctx.tipo().getText()
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
                raise Exception(
                    f"Error: La variable '{var_name}' ya ha sido declarada en la función '{self.current_function}'.")
            else:
                self.function_directory.add_variable_to_function(self.current_function, var_name, var_type)
                print(
                    f"Variable local '{var_name}' de tipo '{var_type}' agregada a la función '{self.current_function}'.")

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
        if operator in ['+', '-']:
            self.operator_stack.append(operator)
            print(f"Operador '{operator}' detectado y agregado a la pila de operadores.")

    def enterDivmult(self, ctx: patitoParser.DivmultContext):
        operator = ctx.getText()
        if operator in ['*', '/']:
            self.operator_stack.append(operator)
            print(f"Operador '{operator}' detectado y agregado a la pila de operadores.")

    def enterCondicion(self, ctx: patitoParser.CondicionContext):
        # No action needed here
        pass

    def enterCiclo(self, ctx: patitoParser.CicloContext):
        # Registra el índice al inicio de un ciclo para su salto
        self.jump_stack.append(len(self.quadruples))
        print(f"Guardando el inicio del ciclo en la pila de saltos: {len(self.quadruples)}")

    def enterAsigna(self, ctx: patitoParser.AsignaContext):
        # Push the '=' operator onto the operator stack
        self.operator_stack.append('=')

    def enterImprime(self, ctx: patitoParser.ImprimeContext):
        self.escribe_params = []  # Reset the list of parameters

    def enterLlamada(self, ctx: patitoParser.LlamadaContext):
        func_name = ctx.ID().getText()
        if not self.function_directory.get_function(func_name):
            raise Exception(f"Error: La función '{func_name}' no ha sido declarada.")
        else:
            # Generate ERA quadruple
            quadruple = ('ERA', func_name, None, None)
            self.quadruples.append(quadruple)
            print(f"Generando cuádruplo: {quadruple}")
            # Handle parameters if any (not covered here)
            # Generate GOSUB quadruple
            quadruple = ('GOSUB', func_name, None, None)
            self.quadruples.append(quadruple)
            print(f"Generando cuádruplo: {quadruple}")

    def exitExp(self, ctx: patitoParser.ExpContext):
        if ctx.op():
            operator = self.operator_stack.pop()
            right_operand = self.operand_stack.pop()
            right_type = self.type_stack.pop()
            left_operand = self.operand_stack.pop()
            left_type = self.type_stack.pop()
            result_type = self.cube.get_result_type(operator, left_type, right_type)
            if result_type == 'error':
                raise Exception(
                    f"Error semántico: Operación '{operator}' no permitida entre '{left_type}' y '{right_type}'.")
            else:
                temp_var = f"t{self.temp_counter}"
                self.temp_counter += 1
                self.operand_stack.append(temp_var)
                self.type_stack.append(result_type)
                quadruple = (operator, left_operand, right_operand, temp_var)
                self.quadruples.append(quadruple)
                print(f"Generando cuádruplo: {quadruple}")

    def exitTermino(self, ctx: patitoParser.TerminoContext):
        if ctx.divmult():
            operator = self.operator_stack.pop()
            right_operand = self.operand_stack.pop()
            right_type = self.type_stack.pop()
            left_operand = self.operand_stack.pop()
            left_type = self.type_stack.pop()
            result_type = self.cube.get_result_type(operator, left_type, right_type)
            if result_type == 'error':
                raise Exception(
                    f"Error semántico: Operación '{operator}' no permitida entre '{left_type}' y '{right_type}'.")
            else:
                temp_var = f"t{self.temp_counter}"
                self.temp_counter += 1
                self.operand_stack.append(temp_var)
                self.type_stack.append(result_type)
                quadruple = (operator, left_operand, right_operand, temp_var)
                self.quadruples.append(quadruple)
                print(f"Generando cuádruplo: {quadruple}")

    def exitCiclo(self, ctx: patitoParser.CicloContext):
        # After processing the loop condition
        exp_type = self.type_stack.pop()
        if exp_type != 'bool':
            raise Exception("Error: La expresión en el 'Mientras' no es booleana.")
        else:
            result = self.operand_stack.pop()
            # Generate the GOTOF quadruple
            quadruple_gotof = ('GOTOF', result, None, None)
            self.quadruples.append(quadruple_gotof)
            print(f"Generando cuádruplo: {quadruple_gotof}")
            # Save the index of the GOTOF for backpatching
            false_jump = len(self.quadruples) - 1

            # Retrieve the loop start index
            loop_start = self.jump_stack.pop()
            # Generate the GOTO quadruple to return to the start of the loop
            quadruple_goto = ('GOTO', None, None, loop_start)
            self.quadruples.append(quadruple_goto)
            print(f"Generando cuádruplo: {quadruple_goto}")

            # Backpatch the GOTOF quadruple with the current quadruple index
            self.quadruples[false_jump] = self.quadruples[false_jump][:3] + (len(self.quadruples),)
            print(f"Actualizando cuádruplo en posición {false_jump} con salto a {len(self.quadruples)}")

    def exitAsigna(self, ctx: patitoParser.AsignaContext):
        operator = self.operator_stack.pop()
        right_operand = self.operand_stack.pop()
        right_type = self.type_stack.pop()
        left_operand = ctx.ID().getText()
        left_var_info = self.get_variable_info(left_operand)
        if not left_var_info:
            raise Exception(f"Error: La variable '{left_operand}' no ha sido declarada.")
        left_type = left_var_info['type']
        result_type = self.cube.get_result_type(operator, left_type, right_type)
        if result_type == 'error':
            raise Exception(f"Error semántico: Asignación no permitida entre '{left_type}' y '{right_type}'.")
        else:
            # Generate the quadruple
            quadruple = (operator, right_operand, None, left_operand)
            self.quadruples.append(quadruple)
            print(f"Generando cuádruplo: {quadruple}")

    def exitImprime(self, ctx: patitoParser.ImprimeContext):
        for param in self.escribe_params:
            if isinstance(param, str) and param.startswith('"') and param.endswith('"'):
                # String literal
                quadruple = ('Escribe', param, None, None)
                self.quadruples.append(quadruple)
                print(f"Generando cuádruplo: {quadruple}")
            else:
                # It's an operand (variable or temp variable)
                quadruple = ('Escribe', param, None, None)
                self.quadruples.append(quadruple)
                print(f"Generando cuádruplo: {quadruple}")

    def exitParam(self, ctx: patitoParser.ParamContext):
        if ctx.LETRERO():
            text = ctx.LETRERO().getText()
            self.escribe_params.append(text)
        elif ctx.expresion():
            # The expression has been processed; operand is on top of the stack
            operand = self.operand_stack.pop()
            operand_type = self.type_stack.pop()
            self.escribe_params.append(operand)

    def exitExpresion(self, ctx: patitoParser.ExpresionContext):
        # Check if there are more than one child (indicating the presence of a relational operation)
        if len(ctx.children) == 3:
            operator = ctx.getChild(1).getText()
            # Pop right operand and type
            right_operand = self.operand_stack.pop()
            right_type = self.type_stack.pop()
            # Pop left operand and type
            left_operand = self.operand_stack.pop()
            left_type = self.type_stack.pop()
            # Get the result type from the semantic cube
            result_type = self.cube.get_result_type(operator, left_type, right_type)
            if result_type == 'error':
                raise Exception(
                    f"Error semántico: Operación relacional '{operator}' no permitida entre '{left_type}' y '{right_type}'.")
            else:
                # Create a temporary variable to store the result
                temp_var = f"t{self.temp_counter}"
                self.temp_counter += 1
                self.operand_stack.append(temp_var)
                self.type_stack.append(result_type)
                # Generate the quadruple
                quadruple = (operator, left_operand, right_operand, temp_var)
                self.quadruples.append(quadruple)
                print(f"Generando cuádruplo: {quadruple}")

    def exitCondicion(self, ctx: patitoParser.CondicionContext):
        # Pop the expression type and operand
        exp_type = self.type_stack.pop()
        if exp_type != 'bool':
            raise Exception("Error: La expresión en el 'Si' no es booleana.")
        else:
            result = self.operand_stack.pop()
            # Generate the GOTOF quadruple
            quadruple = ('GOTOF', result, None, None)
            self.quadruples.append(quadruple)
            false_jump = len(self.quadruples) - 1
            self.jump_stack.append(false_jump)
            print(f"Generando cuádruplo: {quadruple}")

        if ctx.SINO():
            # Generate GOTO to jump over the else block
            quadruple = ('GOTO', None, None, None)
            self.quadruples.append(quadruple)
            end_jump = len(self.quadruples) - 1
            # Backpatch the false jump to point to the else block
            false_jump = self.jump_stack.pop()
            self.quadruples[false_jump] = self.quadruples[false_jump][:3] + (len(self.quadruples),)
            print(f"Actualizando cuádruplo en posición {false_jump} con salto a {len(self.quadruples)}")
            # Push the end jump to backpatch after the else block
            self.jump_stack.append(end_jump)
            # After processing the else block, backpatch the end jump
            end_jump = self.jump_stack.pop()
            self.quadruples[end_jump] = self.quadruples[end_jump][:3] + (len(self.quadruples),)
            print(f"Actualizando cuádruplo en posición {end_jump} con salto a {len(self.quadruples)}")
        else:
            # No else part
            false_jump = self.jump_stack.pop()
            # Backpatch the false jump to point to the next instruction
            self.quadruples[false_jump] = self.quadruples[false_jump][:3] + (len(self.quadruples),)
            print(f"Actualizando cuádruplo en posición {false_jump} con salto a {len(self.quadruples)}")

    def get_variable_info(self, var_name):
        # Primero, buscar en las variables locales (incluyendo parámetros)
        if self.current_scope == 'local':
            function = self.function_directory.get_function(self.current_function)
            if function:
                if var_name in function['variables']:
                    return function['variables'][var_name]
        # Luego, buscar en las variables globales
        return self.global_variables.get_variable(var_name)

