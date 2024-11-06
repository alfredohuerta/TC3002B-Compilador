class Cube:
    def __init__(self):
        # Cubo semántico como un diccionario anidado

        self.cube = {
            # Operación
            '+': { # Suma
                # Tipo de operando : {Tipo de operando: Resultado | Tipo de operando: Error}
                'int': {'int': 'int', 'float': 'float', 'bool': 'error'},
                'float': {'int': 'float', 'float': 'float', 'bool': 'error'},
                'bool': {'int': 'error', 'float': 'error', 'bool': 'error'}
            },
            '-': { # Resta
                'int': {'int': 'int', 'float': 'float', 'bool': 'error'},
                'float': {'int': 'float', 'float': 'float', 'bool': 'error'},
                'bool': {'int': 'error', 'float': 'error', 'bool': 'error'}
            },
            '*': { # Multiplicación
                'int': {'int': 'int', 'float': 'float', 'bool': 'error'},
                'float': {'int': 'float', 'float': 'float', 'bool': 'error'},
                'bool': {'int': 'error', 'float': 'error', 'bool': 'error'}
            },
            '/': { # División
                'int': {'int': 'float', 'float': 'float', 'bool': 'error'},
                'float': {'int': 'float', 'float': 'float', 'bool': 'error'},
                'bool': {'int': 'error', 'float': 'error', 'bool': 'error'}
            },
            '=': {
                'int': {'int': 'int', 'float': 'error', 'bool': 'error'},
                'float': {'int': 'float', 'float': 'float', 'bool': 'error'},
                'bool': {'int': 'error', 'float': 'error', 'bool': 'bool'}
            },
            '==': {
                'int': {'int': 'bool', 'float': 'bool', 'bool': 'error'},
                'float': {'int': 'bool', 'float': 'bool', 'bool': 'error'},
                'bool': {'int': 'error', 'float': 'error', 'bool': 'bool'}
            },
            '!=': {
                'int': {'int': 'bool', 'float': 'bool', 'bool': 'error'},
                'float': {'int': 'bool', 'float': 'bool', 'bool': 'error'},
                'bool': {'int': 'error', 'float': 'error', 'bool': 'bool'}
            },
            '<': {
                'int': {'int': 'bool', 'float': 'bool', 'bool': 'error'},
                'float': {'int': 'bool', 'float': 'bool', 'bool': 'error'},
                'bool': {'int': 'error', 'float': 'error', 'bool': 'error'}
            },
            '<=': {
                'int': {'int': 'bool', 'float': 'bool', 'bool': 'error'},
                'float': {'int': 'bool', 'float': 'bool', 'bool': 'error'},
                'bool': {'int': 'error', 'float': 'error', 'bool': 'error'}
            },
            '>': {
                'int': {'int': 'bool', 'float': 'bool', 'bool': 'error'},
                'float': {'int': 'bool', 'float': 'bool', 'bool': 'error'},
                'bool': {'int': 'error', 'float': 'error', 'bool': 'error'}
            },
            '>=': {
                'int': {'int': 'bool', 'float': 'bool', 'bool': 'error'},
                'float': {'int': 'bool', 'float': 'bool', 'bool': 'error'},
                'bool': {'int': 'error', 'float': 'error', 'bool': 'error'}
            },
            '&&': {
                'bool': {'bool': 'bool', 'int': 'error', 'float': 'error'},
                'int': {'bool': 'error', 'int': 'error', 'float': 'error'},
                'float': {'bool': 'error', 'int': 'error', 'float': 'error'}
            },
            '||': {
                'bool': {'bool': 'bool', 'int': 'error', 'float': 'error'},
                'int': {'bool': 'error', 'int': 'error', 'float': 'error'},
                'float': {'bool': 'error', 'int': 'error', 'float': 'error'}
            }
        }

    def get_result_type(self, operation, type1, type2):
        return self.cube.get(operation, {}).get(type1, {}).get(type2, 'error')