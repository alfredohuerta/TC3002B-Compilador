class VariableTable:
    def __init__(self, base_address=0):
        self.variables = {}
        self.counters = {
            'int': 0,
            'float': 0,
            'bool': 0,
            'string': 0
        }
        self.base_addresses = {
            'int': base_address,
            'float': base_address + 1000,
            'bool': base_address + 2000,
            'string': base_address + 3000
        }

    def add_variable(self, name, var_type, scope):
        if name in self.variables:
            raise Exception(f"Error: La variable '{name}' ya ha sido declarada.")
        else:
            address = self.base_addresses[var_type] + self.counters[var_type]
            self.counters[var_type] += 1
            self.variables[name] = {
                'type': var_type,
                'scope': scope,
                'address': address
            }

    def get_variable(self, name):
        return self.variables.get(name, None)
