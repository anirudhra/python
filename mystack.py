#############################################################################
### Python mmodule implementing stack
#############################################################################
class Stack:

    """ Stack class """

    def __init__(self, size = 0):
        """ Constructor, if size == 0, stack is infinite """
        self.__entries = []
        self.__size = size

    def push(self, data):
        """ pushes data in to stack """
        if (self.is_full() == False):
            self.__entries.append(data)
            print "Pushed: ",data

    def is_full(self):
        """ Check for full only if size != 0 """
        ret = False
        if self.__size > 0:
            ret = (len(self.__entries) == self.__size)
        return ret

    def is_empty(self):
        return (len(self.__entries) == 0)

    def pop(self):
        """ pops stack, returns None if empty """
        ret = None        
        if (self.__entries):
            ret = self.__entries[-1]
            del self.__entries[-1]  
            print "Popped: ", ret
        return ret

    def peek(self):
        """ peeks stack, returns None if empty """
        ret = None        
        if (self.__entries):
            ret = self.__entries[-1]      
        return ret

    def contents(self):
        """ stack pretty printing """
        print "###"
        if (self.is_empty() == False):
            for entry in reversed(self.__entries):
                print entry

#############################################################################
