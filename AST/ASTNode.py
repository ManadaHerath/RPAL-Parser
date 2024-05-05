nodeTypes = {
    "IDENTIFIER": ["IDENTIFIER", "<ID:%s>"],
    "STRING": ["STRING", "<STR:%s>"],
    "INTEGER": ["INTEGER", "<INT:%s>"],
    "LET": ["LET", "let"],
    "LAMBDA": ["LAMBDA", "lambda"],
    "WHERE": ["WHERE", "where"],
    "TAU": ["TAU", "tau"],
    "AUG": ["AUG", "aug"],
    "CONDITIONAL": ["CONDITIONAL", "->"],
    "OR": ["OR", "or"],
    "AND": ["AND", "&"],
    "NOT": ["NOT", "not"],
    "GR": ["GR", "gr"],
    "GE": ["GE", "ge"],
    "LS": ["LS", "ls"],
    "LE": ["LE", "le"],
    "EQ": ["EQ", "eq"],
    "NE": ["NE", "ne"],
    "PLUS": ["PLUS", "+"],
    "MINUS": ["MINUS", "-"],
    "NEG": ["NEG", "neg"],
    "MULT": ["MULT", "*"],
    "DIV": ["DIV", "/"],
    "EXP": ["EXP", "**"],
    "AT": ["AT", "@"],
    "GAMMA": ["GAMMA", "gamma"],
    "TRUE": ["TRUE", "<true>"],
    "FALSE": ["FALSE", "<false>"],
    "NIL": ["NIL", "<nil>"],
    "DUMMY": ["DUMMY", "<dummy>"],
    "WITHIN": ["WITHIN", "within"],
    "SIMULTDEF": ["SIMULTDEF", "and"],
    "REC": ["REC", "rec"],
    "EQUAL": ["EQUAL", "="],
    "FCNFORM": ["FCNFORM", "function_form"],
    "PAREN": ["PAREN", "<()>"],
    "COMMA": ["COMMA", ","],
    "YSTAR": ["YSTAR", "<Y*>"],
    "BETA": ["BETA", ""],
    "DELTA": ["DELTA", ""],
    "ETA": ["ETA", ""],
    "TUPLE": ["TUPLE", ""]
}


class ASTNode:
    def __init__(self) -> None:
        self.type=None
        self.value=None
        self.child=None
        self.sibling=None
        self.sourceLineNumber=None
    
    def getName(self):
        if self.type is None:
            raise ValueError("Type can't be None")
        return self.type[0]     #ast node type name

    def getPrintName(self):
        if self.type is None:
            raise ValueError("Type can't be None")
        return self.type[1]    

    def getType(self):
        return self.type

    def setType(self,type):
        if type is None:
            raise ValueError("Type can't be None")
        self.type=type

    def getChild(self):
        return self.child

    def setChild(self,child):
        if child is None:
            raise ValueError("Child can't be None")
        self.child=child

    def getSibling(self):
        return self.sibling

    def setSibling(self,sibling):
        if sibling is None:
            raise ValueError("Sibling can't be None")
        self.sibling=sibling

    def getValue(self):
        return self.value

    def setValue(self,value):
        if value is None:
            raise ValueError("Value can't be None")
        self.value=value

    def getSourceLineNumber(self):
        return self.sourceLineNumber

    def setSourceLineNumber(self,sourceLineNumber):
        if sourceLineNumber is None:
            raise ValueError("Source line number can't be None")
        self.sourceLineNumber=sourceLineNumber
        
        
        

