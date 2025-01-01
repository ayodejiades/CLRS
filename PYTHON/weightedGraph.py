class WeightedGraph:
  def __init__(self):
    self.vertices = {}
  
  def add_vertex(self, vertex):
    self.vertices[vertex] = []
    
  def add_edge(self, source, target, weight):
    self.vertices[source].append([target, weight])

myGraph = WeightedGraph()

myGraph.add_vertex('Paris')
myGraph.add_vertex('Toulouse')
myGraph.add_vertex('Biarritz')

myGraph.add_edge('Paris',"Toulouse", 678)
myGraph.add_edge("Toulouse", "Biarritz", 312)
myGraph.add_edge("Biarritz", 'Paris', 783)