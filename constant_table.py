class ConstantTable:
    """
    Esta clase genera la tabla de constantes, similar a la tabla de variables almacena los datos de las contantes en un
    diccionario que usa como llave al valor de la constante, asigna valores de memoria a las constantes, además de que
    aquí almacenamos los strings de los letreros
    """
    def __init__(self):
        self.constants = {} # Inicializamos el diccionario que tendrá la información de las constantes siguiendo la
                            # estructura: {value: {type, address}}
        self.counters = { # Inicializamos los contadores de las constantes
            'int': 0,
            'float': 0,
            'bool': 0,
            'string': 0 # Esto solo se usa para administrar los letreros en el código
        }
        self.base_addresses = { # Asignamos direcciones base virtuales a las constantes
            'int': 9000,
            'float': 10000,
            'bool': 11000,
            'string': 12000
        }

    def add_constant(self, value, const_type):
        """
        Función que agrega una constante a la tabla de constantes si es que no existe para asignar una dirección virtual
        o devuelve la dirección en caso de que ya haya sido registrada
        :param value: valor de la constante
        :param const_type: tipo de constante
        :return: dirección de memoria virtual de la constante
        """
        if value in self.constants: # Identificamos si esta constante ya ha sido declarada
            return self.constants[value]['address'] # Regresamos la dirección de la constante
        else: # Registramosd la constante
            address = self.base_addresses[const_type] + self.counters[const_type] # Generamos una dirección a la constante
            self.counters[const_type] += 1 # Aumentamos el contador de la constante
            self.constants[value] = { # Construimos la entrada en el diccionario usando de llave el valor de la constante
                'type': const_type,
                'address': address
            }
            return address # Regresamos la dirección de la nueva constante

    def get_constant(self, value):
        """
        Función que obtiene la información de una constante previamente almacenada en la tabla de constantes
        :param value: Valor de la constante que se quiere buscar
        :return: valor de la constante en la tabla de constantes | None si no existe
        """
        return self.constants.get(value, None)
