class Graph:
    def __init__(self):
        self.vertices = {}
    
    def add_vertex(self, vertex):
        self.vertices[vertex] = []

    def add_edge(self, source, target):
        self.vertices[source].append(target)

myGraph = Graph()
myGraph.add_vertex("David")
myGraph.add_vertex("Miriam")
myGraph.add_vertex("Martin")
myGraph.add_edge("David", "Miriam")
myGraph.add_edge("David", "Martin")
myGraph.add_edge("Miriam", "Martin")

print(myGraph.vertices)