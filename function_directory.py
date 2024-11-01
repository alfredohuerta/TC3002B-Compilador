class FunctionDirectory:
    def __init__(self):
        # Diccionario que almacena las funciones
        # Clave: nombre de la función
        # Valor: diccionario con información de la función
        self.functions = {}

    def add_function(self, name, return_type, parameters):
        if name in self.functions:
            raise Exception(f"Error: La función '{name}' ya ha sido declarada.")
        else:
            # Cada función tiene su propia tabla de variables locales
            self.functions[name] = {
                'return_type': return_type,
                'parameters': parameters,  # Lista de parámetros [(nombre, tipo)]
                'variables': {},  # Tabla de variables locales
            }

    def get_function(self, name):
        return self.functions.get(name, None)

    def add_variable_to_function(self, func_name, var_name, var_type):
        function = self.get_function(func_name)
        if function:
            if var_name in function['variables']:
                raise Exception(f"Error: La variable '{var_name}' ya ha sido declarada en la función '{func_name}'.")
            else:
                function['variables'][var_name] = {
                    'type': var_type,
                }
        else:
            raise Exception(f"Error: La función '{func_name}' no está definida.")

    def variable_exists_in_function(self, func_name, var_name):
        function = self.get_function(func_name)
        if function:
            return var_name in function['variables']
        else:
            return False
