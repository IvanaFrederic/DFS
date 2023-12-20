class Graph:
    def __init__(self):
        self.vertices = {}

    def add_vertex(self, name, neighbors):
        self.vertices[name] = neighbors

    def dfs(self, start, visited, distances):
        visited.add(start)
        print(f"Visiting node: {start}, Distance: {distances[start]}")

        for neighbor in self.vertices[start]:
            if neighbor not in visited:
                distances[neighbor] = distances[start] + 1
                self.dfs(neighbor, visited, distances)

    def dfs_traversal(self, start):
        visited = set()
        distances = {node: 0 for node in self.vertices}
        self.dfs(start, visited, distances)

# Example usage:
g = Graph()
g.add_vertex('A', ['B', 'C'])
g.add_vertex('B', ['A', 'D', 'E'])
g.add_vertex('C', ['A', 'F', 'G'])
g.add_vertex('D', ['B'])
g.add_vertex('E', ['B'])
g.add_vertex('F', ['C'])
g.add_vertex('G', ['C'])

start_vertex = 'A'
print("DFS Traversal:")
g.dfs_traversal(start_vertex)
