from variable_table import VariableTable

class FunctionDirectory:
    def __init__(self):
        self.functions = {}

    def add_function(self, name, return_type, parameters):
        if name in self.functions:
            raise Exception(f"Error: La función '{name}' ya ha sido declarada.")
        else:
            # Cada función tiene su propia tabla de variables locales
            self.functions[name] = {
                'return_type': return_type,
                'parameters': parameters,  # Lista de parámetros [(nombre, tipo)]
                'variables': VariableTable(base_address=5000),  # Direcciones locales empiezan en 5000
            }

    def get_function(self, name):
        return self.functions.get(name, None)

    def add_variable_to_function(self, func_name, var_name, var_type):
        function = self.get_function(func_name)
        if function:
            function['variables'].add_variable(var_name, var_type, 'local')
        else:
            raise Exception(f"Error: La función '{func_name}' no está definida.")

    def variable_exists_in_function(self, func_name, var_name):
        function = self.get_function(func_name)
        if function:
            return var_name in function['variables'].variables
        else:
            return False

    def get_variable_from_function(self, func_name, var_name):
        function = self.get_function(func_name)
        if function:
            return function['variables'].get_variable(var_name)
        else:
            return None
