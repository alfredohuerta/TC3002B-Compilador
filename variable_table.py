class VariableTable:
    """
    Esta clase maneja la tabla de variables que genera un registro de las variables identificadas en el árbol dado por el
    parser. Esta tabla registra las características de la variable en un diccionario que usa como llave el nombre de la
    variable, el ámbito de las variables puede variar entre global y local dependiendo de dónde se encuentren en el código
    """
    def __init__(self, base_address=0):
        self.variables = {} # Inicializamos el diccionario que contiene la tabla de variables y sigue la
                            # estructura: {name: {type, scope, address}}
        self.counters = { # Inicializamos los contadores por tipo para llevar el registro de las variables agregadas
            'int': 0,
            'float': 0,
            'bool': 0
        }
        self.base_addresses = { # Inicializamos las direcciones base por tipo
            'int': base_address,
            'float': base_address + 1000,
            'bool': base_address + 2000
        }

    def add_variable(self, name, var_type, scope):
        """
        Función para agregar una nueva variable a la tabla, asignándole tipo, alcance y dirección virtual
        :param name: nombre de la variable
        :param var_type: tipo de variable (int, float, bool)
        :param scope: ámbito de la variable (global, local)
        :return:
        """
        if name in self.variables: # Comprobamos que no se haya registrado previamente la variable
            raise Exception(f"Error: La variable '{name}' ya ha sido declarada.")
        else:
            address = self.base_addresses[var_type] + self.counters[var_type] # calculamos la dirección de la nueva variable
            self.counters[var_type] += 1 # Añadimos al contador
            self.variables[name] = { # Agregamos una nueva entrada al diccionario usando el nombre como clave
                'type': var_type,
                'scope': scope,
                'address': address
            }

    def get_variable(self, name):
        """
        Función para obtener la información de una variable ya declarada a través de su nombre.
        :param name: Nombre de la variable a buscar en el diccionario
        :returns: Diccionario con la información de la variable | None en caso de que la variable no exista
        """
        return self.variables.get(name, None)
