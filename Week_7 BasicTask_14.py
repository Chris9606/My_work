
class Node:
    def __init__(self,value,ver):
        self.value = value
        self.ver = ver
        Graph.dict[value] = ver
        Graph.keys.append(value)

class Graph:

    dict={}               # key(nodeNameVale): value( Edges)
    keys = []             # Stores the keys for the dictionary
    flagged = []          # checking
    stack = []
    queue = []

    def insert(self,value, ver):
        Node(value,ver)

    def breath_first(self,node = None,count=1,first = False):
        if node == None:                  # If no starting node passed on to the function it starts with the first added
            node = Graph.keys[0]
        if first == False:                # Initialise the starting node
            Graph.flagged.append(node)    # Flag the node as visited
            Graph.queue.insert(0,node)    # Insert it in a queue( First in / Fist out)
            count = 1
            first = True
        node = Graph.queue.pop()          # Pop the current node
        f = open('traversal', 'a+')          # Printing it in a text file
        f.write("BFS: " + str(node) + "\n")
        f.close()
        print(node)
        for edge in Graph.dict[node]:     # For every edge of the current node, flag it
            if edge not in Graph.flagged:
                Graph.flagged.append(edge)
        try:
            Graph.queue.append(Graph.flagged[count])    # Add the next flagged node to the queue
            self.breath_first(node,count+1,first)       # Call the function updating the count which points to the next flagged node to become current node
        except:                                         # Function stops the recursion when a run-time error occurs ( all items iterated - no more flagged nodes to add)
           pass


    def depth_first(self,node=None,first = False):
        if node == None:                               # If the starting node isn't provided take the first one added
            node = Graph.keys[0]
        if first == False:                             # Initialising the first node
            Graph.flagged.append(node)
            Graph.stack.append(node)
            first = True

        count_edge = len(Graph.dict[node]) - 1         # Counts down the visited edges so we now when all of them have been visited
        for edge in Graph.dict[node]:                  # Goes down on every edge of this node
            count_edge -= 1
            if edge not in Graph.flagged:              # If the edge is not visited, mark it as such and add it to the stack. Then recourse the function with it.
                Graph.stack.append(edge)
                Graph.flagged.append(edge)
                self.depth_first(edge,first)
            if count_edge < 0:                         # If the current node has no more edges that haven't been visited, it gets popped and printed.
                a = Graph.stack.pop()
                f = open('traversal', 'a+')
                f.write("DFS : " + str(a) + "\n")
                f.close()
                print (a)

if __name__ == '__main__':
    G = Graph()
    G.insert(1, [2,3,4])
    G.insert(2, [1,5])
    G.insert(3, [1,6])
    G.insert(4, [1,7])
    G.insert(5, [2,8])
    G.insert(6, [3,8])
    G.insert(7, [4,8])
    G.insert(8, [5,6,7,9])
    G.insert(9, [8,10])
    G.insert(10, [9])

    #G.depth_first()
    G.breath_first()



