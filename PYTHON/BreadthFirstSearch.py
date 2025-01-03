import queue
def bfs(self):
    if self.root:
        visited_nodes = []
        bfs_queue = queue.SimpleQueue()
        bfs_queue.put(self.root)
        while not bfs_queue.empty():
            current_node = bfs_queue.get()
            visited_nodes.append(current_node.data)
            if current_node.left:
                bfs_queue.put(current_node.left)
            if current_node.right:
                bfs_queue.put(current_node.right)
    return visited_nodes


def bfsGraph(graph, initial_vertex):
    visited_vertices = []
    bfs_queue = queue.SimpleQueue()
    bfs_queue.put(initial_vertex)
    visited_vertices.append(initial_vertex)
    while not bfs_queue.empty():
        current_vertex = bfs_queue.get()
        for adjacent_vertex in graph[current_vertex]:
            if adjacent_vertex not in visited_vertices:
                visited_vertices.append(adjacent_vertex)
                bfs_queue.put(adjacent_vertex)
    return visited_vertices