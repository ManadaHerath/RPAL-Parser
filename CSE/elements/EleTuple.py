from .EleValueOrTuple import EleValueOrTuple

class EleTuple(EleValueOrTuple):
    def __init__(self, value):
        """Initialize an EleTuple instance with a tuple value."""
        super().__init__("tuple")  # Call the parent class constructor with "tuple" as the type
        self.value = value  # Set the value of the tuple

    def getValue(self):
        """Return the value of the tuple."""
        return self.value

    def equals(self, o):
        """Check if this instance is equal to another instance."""
        if self is o:
            return True  # If both references are the same, return True
        if o is None or self.__class__ != o.__class__:
            return False  # If the other object is None or not of the same class, return False
        return self.value == o.value  # Compare the tuple values

    def hashCode(self):
        """Return the hash code of the tuple."""
        return hash(tuple(self.value))  # Compute and return the hash of the tuple value

    def toString(self):
        """Return the string representation of the tuple."""
        return str(self.value)  # Convert the tuple value to a string and return it
