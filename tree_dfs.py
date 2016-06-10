import mystack
import mynode

#############################################################################
# Main program - depth first search
#############################################################################

# create inf. stack
stack = mystack.Stack()

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

# function to stack up depth wise
def explore_node(nodeNum):
    ret = None
    for child in node[nodeNum].get_children():
        if node[child].get_data() == "White":
            stack.push(node[child].get_nodeNum())
            node[child].set_data("Gray")
            ret = 1
            break
    if ret:
        print stack.contents()
    return ret


# __main__ loop
node[0].set_data("Gray")
stack.push(node[0].get_nodeNum())
while (stack.is_empty() != True):
    curr_node = stack.peek()
    ret = explore_node(curr_node)

    #if all done, change to black
    if ret == None:
        node[curr_node].set_data("Black")
        stack.pop()


