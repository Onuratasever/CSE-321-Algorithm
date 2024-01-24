from collections import defaultdict

class Graph:
    def __init__(self):
        self.graph = defaultdict(list)

    def add_edge(self, u, v, w):
        self.graph[u].append((v, w))
        self.graph[v].append((u, w))  # undirected graph olduğu için

def dfs(graph, start_vertex, end_vertex, path, visited, current_weight, min_weight):
    visited[start_vertex] = True
    path.append(start_vertex)

    if start_vertex == end_vertex:
        # If the current path is shorter than the minimum path, update it
        if current_weight < min_weight[0]:
            min_weight[0] = current_weight
            min_path[0] = list(path)
    else:
        for neighbour, weight in graph[start_vertex]:
            if not visited[neighbour]:
                dfs(graph, neighbour, end_vertex, path, visited, current_weight + weight, min_weight)
    visited[start_vertex] = False
    path.pop()

def exhaustive_search_shortest_path(graph, start_vertex, end_vertex):
    visited = defaultdict(bool)
    min_weight = [float('inf')]  # Initialize with infinite
    path = []
    global min_path
    min_path = [[]]  # Initialize empty list off list

    dfs(graph, start_vertex, end_vertex, path, visited, 0, min_weight)

    return min_path[0], min_weight[0]

def main():
    g = Graph()
    g.add_edge(0, 1, 2)
    g.add_edge(0, 2, 4)
    g.add_edge(1, 2, 1)
    g.add_edge(1, 3, 1)
    g.add_edge(2, 3, 3)
    g.add_edge(2, 4, 1)
    g.add_edge(4, 3, 1)

    start_node = 0
    end_node = 4

    shortest_path, shortest_path_latency = exhaustive_search_shortest_path(g.graph, start_node, end_node)

    print("Shortest Path from",start_node, "to",end_node, ":", shortest_path)
    print("Shortest Path Weight:", shortest_path_latency)

main()