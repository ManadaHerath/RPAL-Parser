from .ASTNode import nodeTypes

class AST:
    def __init__(self,root) -> None:
        if root is None:
            raise ValueError("Root node can't be None")
        self.text=""
        self.root=root

    def getAST(self):
       self.preOrder(self.root,"")
       return self.text

    def preOrder(self,node,printPrefix):
        if node is None:
            return
        self.addNodeDetails(node,printPrefix)
        self.preOrder(node.getChild(),printPrefix+".")
        self.preOrder(node.getSibling(),printPrefix)

    def addNodeDetails(self,node,printPrefix):
        if node is None:
            raise ValueError("Node can't be None")
        if node.getType() is None:
            raise ValueError("Node type can't be None")
        # print("tempdddddd",node.getType())
        if node.getType()[0]==nodeTypes["IDENTIFIER"][0] or node.getType()[0]==nodeTypes["INTEGER"][0]:
            if node.getValue() is None:
                raise ValueError("Node value can't be None")
            string=str(printPrefix+node.getPrintName()+"\n") % (node.getValue())
            self.text+=string
        elif node.getType()[0]==nodeTypes["STRING"][0]:
            if node.getValue() is None:
                raise ValueError("Node value can't be None")
            string=str(printPrefix+node.getPrintName()+"\n") % (node.getValue())
            self.text+=string
        else:
            self.text+=printPrefix+node.getPrintName()+"\n"