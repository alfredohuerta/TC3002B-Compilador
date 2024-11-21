from variable_table import VariableTable # Importamos la tabla de variables para administrar los parámetros de las
                                         # funciones y generamos una tabla de variables locales para cada una de las funciones

class FunctionDirectory:
    """
    Esta clase ayuda a administrar una estructura que almacena la información de cada función en el programa, incluídas
    las variables locales que se generen y los parámetros que se declaren
    """
    def __init__(self):
        self.functions = {} # Inicializamos el diccionario de las funciones con esta estructura
                            # {nombre: {return, parámetros: {(nombre, tipo)}, {tabla de variables}}}

    def add_function(self, name, return_type, parameters):
        """
        Función que agrega una nueva función a la tabla de funciones
        :param name: nombre de la función
        :param return_type: Tipo de retorno de la función (está hardcodeado a void)
        :param parameters: lista de parámetros de la función en forma de tupla
        :return:
        """
        if name in self.functions: # Comprueba si el nombre de la función ya existe en el directorio
            raise Exception(f"Error: La función '{name}' ya ha sido declarada.")
        else: # Registra la nueva función en el directorio
            self.functions[name] = { # Creamos la entrada en el diccionario
                'return_type': return_type,
                'parameters': parameters,  # Lista de parámetros [(nombre, tipo)]
                'variables': VariableTable(base_address=5000),  # Cada función tiene su propia tabla de variables
                                                                # locales mientras que sus direcciones base empiezan en 5000
            }

    def get_function(self, name):
        """
        Función que recupera la información de una función usando el método GET
        :param name: nombre de la función que se usa como llave en el directorio
        :return: Información de la función | None en caso de que la función no exita
        """
        return self.functions.get(name, None)

    def add_variable_to_function(self, func_name, var_name, var_type):
        """
        Función que añade una variable local a una función en específico
        :param func_name: Nombre de la función donde se añadirá la variable local
        :param var_name: Nombre de la variable
        :param var_type: Tipo de variable
        :return:
        """
        function = self.get_function(func_name)
        if function:
            function['variables'].add_variable(var_name, var_type, 'local')
        else:
            raise Exception(f"Error: La función '{func_name}' no está definida.")

    def variable_exists_in_function(self, func_name, var_name):
        """
        Función auxiliar que identifica si una variable existe o no en una función
        :param func_name: Nombre de la función
        :param var_name: Nombre de la variable a buscar
        :return: Booleano si la variable existe o no
        """
        function = self.get_function(func_name) # Obtenemos toda la información de la función
        if function: # Si los datos sin válidos, recorremos la función buscando la variable por su nombre
            return var_name in function['variables'].variables
        else: # Si no existe, regresa falso
            return False

    def get_variable_from_function(self, func_name, var_name):
        """
        Función que busca obtener la información de una variable en específico en el directorio
        :param func_name: nombre de la función donde se hace la búsqueda
        :param var_name: nombre de la variable a buscar
        :return:
        """
        function = self.get_function(func_name) # Obtenenmos todos los datos de la función
        if function: # Si los datos son válidos, llamamos a la tabla de variables para obtener los datos de la variable
            return function['variables'].get_variable(var_name)
        else: # Si los datos no son válidos regresa nulo
            return None
