class VariableTable:
    def __init__(self):
        # Diccionario de variables globales
        # Clave: nombre de la variable
        # Valor: diccionario con información de la variable
        self.variables = {}

    def add_variable(self, name, var_type, scope):
        if name in self.variables:
            raise Exception(f"Error: La variable '{name}' ya ha sido declarada en el ámbito '{scope}'.")
        else:
            self.variables[name] = {
                'type': var_type,
                'scope': scope,
            }

    def get_variable(self, name):
        return self.variables.get(name, None)
