from antlr_files.patitoParser import patitoParser # Importamos el parser para poder acceder a los contextos del árbol
from antlr_files.patitoListener import patitoListener # Importamos el listener original para modificarlo
from function_directory import FunctionDirectory # Importamos el function directory para poder registrar las funciones
from variable_table import VariableTable # Importamos el function directory para poder registrar las variables
from semantic_cube import Cube # Importamos el cubo semántico para poder identificar las compatibilidades en las operaciones
from constant_table import  ConstantTable # Importamos el function directory para poder registrar las constantes

class SemanticAnalyzer(patitoListener):
    """
    Esta clase es un custom listener que generamos usando como base el listener generado por ANTLR, en este analizador
    recorremos el árbol que genera el parser y obtenemos los contextos de los diferentes nodos realizando las operaciones
    de entrada y salida en estas reglas para generar los cuádruplos y el código intermedio del proyecto
    """
    def __init__(self):
        self.function_directory = FunctionDirectory() # Instancia de FunctionDirectory para gestionar las funciones.
        self.global_variables = VariableTable(base_address=1000) # Instancia de VariableTable para variables
                                                                 # globales, con dirección base 1000
        self.local_variables = None           # Inicialmente, None, se utiliza para variables locales dentro de funciones.
        self.current_function = None          # Nombre de la función actual en la que se está trabajando.
        self.current_scope = 'global'         # Indica el alcance actual, puede ser 'global' o 'local'
        self.cube = Cube()                    # Instancia de Cube para verificar compatibilidad de tipos.
        self.constant_table = ConstantTable() # Instancia de ConstantTable para gestionar constantes.
        self.operand_stack = []               # Pila de operandos
        self.operator_stack = []              # Pila de operadores
        self.type_stack = []                  # Pila de tipos correspondientes a los operandos.
        self.jump_stack = []                  # Pila de saltos para gestionar el flujo de control.
        self.quadruples = []                  # Lista de cuádruplos generados.
        self.temp_counters = {                # Contadores para variables temporales por tipo.
            'int': 0,
            'float': 0,
            'bool': 0
        }
        self.temp_base_addresses = {          # Direcciones base para variables temporales por tipo.
            'int': 13000,
            'float': 14000,
            'bool': 15000
        }
        self.function_addresses = {}  # Añadido


    # Punto neurálgico: Inicio del programa
    def enterPrograma(self, ctx: patitoParser.ProgramaContext):
        """
        Se activa al entrar en un programa como establece la gramática
        :param ctx:
        :return:
        """
        self.current_scope = 'global' # Establece el alcance actual como global
        print("Inicio del análisis semántico del programa.")

    # Punto neurálgico: Declaración de variables
    def enterVars(self, ctx: patitoParser.VarsContext):
        """
        Determina si las variables son globales o locales según el alcance actual.
        :param ctx:
        :return:
        """
        if self.current_scope == 'global':
            print("Procesando declaración de variables globales.")
        else:
            print(f"Procesando declaración de variables locales en la función '{self.current_function}'.")
        for var_decl_ctx in ctx.var_decl(): # Procesa cada declaración de variable llamando a process_var_decl.
            self.process_var_decl(var_decl_ctx)

    def process_var_decl(self, ctx):
        """
        Función auxiliar que extrae los nombres de las variables y su tipo
        :param ctx:
        :return:
        """
        var_ids = [id_token.getText() for id_token in ctx.ID()]
        var_type = ctx.tipo().getText()
        for var_name in var_ids: # Agrega cada variable en la lista dada de ID's
            self.add_variable(var_name, var_type)

    def add_variable(self, var_name, var_type):
        """
        Verifica si la variable ya ha sido declarada en el alcance actual y llama a los métodos de la tabla de variable
        de acuerdo a lo necesario
        :param var_name: Nombre de la variable
        :param var_type: Tipo de variable
        :return:
        """
        if self.current_scope == 'global': # Si es global, utiliza registra como variable global
            if self.global_variables.get_variable(var_name): # Identifica si ya ha sido declarada y si sí, regresa error
                raise Exception(f"Error: La variable global '{var_name}' ya ha sido declarada.")
            else: # Si no ha sido declarada, la agrega a la tabla de variables como vaariable global
                self.global_variables.add_variable(var_name, var_type, 'global') # Registra los datos de la variable
                address = self.global_variables.get_variable(var_name)['address']
                print(f"Variable global '{var_name}' de tipo '{var_type}' agregada con dirección {address}.")
        else: # si el ámbito no es global, por descarte es local
            if self.function_directory.variable_exists_in_function(self.current_function, var_name): # Verifica que si ha sido registrada
                raise Exception(
                    f"Error: La variable '{var_name}' ya ha sido declarada en la función '{self.current_function}'.")
            else: # Si no ha sido declarada, la agrega a la tabla de variables como variable local
                self.function_directory.add_variable_to_function(self.current_function, var_name, var_type)
                var_info = self.function_directory.get_variable_from_function(self.current_function, var_name)
                address = var_info['address']
                print(f"Variable local '{var_name}' de tipo '{var_type}' agregada a la función '{self.current_function}' con dirección {address}.")

    # Punto neurálgico: Declaración de funciones
    def enterFuncs(self, ctx: patitoParser.FuncsContext):
        """
        Función que registra los datos de la función en la tabla de funciones
        :param ctx: patitoParser.FuncsContext Contexto de la regla de funciones en el árbol sintáctico
        :return:
        """
        func_name = ctx.ID(0).getText()
        return_type = 'void' # Solo hay funciones tipo Void, así que se hardcodea
        # Extraer el parámetro directamente
        parameters = [] # Arreglo vacío que almacena todos los posibles parámetros
        param_name = ctx.ID(1).getText() # Extráe el nombre de la función
        param_type = ctx.tipo().getText() # Extráe el tipo de dato del parámetro
        parameters.append((param_name, param_type)) # Agrega la tupla de nombre y tipo en el arreglo de parámetros

        if self.function_directory.get_function(func_name): # Busca si se encuentra la función en el directorio de funciones
            raise Exception(f"Error: La función '{func_name}' ya ha sido declarada.")
        else: # Reconoce que la función es nueva
            self.function_directory.add_function(func_name, return_type, parameters) # Registra ID, tipo de return y parámetros
            self.current_function = func_name
            self.current_scope = 'local' # Declara el ámbito de la función como local, será utilizado para las variables
            print(f"Función '{func_name}' agregada al Directorio de Funciones.")

            self.function_addresses[func_name] = len(self.quadruples)
            print(f"Dirección de inicio de la función '{func_name}' registrada en {self.function_addresses[func_name]}.")

            # Agregar el parámetro a la tabla de variables locales de la función a través del directorio de variables
            self.function_directory.add_variable_to_function(self.current_function, param_name, param_type)
            print(f"Parámetro '{param_name}' de tipo '{param_type}' agregado a la función '{self.current_function}'.")

    def exitFuncs(self, ctx: patitoParser.FuncsContext):
        """
        Función que restablece las variables con los datos de la función para reutilizarlas más tarde
        :param ctx:
        :return:
        """
        quadruple = ('RET', None, None, None) # Generamos el cuádruplo de retorno para que vuelva al main al terminar la función
        self.quadruples.append(quadruple)
        print(f"Generando cuádruplo: {quadruple}")

        self.current_scope = 'global' # Restablece el ámbito actual al global
        self.current_function = None # Restablece en qué función se encuentran

    # Punto neurálgico: Uso de variables y expresiones
    def enterFactor(self, ctx: patitoParser.FactorContext):
        """
        Identifica ID's y constantes y las agrega a sus respectivos cuádruplos y registros en la tabla de variables o
        constantes de acuerdo a lo necesario
        :param ctx:
        :return:
        """
        if ctx.ID(): # Identifica si es una variable usando las reglas de un ID
            var_name = ctx.ID().getText() # Identifica el nombre de la variable
            var_info = self.get_variable_info(var_name) # Identifica las propiedades de la variable
            if not var_info: # Identifica la variable está bien construída
                raise Exception(f"Error: La variable '{var_name}' no ha sido declarada.")
            else:
                address = var_info['address'] # Guardamos la dirección de memoria
                self.operand_stack.append(address) # Actualizamos el stack de operandos
                self.type_stack.append(var_info['type']) # Actualizamos es stack de tipos
                print(f"Uso de la variable '{var_name}' de tipo '{var_info['type']}' con dirección {address}.")
        elif ctx.cte(): # Identificamos si es una constante
            cte_node = ctx.cte() # Asignamos el valor del contexto en una variable
            if cte_node.CTE_ENT(): # Identificamos si es un entero
                value = int(cte_node.CTE_ENT().getText()) # Guardamos su valor en una variable convertido en un entero desde un string
                const_type = 'int' # Guardamos su tipo
            elif cte_node.CTE_FLOT(): # Identificamos si es un flotante
                value = float(cte_node.CTE_FLOT().getText()) # Guardamos su valor en una variable convertido en flotante desde un string
                const_type = 'float' #Guardamos su tipo
            # Agrega las constantes a la tabla de constantes
            address = self.constant_table.add_constant(value, const_type) # Asignamos una dirección de memoria
            self.operand_stack.append(address) # Guardamos la constante en el stack de operandos
            self.type_stack.append(const_type) # Guardamos la constante en el stack de tipos
            print(f"Constante {const_type} '{value}' detectada con dirección {address}.")

    def enterOp(self, ctx: patitoParser.OpContext):
        """
        Función que toma los operadores de suma (+) o resta (-) para agregarlos en el stack de operadores
        :param ctx:
        :return:
        """
        operator = ctx.getText() # Almacenamos el char en una variable
        if operator in ['+', '-']:
            self.operator_stack.append(operator) # Añadimos el char en el stack de operadores
            print(f"Operador '{operator}' detectado y agregado a la pila de operadores.")

    def enterDivmult(self, ctx: patitoParser.DivmultContext):
        """
        Función que toma los operadores de multiplicación (*) o división (/) para agregarlos en el stack de operadores
        :param ctx:
        :return:
        """
        operator = ctx.getText() # Almacenamos el char en una variable
        if operator in ['*', '/']:
            self.operator_stack.append(operator) # Añadimos el char en el stack de operadores
            print(f"Operador '{operator}' detectado y agregado a la pila de operadores.")

    def enterCondicion(self, ctx: patitoParser.CondicionContext):
        # No se hace nada aquí, este punto está integrado en exit_Expression
        pass

    def enterCiclo(self, ctx: patitoParser.CicloContext):
        """
        Esta función maneja el inicio del ciclo para su posterior uso
        :param ctx:
        :return:
        """
        # Registra el índice al inicio de un ciclo para su salto
        self.jump_stack.append(len(self.quadruples))
        print(f"Guardando el inicio del ciclo en la pila de saltos: {len(self.quadruples)}")

    def enterAsigna(self, ctx: patitoParser.AsignaContext):
        """
        Esta función sirve para asginar valores a las variables y constantes. El grueso de la operación se encuentra
        en exitAsigna
        :param ctx:
        :return:
        """
        self.operator_stack.append('=') # Añade el '=' a la pila de operadores

    def enterImprime(self, ctx: patitoParser.ImprimeContext):
        self.escribe_params = []  # Reinicia la lista de parámetros que recibe la llamada Escribe

    def enterLlamada(self, ctx: patitoParser.LlamadaContext):
        """
        Función que maneja los cuádruplos y el flujo de la llamada a las funciones. Utiliza el ID de la función para
        identificarla y registrarla en los cuádruplos
        :param ctx:
        :return:
        """
        func_name = ctx.ID().getText() # Obtenemos el nombre de la función
        if not self.function_directory.get_function(func_name): # Buscamos en el directorio de funciones a la función
            raise Exception(f"Error: La función '{func_name}' no ha sido declarada.")
        else:
            quadruple = ('ERA', func_name, None, None) # Generamos el cuádruplo de la función con su nombre para su activación
            self.quadruples.append(quadruple) # Añadimos el cuádruplo a la lista
            print(f"Generando cuádruplo: {quadruple}")
            quadruple = ('GOSUB', func_name, None, None) # Generamos el cuádruplo para ir a la función
            self.quadruples.append(quadruple) # Añadimos el cuádruplo a la lista
            print(f"Generando cuádruplo: {quadruple}")

    def generate_temp(self, temp_type):
        """
        Función que genera una dirección virtual para una variable temporal del tipo que se obtenga tras la revisión de
        compatibilidad con el cubo semántico.
        :param temp_type: Tipo del temporal a crear
        :return: Una dirección de memoria virtual para la variable temporal
        """
        # Se genera la dirección virtual usando de referencia la base definida durante la iniciación de la clase y los contadores
        address = self.temp_base_addresses[temp_type] + self.temp_counters[temp_type]
        self.temp_counters[temp_type] += 1 # Aumentamos el contador
        return address

    def exitExp(self, ctx: patitoParser.ExpContext):
        """
        Función que nos permite analizar las expresiones de suma y resta e identificar la compatibilidad de los
        operadores usando de referencia el cubo semántico para la comptaibilidad y si son compatibles, generamos el
        cuádruplo de la operación.
        :param ctx:
        :return:
        """
        if ctx.op(): # Identificamos si nos encontramos en suma o resta
            operator = self.operator_stack.pop() # Asignamos el operador desde el stack
            right_operand = self.operand_stack.pop() # Asignamos operando derecho desde el stack
            right_type = self.type_stack.pop() # Asignamos el tipo de operando derecho
            left_operand = self.operand_stack.pop() # Asignamos el operando izquierdo
            left_type = self.type_stack.pop() # Asignamos el tipo de operando izquierdo
            result_type = self.cube.get_result_type(operator, left_type, right_type) # Verificamos compatibilidad
            if result_type == 'error': # Declaramos errores en caso de que sean incompatibles
                raise Exception(
                    f"Error semántico: Operación '{operator}' no permitida entre '{left_type}' y '{right_type}'.")
            else: # En caso de que sean compatibles continuamos para construir el cuádruplo
                temp_address = self.generate_temp(result_type) # Asignamos una dirección temporal con el tipo del resultado
                self.operand_stack.append(temp_address) # Guardamos el operando del temporal
                self.type_stack.append(result_type) # Guardamos el tipo del temporal
                quadruple = (operator, left_operand, right_operand, temp_address) # Construimos el cuádruplo con los datos
                self.quadruples.append(quadruple) # Agregamos el cuádruplo nuevo en la lista de cuádruplos
                print(f"Generando cuádruplo: {quadruple}")

    def exitTermino(self, ctx: patitoParser.TerminoContext):
        """
        Función que nos permite analizar las expresiones de multiplicación y división e identificar la compatibilidad de
        los operadores usando de referencia el cubo semántico para la comptaibilidad y si son compatibles, generamos el
        cuádruplo de la operación.
        :param ctx:
        :return:
        """
        if ctx.divmult(): # Identificamos si nos encontramos en multiplicación o división
            operator = self.operator_stack.pop()  # Asignamos el operador desde el stack
            right_operand = self.operand_stack.pop()  # Asignamos operando derecho desde el stack
            right_type = self.type_stack.pop()  # Asignamos el tipo de operando derecho
            left_operand = self.operand_stack.pop()  # Asignamos el operando izquierdo
            left_type = self.type_stack.pop()  # Asignamos el tipo de operando izquierdo
            result_type = self.cube.get_result_type(operator, left_type, right_type)  # Verificamos compatibilidad
            if result_type == 'error':  # Declaramos errores en caso de que sean incompatibles
                raise Exception(
                    f"Error semántico: Operación '{operator}' no permitida entre '{left_type}' y '{right_type}'.")
            else:  # En caso de que sean compatibles continuamos para construir el cuádruplo
                temp_address = self.generate_temp(
                    result_type)  # Asignamos una dirección temporal con el tipo del resultado
                self.operand_stack.append(temp_address)  # Guardamos el operando del temporal
                self.type_stack.append(result_type)  # Guardamos el tipo del temporal
                quadruple = (
                operator, left_operand, right_operand, temp_address)  # Construimos el cuádruplo con los datos
                self.quadruples.append(quadruple)  # Agregamos el cuádruplo nuevo en la lista de cuádruplos
                print(f"Generando cuádruplo: {quadruple}")

    def exitCiclo(self, ctx: patitoParser.CicloContext):
        """
        :param ctx:
        :return:
        """
        exp_type = self.type_stack.pop() # Almacenamos el tipo de los parámetros
        if exp_type != 'bool': # Identificamos si es un valor booleano
            raise Exception("Error: La expresión en el 'Mientras' no es booleana.")
        else: # En caso de que sea un booleano, continuamos
            result = self.operand_stack.pop() # Guardamos el operando (TRUE FALSE)
            # Generate the GOTOF quadruple
            quadruple_gotof = ('GOTOF', result, None, None) # Actualizamos el cuádruplo con el valor del operando
            self.quadruples.append(quadruple_gotof) # Añadimos el cuádruplo a la lista
            print(f"Generando cuádruplo: {quadruple_gotof}")
            false_jump = len(self.quadruples) - 1 # Salvamos el índice para más tarde

            loop_start = self.jump_stack.pop() # Recuperamos el índice del inicio del loop
            quadruple_goto = ('GOTO', None, None, loop_start) # Generamos el cuádruplo de TRUE del ciclo y lo apuntamos al inicio
            self.quadruples.append(quadruple_goto) # Añadimos el cuádruplo a la lista de cuádruplos
            print(f"Generando cuádruplo: {quadruple_goto}")

            # Actualizamos el valor del cuádruplo para el FALSE con el índice actual (final del ciclo)
            self.quadruples[false_jump] = self.quadruples[false_jump][:3] + (len(self.quadruples),)
            print(f"Actualizando cuádruplo en posición {false_jump} con salto a {len(self.quadruples)}")

    def exitAsigna(self, ctx: patitoParser.AsignaContext):
        """
        Función que extraer el operador y operandos para verificar la compatibilidad de los tipos con el cubo semántico
        y genera el cuádruplo de asignación
        :param ctx:
        :return:
        """
        operator = self.operator_stack.pop() # Obtenemos el último operador usado
        right_operand = self.operand_stack.pop() # Obtenemos el operador derecho
        right_type = self.type_stack.pop() # Obtenemos el tipo derecho
        left_operand = ctx.ID().getText() # Obtenemos el operando izquierdo que debe ser una variable para asignarle valores
        left_var_info = self.get_variable_info(left_operand) # Obtenemos la información de la variable
        if not left_var_info: # Confirmamos que estemos trabajando con una variable válida
            raise Exception(f"Error: La variable '{left_operand}' no ha sido declarada.")
        left_type = left_var_info['type'] # Obtenemos el tipo de la variable
        result_type = self.cube.get_result_type(operator, left_type, right_type) # Hacemos la operación de compatibilidad
                                                                                 # y obtenemos el tipo final del operador
        if result_type == 'error': # Validamos que no haya errores
            raise Exception(f"Error semántico: Asignación no permitida entre '{left_type}' y '{right_type}'.")
        else:
            left_address = left_var_info['address'] # Generamos la dirección de memoria
            quadruple = (operator, right_operand, None, left_address) # Generamos el cuádruplo de asignación
            self.quadruples.append(quadruple) # Añadimos el cuádruplo a la lista
            print(f"Generando cuádruplo: {quadruple}")

    def exitImprime(self, ctx: patitoParser.ImprimeContext):
        for param in self.escribe_params:
            # param is the address of the operand or constant
            quadruple = ('Escribe', param, None, None)
            self.quadruples.append(quadruple)
            print(f"Generando cuádruplo: {quadruple}")

    def exitParam(self, ctx: patitoParser.ParamContext):
        if ctx.LETRERO():
            text = ctx.LETRERO().getText()
            # Add the string constant to the constant table
            address = self.constant_table.add_constant(text, 'string')
            self.escribe_params.append(address)
            print(f"Constante string {text} detectada con dirección {address}.")
        elif ctx.expresion():
            # The expression has been processed; operand is on top of the stack
            operand = self.operand_stack.pop()
            operand_type = self.type_stack.pop()
            self.escribe_params.append(operand)

    def exitExpresion(self, ctx: patitoParser.ExpresionContext):
        """
        Su función es procesar expresiones relacionales y manejar situaciones en las que la expresión forma parte de una
         estructura condicional (Si o Sino). Nos aprovechamos de la construcción en la gramática para identificar estos
         datos
        :param ctx:
        :return:
        """
        if len(ctx.children) == 3: # Verificamos si es una expresión relacional basados en el número de higos que tiene
            operator = ctx.getChild(1).getText() # Extraemos el segundo hijo del contexto que es el operador
            right_operand = self.operand_stack.pop()  # Asignamos operando derecho desde el stack
            right_type = self.type_stack.pop()  # Asignamos el tipo de operando derecho
            left_operand = self.operand_stack.pop()  # Asignamos el operando izquierdo
            left_type = self.type_stack.pop()  # Asignamos el tipo de operando izquierdo
            result_type = self.cube.get_result_type(operator, left_type, right_type)  # Verificamos compatibilidad
            if result_type == 'error':  # Declaramos errores en caso de que sean incompatibles
                raise Exception(
                    f"Error semántico: Operación '{operator}' no permitida entre '{left_type}' y '{right_type}'.")
            else:  # En caso de que sean compatibles continuamos para construir el cuádruplo
                temp_address = self.generate_temp(
                    result_type)  # Asignamos una dirección temporal con el tipo del resultado
                self.operand_stack.append(temp_address)  # Guardamos el operando del temporal
                self.type_stack.append(result_type)  # Guardamos el tipo del temporal
                quadruple = (
                operator, left_operand, right_operand, temp_address)  # Construimos el cuádruplo con los datos
                self.quadruples.append(quadruple)  # Agregamos el cuádruplo nuevo en la lista de cuádruplos
                print(f"Generando cuádruplo: {quadruple}")

        # Identificamos si el contexto padre es el de una condicional
        if isinstance(ctx.parentCtx, patitoParser.CondicionContext):
            exp_type = self.type_stack.pop() # Almacenamos el tipo del operando en una nueva variable
            if exp_type != 'bool': # Identificamos si el tipo es un boolaneo
                raise Exception("Error: La expresión en el 'Si' no es booleana.")
            else:
                result = self.operand_stack.pop()
                quadruple = ('GOTOF', result, None, None) # Creamos el cuádruplo del falso que será actualizado más tarde
                self.quadruples.append(quadruple) # Agregamos el cuádruplo en la lista de cuádruplos
                false_jump = len(self.quadruples) - 1 # Guardamos el índice actual para regresar más tarde a actualizar
                                                      # la dirección del cuádruplo
                self.jump_stack.append(false_jump) # Guardamos el índice en el stack de saltos
                print(f"Generando cuádruplo: {quadruple}")

    def exitCondicion(self, ctx: patitoParser.CondicionContext):
        """
        Función que nos permite manejar cómo se crean y parchean los cuádruplos de condicionales SI-SINO
        :param ctx:
        :return:
        """
        if ctx.SINO():
            false_jump = self.jump_stack.pop() # Guardamos el salto
            # Generar GOTO para saltar el bloque del 'Sino' después de ejecutar el 'Si'
            quadruple = ('GOTO', None, None, None) # Genera un cuádruplo GOTO vacío para más tarde
            self.quadruples.append(quadruple) # Añade el cuádruplo a la lista de cuádruplos
            end_jump = len(self.quadruples) - 1 # Índice actual que se usará más tarde
            self.quadruples[false_jump] = self.quadruples[false_jump][:3] + (false_jump + 1) # Actualizamos el valor del salto
            print(f"Actualizando cuádruplo en posición FALSE JUMP {false_jump} con salto a {false_jump + 1}")
            # Guardar el índice del GOTO para backpatching después del 'Sino'
            self.jump_stack.append(end_jump) # Agregamos el salto al jump_stack
            # Después de procesar el 'Sino', hacer backpatch del GOTO al final
            end_jump = self.jump_stack.pop() # Obtenemos el valor del salto
            self.quadruples[end_jump] = self.quadruples[end_jump][:3] + (len(self.quadruples),) # Actualizamos el valor del salto
            print(f"Actualizando cuádruplo en posición {end_jump} con salto a {len(self.quadruples)}")
        else:
            # Sin bloque 'Sino', hacer backpatch directo
            false_jump = self.jump_stack.pop()
            self.quadruples[false_jump] = self.quadruples[false_jump][:3] + (len(self.quadruples),)
            print(f"Actualizando cuádruplo en posición {false_jump} con salto a {len(self.quadruples)}")

    def get_variable_info(self, var_name):
        """
        Función que busca la información de la variable desde el ámbito local primero al global utilizando el nombre de
        la variable y su función en caso de que la tenga, para encontrar su información en el directorio de funciones
        :param var_name: Nombre de la variable
        :return: Información de la variable
        """
        if self.current_scope == 'local': # Empezamos a buscar dede el ambiente local
            # Utilizamos la variable local en la que nos encontramos de acuerdo al self para buscar en el directorio
            # los datos de la variable usando de referencia su nombre y función
            var_info = self.function_directory.get_variable_from_function(self.current_function, var_name)
            if var_info:
                return var_info
        var_info = self.global_variables.get_variable(var_name) # Damos por hecho que es una variable global
        if var_info:
            return var_info
        return None # None en caso de que haya error
