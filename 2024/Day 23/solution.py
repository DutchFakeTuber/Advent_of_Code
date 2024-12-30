from os.path import dirname, realpath
import networkx as nx

TEST: str = open(f"{dirname(realpath(__file__))}\\test.txt").read()
DATA: str = open(f"{dirname(realpath(__file__))}\\input.txt").read()

def fetchData(data: str) -> list[list[str]]:
    return [line.split('-') for line in data.splitlines() if len(line)]

def partOne(data: list[list[str]]) -> int:
    network: nx.DiGraph = nx.DiGraph()
    network.add_edges_from((one, two) for one, two in data)
    lanConnection: dict[str, set] = {node: set(network.successors(node)).union(network.predecessors(node)) for node in network.nodes}
    seen: set = set()
    for node, first in [[key, val] for key, value in lanConnection.items() for val in value]:
        for second in lanConnection[first]:
            if node not in lanConnection[second]: continue
            normalized: tuple[str] = tuple(sorted((node, first, second)))
            if normalized in seen: continue
            seen.add(normalized)
    tNodes: set = {node for node in lanConnection.keys() if node.startswith('t')}
    return len({connection for connection in seen for node in connection if node in tNodes})

def partTwo(data: list[list[str]]) -> str:
    network: nx.DiGraph = nx.DiGraph()
    network.add_edges_from((one, two) for one, two in data)
    clusterCalc: dict[str, int] = nx.clustering(network)
    cluster = max(clusterCalc.values())
    nodes: set = {node for node, value in clusterCalc.items() if value == cluster}
    lanConnection: dict[str, set] = {node: set(network.successors(node)).union(network.predecessors(node)) for node in network.nodes}
    connections: set = set()
    for node in nodes:
        connections: set = max({node} | nodes.intersection(lanConnection[node]), connections, key=len)
    return ','.join(sorted(connections))

if __name__ == "__main__":
    data: list[list[str]] = fetchData(DATA)
    print(partOne(data))
    print(partTwo(data))
