
from INTERPRETER.createTree import CreateTree
from INTERPRETER.ASTtoST import AstToSt
from parser1 import Parser
from Exception import Exception
from CSE.CSEMachine import CSEMachine
from CSE.ElementParser import ElementParser
from lexicon import *


import sys

if __name__ == "__main__":
    astVisible=False
    
    params=sys.argv[1:]
    if len(params)==1:
        path=params[0]
    elif len(params) ==2 and params[0]=="--ast":
        astVisible=True
        path=params[1]
     
    tokens=[]
    with open(path, "r") as file:

        try:
            lines=file.readlines()
            tokens=get_next_token(lines,tokens)
            pasrser = Parser(tokens)
            ast=pasrser.buildAst()

            if astVisible:    
               print(ast.getAST())
               print("")
            

            text =ast.getAST().split("\n")
            root=CreateTree().nodeFromFile(text)
            AstToSt().astToSt(root)
            controls=ElementParser().generateCs(root)
            cseMachine=CSEMachine(controls)
            cseMachine.evaluateTree()

       
        except Exception as e:
            print("Custom Exception:", e.message)
        except Exception as e:
            print("Custom Exception:", e.message)
        except Exception as e:
            print("Custom Exception:", e.message)
        except RuntimeError as e:
            print("Custom Exception:", e.message)
        
