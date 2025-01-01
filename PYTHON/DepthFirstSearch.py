def in_order(self, current_node):
    if current_node:
        self.in_order(current_node.left_child)
        print(current_node.data)
        self.in_order(current_node.right_child)


def pre_order(self, current_node):
    if current_node:
        print(current_node.data)
        self.pre_order(current_node.left_child)
        self.pre_order(current_node.right_child)


def dfs(visited_vertices, graph, current_vertex):
    if current_vertex not in visited_vertices:
        print(current_vertex)
        visited_vertices.add(current_vertex)
        for adjacent_vertex in graph[current_vertex]:
            dfs(visited_vertices, graph, adjacent_vertex)