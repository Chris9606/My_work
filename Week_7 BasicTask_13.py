"""
CLASS NODE
   value <-- val

CLASS GRAPH
    dict <-- new dictionary
    key <-- []

    ADD_VERTEX
        NODE(val)
        dict val <-- []
        keys.append(val)

    ADD_EDGE(vertex_1, vertex_2)
        dict vertex_1.append(vertex_2)
        dict vertex_2.append(vertex_1)

"""
class Node:
    def __init__(self,value):
        self.value = value

class Graph:
    dict = {}             # key(nodeNameVale): value( Edges) //edges added here are for the ease of the use on BFS and DFS
    keys = []             # Stores the keys for the dictionary

    def add_vertex(self,value):    # Creates the new Vertex
        Node(value)
        self.dict[value] = []
        self.keys.append(value)

    def add_edge(self,vertex_1,vertex_2):     # Adds the edge connecting  vertex_1 and vertex_2
        self.dict[vertex_1].append(vertex_2)
        self.dict[vertex_2].append(vertex_1)


if __name__ =='__main__':
    G = Graph()
    G.add_vertex(1)
    G.add_vertex(2)
    G.add_vertex(3)
    G.add_vertex(4)
    G.add_vertex(5)
    G.add_vertex(6)
    G.add_vertex(7)
    G.add_vertex(8)
    G.add_vertex(9)
    G.add_vertex(10)

    G.add_edge(1, 2)
    G.add_edge(1, 3)
    G.add_edge(1, 4)
    G.add_edge(2, 5)
    G.add_edge(3, 6)
    G.add_edge(4, 7)
    G.add_edge(5, 8)
    G.add_edge(6, 8)
    G.add_edge(7, 8)
    G.add_edge(9, 8)
    G.add_edge(10, 9)
    print(Graph.dict)






