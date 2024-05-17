from .ASTNode import nodeTypes

class AST:
    def __init__(self, root) -> None:
        """Initialize the AST with a root node."""
        if root is None:
            raise ValueError("Root node can't be None")
        self.text = ""  # Initialize an empty string to store the AST text
        self.root = root  # Set the root of the AST

    def getAST(self):
        """Return the string representation of the AST."""
        self.preOrder(self.root, "")  # Perform a pre-order traversal starting from the root
        return self.text  # Return the accumulated text

    def preOrder(self, node, printPrefix):
        """Perform a pre-order traversal of the AST."""
        if node is None:
            return  # Base case: if the node is None, return
        self.addNodeDetails(node, printPrefix)  # Add the current node's details to the text
        self.preOrder(node.getChild(), printPrefix + ".")  # Recursively traverse the child node with updated prefix
        self.preOrder(node.getSibling(), printPrefix)  # Recursively traverse the sibling node with the same prefix

    def addNodeDetails(self, node, printPrefix):
        """Add details of a node to the text."""
        if node is None:
            raise ValueError("Node can't be None")  # Node should not be None
        if node.getType() is None:
            raise ValueError("Node type can't be None")  # Node type should not be None

        # If node is an identifier or an integer
        if node.getType()[0] == nodeTypes["IDENTIFIER"][0] or node.getType()[0] == nodeTypes["INTEGER"][0]:
            if node.getValue() is None:
                raise ValueError("Node value can't be None")  # Node value should not be None
            string = str(printPrefix + node.getPrintName() + "\n") % (node.getValue())  # Format the string with node value
            self.text += string  # Add the formatted string to the text

        # If node is a string
        elif node.getType()[0] == nodeTypes["STRING"][0]:
            if node.getValue() is None:
                raise ValueError("Node value can't be None")  # Node value should not be None
            string = str(printPrefix + node.getPrintName() + "\n") % (node.getValue())  # Format the string with node value
            self.text += string  # Add the formatted string to the text

        # For other node types
        else:
            self.text += printPrefix + node.getPrintName() + "\n"  # Add the node's print name to the text
