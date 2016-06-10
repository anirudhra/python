#import mystack
import mynode
import myqueue

#############################################################################
# Main program - breadth first search
#############################################################################

# create inf. queue
queue = myqueue.Queue()

node = []
MAX_NODES = 10

# create nodes
for i in range(0,MAX_NODES):
    node.append(mynode.Node(i))

# create tree
node[0].set_children([ node[1], node[2], node[3] ])
node[1].set_children([ node[4], node[5] ])
node[3].set_children( node[6] )
node[6].set_children([ node[7], node[8] ])
node[2].set_children( node[9] )

# print tree
for i in range(0,MAX_NODES):
    print node[i]

# function to explore breadth wise
def explore_node(nodeNum):
    ret = None
    node[nodeNum].set_data("Gray")
    for child in node[nodeNum].get_children():
        if node[child].get_data() == "White":
            queue.enqueue(node[child].get_nodeNum())
            node[child].set_data("Gray")
            ret = 1
    return ret


# __main__ loop
queue.enqueue(node[0].get_nodeNum())
while (queue.is_empty() != True):
    print "Start: ", queue.contents()
    curr_node = queue.peek()
    ret = explore_node(curr_node)

    #if all done, change to black
    #if ret == 1:
    node[curr_node].set_data("Black")
    queue.dequeue()
    print queue.contents()


