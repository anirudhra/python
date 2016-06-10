#################################################
### Queue Python Module
#################################################

class Queue(object):

    """ Queue class """

    def __init__(self, size = 0):
        """ Constructor; if size == 0, queue is infinite """
        self.__entries = []
        self.__size = size

    def enqueue(self, data):
        """ pushes data in to queue """
        if (self.is_full() == False):
            self.__entries.append(data)
            print "Enqueued: ",data

    def is_full(self):
        """ Check for full only if size != 0 """
        ret = False
        if self.__size > 0:
            ret = (len(self.__entries) == self.__size)
        return ret

    def is_empty(self):
        return (len(self.__entries) == 0)

    def dequeue(self):
        """ dequeues entry, returns None if empty """
        ret = None        
        if (self.__entries):
            ret = self.__entries[0]
            del self.__entries[0]
            print "Dequeued: ", ret
        return ret

    def peek(self):
        """ peeks queue, returns None if empty """
        ret = None        
        if (self.__entries):
            ret = self.__entries[0]
        return ret

    def contents(self):
        """ queue pretty printing """
        print "###"
        if (self.is_empty() == False):
            for entry in (self.__entries):
                print entry

#############################################################################

