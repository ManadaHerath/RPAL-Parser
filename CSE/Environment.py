from .elements.EleValueOrTuple import EleValueOrTuple

class Environment:
    def __init__(self, parent=None, key=None, value=None):
        # Initialize Environment
        self.parent = parent
        self.memory = {}
            
        if key is None and value is None:
            self.initializePrimaryEnv()  # Initialize primary environment with predefined values
        elif key and value:
            self.remember(key, value)  # Remember key-value pair if provided

    def initializePrimaryEnv(self):
        # Initialize primary environment with predefined values
        self.remember("Print", None)
        self.remember("Isstring", None)
        self.remember("Isinteger", None)
        self.remember("Istruthvalue", None)
        self.remember("Istuple", None)
        self.remember("Isfunction", None)
        self.remember("Null", None)
        self.remember("Order", None)
        self.remember("Stern", None)
        self.remember("Stem", None)
        self.remember("ItoS", None)
        self.remember("neg", None)
        self.remember("not", None)
        self.remember("Conc", None)

    def remember(self, key, value):
        # Remember a variable in the environment
        if key in self.memory:
            raise RuntimeError("Variable is already defined: " + key)
        self.memory[key] = value

    def lookup(self, id):
        # Look up a variable in the environment
        if id in self.memory:
            return self.memory[id]
        if self.parent is None:
            raise RuntimeError("Undefined variable: " + id)
        return self.parent.lookup(id)

    def toString(self):
        # Convert environment to string
        if self.parent is not None:
            data = [f"[{self.memory[key]}/{key}]" for key in self.memory]
            return str(self.parent) + " > " + "".join(data)
        return "PE"
