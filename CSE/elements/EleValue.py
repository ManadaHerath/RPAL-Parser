from .EleValueOrTuple import EleValueOrTuple
from INTERPRETER.Node import Node

class EleValue(EleValueOrTuple):
    def __init__(self, type, value=None):
        # Initialize with type and optional value
        if isinstance(type, str):
            super().__init__(type)
            self.value = value  # Set value if type is string
        if isinstance(type, Node):
            super().__init__(type.getLabel())
            self.value = type.getValue()  # Set value from Node

    def getValue(self):
        # Get the value of this element
        return self.value

    def equals(self, o):
        # Check if two objects are equal
        if self is o:
            return True  # Same reference
        if o is None or self.__class__ != o.__class__:
            return False  # Different class or None
        return self.value == o.value  # Compare values

    def hashCode(self):
        # Get the hash code of the value
        return hash(self.value)

    def toString(self):
        # Convert to string
        if self.value is None:
            return self.getLabel()  # Return label if no value
        return f"{self.getLabel()}({self.getValue()})"  # Format with label and value
