

class Graph:
    def __init__(self):
        self.graph = {}

    def print_graph(self):
        for vertex in self.graph:
            print(vertex, ':', self.graph[vertex])

    def add_vertex(self, vertex):
        if vertex not in self.graph.keys():
            self.graph[vertex] = []
            return True
        return False

    def add_edge(self, v1, v2):
        if v1 in self.graph.keys() and v2 in self.graph.keys():
            self.graph[v1].append(v2)
            self.graph[v2].append(v1)
            return True
        return False

    def remove_edge(self, v1, v2):
        if v1 in self.graph.keys() and v2 in self.graph.keys():
            try:
                self.graph[v1].remove(v2)
                self.graph[v2].remove(v1)
            except ValueError:
                pass
            return True
        return False

    def remove_vertex(self,vertex):
        if vertex in self.graph.keys():
            for i in self.graph[vertex]:
                self.graph[i].remove(vertex)
            del self.graph[vertex]
            return True
        return False


my_graph = Graph()
my_graph.add_vertex('A')
my_graph.add_vertex('B')
my_graph.add_vertex('C')
my_graph.add_vertex('D')

my_graph.add_edge('A','B')
my_graph.add_edge('A','C')
my_graph.add_edge('A','D')
my_graph.add_edge('B','D')
my_graph.add_edge('C','D')
my_graph.remove_edge('A','D')
my_graph.remove_edge('D','C')
my_graph.remove_vertex('D')

my_graph.print_graph()


































