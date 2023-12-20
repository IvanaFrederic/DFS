class Graph:
    def __init__(self):
        self.graph = {}

    def add_edge(self, vertex, neighbors):
        self.graph[vertex] = neighbors

    def dfs(self, start, visited=None):
        if visited is None:
            visited = set()

        if start not in visited:
            print(start, end=" ")
            visited.add(start)
            for neighbor in self.graph[start]:
                self.dfs(neighbor, visited)

# Example usage:
g = Graph()
g.add_edge('A', ['B', 'C'])
g.add_edge('B', ['A', 'D', 'E'])
g.add_edge('C', ['A', 'F', 'G'])
g.add_edge('D', ['B'])
g.add_edge('E', ['B', 'F'])
g.add_edge('F', ['C', 'E'])
g.add_edge('G', ['C'])

print("DFS starting from vertex 'A':")
g.dfs('A')
