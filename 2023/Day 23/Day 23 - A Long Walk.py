from A_Long_Walk import TEST, DATA
from networkx import DiGraph, grid_2d_graph, all_simple_edge_paths, all_simple_paths
from networkx.classes.function import path_weight

def fetchData(data: str) -> list[str]:
    return data.splitlines()

def graph(maze: list[str], slippery: bool=True) -> grid_2d_graph:
    edges: tuple[tuple[int]] = ((-1, len(maze)), (-1, len(maze[0])))
    previous: dict = {'^': (1, 0), '>': (0, -1), 'v': (-1, 0), '<': (0, 1)}
    if slippery:
        graphs: grid_2d_graph = grid_2d_graph(edges[0][1], edges[1][1], create_using=DiGraph)
    else:
        graphs: grid_2d_graph = grid_2d_graph(edges[0][1], edges[1][1])
    for row, r in enumerate(maze):
        for col, c in enumerate(r):
            coord: tuple[int] = (row, col)
            if c == '#':
                graphs.remove_node(coord)
            elif slippery:
                # Check if character is slippery
                if xy := previous.get(c):
                    x, y = xy
                    # Remove edge from node
                    graphs.remove_edge(coord, (row + x, col + y))
    return graphs

def partOne(maze: list[str]) -> int:
    start, end = (0, maze[0].index('.')), (len(maze)-1, maze[-1].index('.'))
    graphs: grid_2d_graph = graph(maze, slippery=True)
    return max(map(len, all_simple_edge_paths(graphs, start, end)))

def partTwo(maze: list[str]) -> int:
    start, end = (0, maze[0].index('.')), (len(maze)-1, maze[-1].index('.'))
    graphs: grid_2d_graph = graph(maze, slippery=False)
    # Get all nodes with exactly two neighbors
    neighbors: list = [g for g in graphs.nodes if len(graphs.edges(g)) == 2]
    for neighbor in neighbors:
        n1, n2 = list(graphs.neighbors(neighbor))
        weight: int = sum(graphs.edges[neighbor, n].get("d", 1) for n in (n1, n2))
        graphs.add_edge(n1, n2, d=weight)
        graphs.remove_node(neighbor)
    return max(path_weight(graphs, path, "d") for path in all_simple_paths(graphs, start, end))

if __name__ == "__main__":
    maze: list[str] = fetchData(DATA)
    print(partOne(maze))
    print(partTwo(maze))
