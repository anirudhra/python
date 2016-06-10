#############################################################################
### Python module implementing a generic node for tree/linked list etc.
#############################################################################

class Node:
    """Node Class for constructing trees"""

    def __init__(self, num):
        """ Constructor """
        self.__parent = -1
        self.__children = []
        self.__nodeNum = num
        self.__data = "White"

    def set_data(self, data):
        """ Sets data field of node """
        self.__data = data

    def get_data(self):
        """ Returns data field of node """
        return self.__data

    def get_nodeNum(self):
        """ Returns self node number """
        return self.__nodeNum

    def set_parent(self, node):
        """ Sets parent node number """
        self.__parent = node.get_nodeNum()

    def get_parent(self):
        """ Returns parent's node number """
        # -1 indicates root node
        return self.__parent

    def set_children(self, children):
        """ Sets children """
        # if input arg isn't a list, convert to one
        if type(children) is not list:
            children = [children]

        # set children node, as well as set their parent correctly
        for child in children:
            child.set_parent(self)
            self.__children.append(child.get_nodeNum())

    def get_children(self):
        return self.__children

    def __str__(self):
        """ Returns node relevant data """
        return "Node: "+str(self.get_nodeNum())+", Data: "+str(self.get_data())+", Parent: "+str(self.get_parent())+", Children: "+str(self.get_children())


#############################################################################
