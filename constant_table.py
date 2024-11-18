class ConstantTable:
    def __init__(self):
        self.constants = {}
        self.counters = {
            'int': 0,
            'float': 0,
            'bool': 0,
            'string': 0
        }
        self.base_addresses = {
            'int': 9000,
            'float': 10000,
            'bool': 11000,
            'string': 12000
        }

    def add_constant(self, value, const_type):
        if value in self.constants:
            return self.constants[value]['address']
        else:
            address = self.base_addresses[const_type] + self.counters[const_type]
            self.counters[const_type] += 1
            self.constants[value] = {
                'type': const_type,
                'address': address
            }
            return address

    def get_constant(self, value):
        return self.constants.get(value, None)
