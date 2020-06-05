"""
Graph Theory : find path between start vertex and end vertex
"""

def find_path(graph, vertex_start,vertex_end,path_len=0):
    if path_len >= len(graph):
        return False

    #Direct Path
    if graph[vertex_start][vertex_end]:
        return True

    for vertex_neighbour, edge in enumerate(graph[vertex_start]):
        if edge:
            if find_path(graph, vertex_neighbour, vertex_end, path_len+1):
                return True

    return False

G = [
    [1,1,0,0,0],
    [0,1,0,0,0],
    [0,0,1,0,0],
    [0,1,1,1,0],
    [1,0,0,1,1],
]

print(find_path(G, 3, 0))