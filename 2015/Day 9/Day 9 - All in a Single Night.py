from itertools import combinations

from All_in_a_Single_Night import INPUT, TEST

def getData(data: str) -> dict[str, dict[str, int]]:
    graph: dict[str, dict[str, int]] = dict()
    for locations in data.splitlines()[1:]:
        location1, location2, weight = locations.split(' to ')[0], *locations.split(' to ')[1].split(' = ')
        graph[location1] = {**graph.get(location1, {}), location2: int(weight)}
        graph[location2] = {**graph.get(location2, {}), location1: int(weight)}
    # Put Dummy into it for the Held-Karp algorithm
    graph["Dummy"] = {}
    for city in graph:
        graph['Dummy'][city] = 0
        graph[city]['Dummy'] = 0
    return graph

def distance(start: str, end: str, dist: dict) -> int:
    assert start in dist and end in dist
    return 0 if start == end else dist[start][end]

def held_karp_algorithm(graph: dict[str, dict[str, int]], min_path=True) -> int:
    cities = list(graph.keys())
    cities = ['Dummy'] + cities[:-1]
    number_of_cities = len(cities)
    
    route = {}
    for k in range(1, number_of_cities):
        route[tuple([k]), k] = distance(cities[0], cities[k], graph)

    for start in range(2, number_of_cities):
        for _start in combinations(range(1, number_of_cities), start):
            for k in _start:
                options: list = []
                for m in _start:
                    if m == k:
                        continue
                    m_k = distance(cities[m], cities[k], graph)
                    
                    _s_not_k = tuple([i for i in _start if i != k])
                    options.append(route[(_s_not_k, m)] + m_k)
                route[(_start, k)] = min(options) if min_path else max(options)
    paths = []
    for k in range(1, number_of_cities):
        paths.append(route[tuple([tuple(i for i in range(1, number_of_cities)), k])])
    return min(paths) if min_path else max(paths)

def partOne(locations: dict[str, dict[str, int]]) -> int:
    return held_karp_algorithm(locations, True)

def partTwo(locations: dict[str, dict[str, int]]) -> int:
    return held_karp_algorithm(locations, False)

if __name__ == "__main__":
    locations: dict[str, dict[str, int]] = getData(INPUT)
    print(partOne(locations))
    print(partTwo(locations))
