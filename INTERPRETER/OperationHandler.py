from CSE.elements.EleValue import EleValue
from CSE.elements.EleTuple import EleTuple

from Exception import Exception


class OperationHandler:
    def extract(self, operation, operand):
        # Extracts the tuple element based on the index provided by the operand
        if isinstance(operand, EleValue) and operand.isLabel("int"):
            index = int(operand.getValue())
            return operation.getValue()[index - 1]
        raise RuntimeError("Index of the tuple should be integer.")

    def checkMathematicalOperation(self, op):
        # Checks if the operation is a mathematical operation
        operationsMathematical = [
            "+", "-", "/", "*", "**", "eq", "ne", "gr", "ge", "le", ">", "<", ">=", "<=", "or", "&", "aug", "ls"
        ]
        for binaryOp in operationsMathematical:
            if op.isLabel(binaryOp):
                return True
        return False

    def checkArrayOperation(self, op):
        # Checks if the operation is an array operation
        operationsArray = [
            "Print", "Isstring", "Isinteger", "Istruthvalue", "Isfunction", "Null", "Istuple", "Order", "Stern",
            "Stem", "ItoS", "neg", "not", "$ConcPartial"
        ]
        for unaryOp in operationsArray:
            if op.isLabel(unaryOp):
                return True
        return False

    def applyOperations(self, operation, operand1, operand2):
        # Applies binary operations like addition, subtraction, etc.
        operatorLabel = operation.getLabel()
        if operatorLabel == "+":
            return self.numericalOperator(operand1, operand2, lambda a, b: a + b)
        elif operatorLabel == "-":
            return self.numericalOperator(operand1, operand2, lambda a, b: a - b)
        elif operatorLabel == "*":
            return self.numericalOperator(operand1, operand2, lambda a, b: a * b)
        elif operatorLabel == "**":
            return self.numericalOperator(operand1, operand2, lambda a, b: int(a ** b))
        elif operatorLabel == "/":
            return self.numericalOperator(operand1, operand2, lambda a, b: a / b)
        elif operatorLabel == "or":
            return self.binaryBooleanOperator(operand1, operand2, lambda a, b: a or b)
        elif operatorLabel == "&":
            return self.binaryBooleanOperator(operand1, operand2, lambda a, b: a and b)
        elif operatorLabel == "eq":
            return self.booleanCondition(operand1 == operand2)
        elif operatorLabel == "ne":
            return self.notOperator(self.booleanCondition(operand1 == operand2))
        elif operatorLabel in [">", "gr"]:
            return self.greater(operand1, operand2)
        elif operatorLabel in ["<", "ls"]:
            return self.notOperator(self.greater(operand1, operand2))
        elif operatorLabel in [">=", "ge"]:
            return self.orOperator(self.greater(operand1, operand2), self.booleanCondition(operand1 == operand2))
        elif operatorLabel in ["<=", "le"]:
            return self.orOperator(self.notOperator(self.greater(operand1, operand2)), self.booleanCondition(operand1 == operand2))
        elif operatorLabel == "aug":
            return self.aug(operand1, operand2)
        else:
            raise Exception("Unknown operator: " + operation)

    def apply(self, operation, operand):
        # Applies unary operations like Print, Isstring, Isinteger, etc.
        operatorLabel = operation.getLabel()
        if operatorLabel == "Print":
            print(self.covertToString(operand))
            return EleValue("dummy")
        elif operatorLabel == "Isstring":
            return self.booleanCondition(operand.isLabel("str"))
        elif operatorLabel == "Isinteger":
            return self.booleanCondition(operand.isLabel("int"))
        elif operatorLabel == "Istruthvalue":
            return self.booleanCondition(operand.isLabel("true") or operand.isLabel("false"))
        elif operatorLabel == "Istuple":
            return self.booleanCondition(operand.isLabel("tuple"))
        elif operatorLabel == "Isfunction":
            return self.booleanCondition(operand.isLabel("lambda"))
        elif operatorLabel == "Order":
            return self.order(operand)
        elif operatorLabel == "Null":
            return self.booleanCondition(operand.isLabel("nil"))
        elif operatorLabel == "Stern":
            return self.stern(operand)
        elif operatorLabel == "Stem":
            return self.stem(operand)
        elif operatorLabel == "Conc":
            return self.conc(operand)
        elif operatorLabel == "$ConcPartial":
            return self.concPartial(operation, operand)
        elif operatorLabel == "ItoS":
            return self.iToS(operand)
        elif operatorLabel == "neg":
            return self.numericalOperator(EleValue("int", "-1"), operand, lambda a, b: a * b)
        elif operatorLabel == "not":
            return self.notOperator(operand)
        elif operatorLabel == "tuple":
            return self.extract(operation, operand)
        else:
            raise Exception("Unknown variable for CSE machine: " + operation)

    def numericalOperator(self, operand1, operand2, operation):
        # Performs numerical operations on two operands
        if isinstance(operand1, EleValue) and isinstance(operand2, EleValue):
            if operand1.isLabel("int") and operand2.isLabel("int"):
                value1 = int(operand1.getValue())
                value2 = int(operand2.getValue())
                result = operation(value1, value2)
                return EleValue("int", str(result))
        raise RuntimeError("Numerical operator expects both operands to be integers.")

    def binaryBooleanOperator(self, operand1, operand2, operation):
        # Performs binary boolean operations on two operands
        if self.booleanCondition(operand1.isLabel("true") or operand1.isLabel("false")) and self.booleanCondition(operand2.isLabel("true") or operand2.isLabel("false")):
            element1 = operand1.isLabel("true")
            element2 = operand2.isLabel("true")
            return self.booleanCondition(operation(element1, element2))
        raise RuntimeError("Or operator can only be applied to truth values.")

    def covertToString(self, element):
        # Converts an element to its string representation
        if isinstance(element, EleTuple):
            subElements = element.getValue()
            data = [self.covertToString(subElement) for subElement in subElements]
            return "(" + ", ".join(data) + ")"
        elif isinstance(element, EleValue):
            if element.isLabel("lambda"):
                kAndXAndC = element.getValue().split(" ")
                k = kAndXAndC[0]
                x = kAndXAndC[1]
                return "[lambda closure: {}: {}]".format(x, k)
            elif element.isLabel("str") or element.isLabel("int"):
                return element.getValue()
            else:
                return element.getLabel()
        else:
            raise Exception("Unknown element type encountered.")

    def booleanCondition(self, condition):
        # Returns a boolean EleValue based on the condition
        if condition:
            return EleValue("true")
        return EleValue("false")

    def getSubString(self, operand, operation):
        # Gets a substring of a string operand
        if isinstance(operand, EleValue) and operand.isLabel("str"):
            string = operand.getValue()
            if not string:
                return EleValue("str", "")
            stern = operation(string)
            return EleValue("str", stern)
        raise RuntimeError("Substring operations can only be applied to strings.")

    def order(self, operand):
        # Returns the order of a tuple operand
        if isinstance(operand, EleTuple):
            elements = len(operand.getValue())
            return EleValue("int", str(elements))
        raise RuntimeError("Order operation can only be applied to tuples")

    def stern(self, operand):
        # Returns the stern (substring starting from the second character) of a string operand
        return self.getSubString(operand, lambda s: s[1:])

    def stem(self, operand):
        # Returns the stem (first character) of a string operand
        return self.getSubString(operand, lambda s: s[0])

    def conc(self, operand):
        # Concatenates two string operands
        if isinstance(operand, EleValue) and operand.isLabel("str"):
            return EleValue("$ConcPartial", operand.getValue())
        raise RuntimeError("Conc operation can only be applied to strings.")

    def concPartial(self, operator, operand2):
        # Partial concatenation of string operands
        if isinstance(operator, EleValue) and isinstance(operand2, EleValue):
            if operator.isLabel("$ConcPartial") and operand2.isLabel("str"):
                string = operator.getValue() + operand2.getValue()
                return EleValue("str", string)
        raise RuntimeError("Invalid application of Conc operation.")

    def iToS(self, operand):
        # Converts an integer operand to a string
        if isinstance(operand, EleValue) and operand.isLabel("int"):
            value = operand.getValue()
            return EleValue("str", value)
        raise RuntimeError("iToS operation can only be applied to integers.")

    def notOperator(self, operand):
        # Performs logical NOT operation on a boolean operand
        if self.booleanCondition(operand.isLabel("true") or operand.isLabel("false")):
            return self.booleanCondition(operand.isLabel("false"))
        raise RuntimeError("Not operator can only be applied to truth values.")

    def orOperator(self, operand1, operand2):
        # Performs logical OR operation on two boolean operands
        return self.binaryBooleanOperator(operand1, operand2, lambda a, b: a or b)

    def greater(self, operand1, operand2):
        # Checks if operand1 is greater than operand2
        if isinstance(operand1, EleValue) and isinstance(operand2, EleValue):
            if operand1.isLabel("int") and operand2.isLabel("int"):
                value1 = int(operand1.getValue())
                value2 = int(operand2.getValue())
                condition = value1 > value2
                return self.booleanCondition(condition)
            elif operand1.isLabel("str") and operand2.isLabel("str"):
                value1 = operand1.getValue()
                value2 = operand2.getValue()
                condition = value1 > value2
                return self.booleanCondition(condition)
        raise RuntimeError("Operands must be of compatible types.")

    def aug(self, operand1, operand2):
        # Augments a tuple with another element
        if operand1.isLabel("nil"):
            operand1 = EleTuple(())
        if isinstance(operand1, EleTuple):
            op1Tuple = operand1.getValue()
            combined = op1Tuple + (operand2,)
            return EleTuple(combined)
        raise RuntimeError("Augmentation can only be applied to tuples.")
