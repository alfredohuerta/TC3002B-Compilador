class VirtualMachine:
    """
    Esta clase recibe los cuádruplos, tabla de constantes y la dirección de las funciones para sumular el comportamiento
    de una memoria virtual que ejecuta un programa dado donde un puntero de instrucciones recorre el arreglo de cuádruplos
    para ir interpretando las operación y realizar las acciones correspondientes.
    """
    def __init__(self, quadruples, constant_table, function_addresses):
        """
        Inicialización de la clase
        :param quadruples: Lista de cuádruplos generados por el listener
        :param constant_table: Tabla de constantes con sus direcciones
        :param function_addresses: Direcciones de memoria de las funciones
        """
        self.quadruples = quadruples  # Lista de cuádruplos que representan el programa
        self.constant_table = constant_table  # Tabla de constantes {valor: {'type': tipo, 'address': dirección}}
        self.function_addresses = function_addresses  # Direcciones de funciones {nombre_función: dirección_inicio}
        self.instruction_pointer = 0  # Puntero de instrucción (IP)
        self.memory = {
            'global': {},     # Variables globales {dirección: valor}
            'constants': {},  # Constantes {dirección: valor}
            'temporals': {},  # Temporales {dirección: valor}
            'local': {},      # Variables locales del contexto actual {dirección: valor}
            'stack': []       # Pila para gestionar contextos de funciones
        }
        self.load_constants()  # Cargar las constantes en la memoria

    def load_constants(self):
        """
        Función que recorre la tabla de constantes y carga cada constante en su segmento de memoria correspondiente
        :return:
        """
        for const_value, const_info in self.constant_table.items(): # Recorremos cada valor de la tabla de constantes
            address = const_info['address']
            self.memory['constants'][address] = const_value # Guardamos el valor de la constante en la memoria

    def execute(self):
        """
        Función que recorre el arreglo de cuádruplos a través del instruction pointer
        :return:
        """
        while self.instruction_pointer < len(self.quadruples): # nos aseguramos de que el IP está en los límites del arreglo de cuádruplos
            # Obtener el cuádruplo en la dirección actual
            quad = self.quadruples[self.instruction_pointer]
            op, arg1, arg2, result = quad # Descomponemos el cuádruplo en sus elementos principales
            # Desplegar la ejecución del cuádruplo
            #print(f"Ejecutando cuádruplo: {quad} en IP = {self.instruction_pointer}")
            # Ejecutar el cuádruplo correspondiente
            self.execute_quadruple(op, arg1, arg2, result)
            # Avanzar el puntero de instrucción
            self.instruction_pointer += 1

    def execute_quadruple(self, op, arg1, arg2, result):
        """
        Función que ejecuta las operaciones del cuádruplo dependiendo del operador que se le entrega
        :param op: operador que define la acción que se va a tomar en el cuádruplo
        :param arg1: elemento del cuádruplo
        :param arg2: elemento del cuádruplo
        :param result: resultado de la operación
        :return:
        """
        if op in ['+', '-', '*', '/']: # Operaciones aritméticas
            self.execute_arithmetic(op, arg1, arg2, result)
        elif op == '=': # Asignación de valor
            self.execute_assignment(arg1, result)
        elif op in ['>', '<', '>=', '<=', '==', '!=']:
            self.execute_relational(op, arg1, arg2, result)
        elif op == 'Escribe': # Despliegue de texto en consola
            self.execute_write(arg1)
        elif op == 'GOTO': # Desplazamiento cuando la condición es verdadera
            self.execute_goto(result)
        elif op == 'GOTOF': # Desplazamiento cuando la condición es falsa
            self.execute_gotof(arg1, result)
        elif op == 'ERA': # Preparación para llamada a una función
            self.execute_era(arg1)
        elif op == 'GOSUB': # Llamada a una función
            self.execute_gosub(arg1)
            # No incrementamos el IP aquí porque saltamos a otra dirección
            return
        elif op == 'RET': # Regresamos al main desde una función
            self.execute_ret()
            # No incrementamos el IP aquí porque regresamos de una función
            return
        else: # Manejo de errores
            raise Exception(f"Error: Operación '{op}' no reconocida.")

    def execute_arithmetic(self, op, left_addr, right_addr, result_addr):
        """
        Función que lleva a cabo operaciones aritméticas
        :param op: operador que determina la operación que se va a llevar a cabo
        :param left_addr: dirección de memoria del operando
        :param right_addr: dirección de memoria del operando
        :param result_addr: dirección de memoria del operando resultante
        :return:
        """
        left_value = self.get_value(left_addr) # Obtenemos los valores usando la dirección de memoria
        right_value = self.get_value(right_addr)
        if op == '+':
            res = left_value + right_value
        elif op == '-':
            res = left_value - right_value
        elif op == '*':
            res = left_value * right_value
        elif op == '/':
            if right_value == 0:
                raise Exception("Error: División entre cero.")
            res = left_value / right_value
        else:
            raise Exception(f"Operación aritmética desconocida: {op}")
        self.set_value(result_addr, res) # Establecemos la dirección y valor del resultado

    def execute_relational(self, op, left_addr, right_addr, result_addr):
        """
        Función que compara dos operandos en una operación booleana
        :param op: Operador booleano
        :param left_addr: Valor a comparar
        :param right_addr: Valor a comparar
        :param result_addr: Locación de memoria donde se va a almacenar el resultado
        :return: TRUE | FALSE | Error
        """
        left_value = self.get_value(left_addr) # Recupera el valor usando de referencia la memoria
        right_value = self.get_value(right_addr)
        if op == '>': # Evaluación de operaciones booleanas
            res = left_value > right_value
        elif op == '<':
            res = left_value < right_value
        elif op == '>=':
            res = left_value >= right_value
        elif op == '<=':
            res = left_value <= right_value
        elif op == '==':
            res = left_value == right_value
        elif op == '!=':
            res = left_value != right_value
        else:
            raise Exception(f"Operación relacional desconocida: {op}")
        self.set_value(result_addr, res) # Almacenamos el valor en la locación del resultado

    def execute_assignment(self, value_addr, result_addr):
        """
        Función que asigna un valor a una nueva vvariable o constante
        :param value_addr: dirección dememoria del valor a asignar
        :param result_addr: dirección del asignado
        :return:
        """
        value = self.get_value(value_addr) # asignamos valor
        self.set_value(result_addr, value) # asignamos una dirección al nuevo valor

    def execute_write(self, value_addr):
        """
        Función que despliega un mensaje en la consola
        :param value_addr: dirección de memoria del valor a desplegar
        :return:
        """
        value = self.get_value(value_addr)
        # Si es una cadena, remover las comillas
        if isinstance(value, str) and value.startswith('"') and value.endswith('"'):
            value = value[1:-1]
        print(value)

    def execute_goto(self, target_addr):
        """
        Función que actualiza el pointer para saltar a un nuevo cuádruplo
        :param target_addr: dirección a la que nos tenemos que dirigir
        :return:
        """
        self.instruction_pointer = target_addr - 1  # -1 porque se incrementará después del retorno

    def execute_gotof(self, condition_addr, target_addr):
        """
        Función que evalua si una condición es falsa para saltar a la dirección de su cuádruplo correspondiente
        :param condition_addr: dirección de memoria del booleano a evaluar
        :param target_addr: dirección del cuádruplo siguiente
        :return:
        """
        condition = self.get_value(condition_addr) # Extraemos el valor
        if not condition: # Evaluamos que sea falso
            self.instruction_pointer = target_addr - 1  # -1 porque se incrementará después del retorno

    def execute_era(self, func_name):
        """
        Función que hace las preparaciones necesarias para saltar a una función
        :param func_name: nombre del funcion
        :return:
        """
        # Crear un nuevo contexto para la función
        new_context = {
            'local': {},  # Memoria local para la función
            'return_address': self.instruction_pointer + 1  # Dirección de retorno
        }
        # Agregar el nuevo contexto a la pila
        self.memory['stack'].append(new_context)

    def execute_gosub(self, func_name):
        """
        Función que mueve el IP a los cuartetos de la función
        :param func_name: nombre de la función
        :return:
        """
        func_address = self.get_function_address(func_name) # Obtenemos la dirección de la función
        if func_address is None: # Validamos la dirección
            raise Exception(f"Error: La función '{func_name}' no está definida.")
        # Establecer la memoria local al nuevo contexto
        current_context = self.memory['stack'][-1]
        self.memory['local'] = current_context['local']
        # Saltar a la dirección de inicio de la función
        self.instruction_pointer = func_address - 1  # -1 porque se incrementará después del retorno

    def execute_ret(self):
        """
        Función que verifica que se pueda regresar al main del programa y si sí, regresa el IP a su posición antes de
        saltar de función
        :return:
        """
        if not self.memory['stack']:
            raise Exception("Error: No hay contexto en la pila de ejecución.")
        # Eliminar el contexto actual
        last_context = self.memory['stack'].pop()
        # Restaurar el IP a la dirección de retorno
        self.instruction_pointer = last_context['return_address'] - 1  # -1 porque se incrementará después del retorno
        # Restaurar la memoria local al contexto previo
        if self.memory['stack']:
            # Si hay un contexto previo, restaurar su memoria local
            self.memory['local'] = self.memory['stack'][-1]['local']
        else:
            # Si no hay más contextos, limpiar la memoria local
            self.memory['local'] = {}

    def get_function_address(self, func_name):
        """
        Función que busca la dirección de una función
        :param func_name: nombre de la función
        :return: dirección de la función buscada
        """
        return self.function_addresses.get(func_name)

    def get_value(self, address):
        """
        Función que determina el segmento de la memoria donde se encuentra la variable o constante y obtiene su valor
        :param address: direccion de memoria del valor a buscar
        :return: valor de la variable | valor de la constante | Error
        """
        if self.is_constant_address(address): # Llamamos función auxiliar para identificar el segmento
            return self.memory['constants'].get(address, None)
        elif self.is_global_address(address):
            return self.memory['global'].get(address, None)
        elif self.is_local_address(address):
            return self.memory['local'].get(address, None)
        elif self.is_temporal_address(address):
            return self.memory['temporals'].get(address, None)
        else:
            raise Exception(f"Error: Dirección de memoria {address} inválida o no inicializada.")

    def set_value(self, address, value):
        """
        Función que determina el segmento de la memoria del ámbito donde se encuentra la variable o constante y asigna
        un valor en el segmento correspondiente
        :param address: dirección de memoria a asignar
        :param value: valor a asignar
        :return:
        """
        if self.is_constant_address(address): # Llamamos a una función auxiliar para identificar el segmento
            raise Exception(f"Error: No se puede modificar una constante en la dirección {address}.")
        elif self.is_global_address(address):
            self.memory['global'][address] = value
        elif self.is_local_address(address):
            self.memory['local'][address] = value
        elif self.is_temporal_address(address):
            self.memory['temporals'][address] = value
        else:
            raise Exception(f"Error: Dirección de memoria {address} inválida.")

    # Funciones auxiliares para determinar el segmento de memoria
    def is_constant_address(self, address):
        return 9000 <= address < 13000

    def is_global_address(self, address):
        return 1000 <= address < 5000

    def is_local_address(self, address):
        return 5000 <= address < 9000

    def is_temporal_address(self, address):
        return 13000 <= address < 16000
