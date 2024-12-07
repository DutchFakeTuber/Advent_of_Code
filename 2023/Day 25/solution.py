import networkx
from matplotlib import pyplot

TEST: str = open("test.txt")
DATA: str = open("input.txt")

def fetchData(data: str) -> dict[str, list[str]]:
    return {line.split(': ')[0]: line.split(': ')[1].split(' ') for line in data.splitlines()}

def partOne(nodes: dict[str, list[str]]) -> int:
    """
    This approach is not a general approach.
    Create the graph, visualize and cut lines by hand.
    """
    graph: networkx.Graph = networkx.Graph()
    [graph.add_edge(key, val) for key, vals in nodes.items() for val in vals]
    nodes: list[tuple[int]] = [('xft', 'pzv'), ('cbx', 'dqf'), ('sds', 'hbr')] # Input Nodes
    # nodes: list[tuple[int]] = [('pzl', 'hfx'), ('jqt', 'nvd'), ('cmg', 'bvb')] # Example
    graph.remove_edges_from(nodes)
    # networkx.draw_networkx(graph)
    # pyplot.show()
    return len(networkx.node_connected_component(graph, nodes[0][0])) * len(networkx.node_connected_component(graph, nodes[0][1]))

if __name__ == "__main__":
    nodes: dict[str, list[str]] = fetchData(DATA)
    print(partOne(nodes))
