from collections import defaultdict

SAMPLE_INPUT = """
kh-tc
qp-kh
de-cg
ka-co
yn-aq
qp-ub
cg-tb
vc-aq
tb-ka
wh-tc
yn-cg
kh-ub
ta-co
de-co
tc-td
tb-wq
wh-td
ta-ka
td-qp
aq-cg
wq-ub
ub-vc
de-ta
wq-aq
wq-vc
wh-yn
ka-de
kh-ta
co-tc
wh-qp
tb-vc
td-yn"""


def bron_kerbosch(R, P, X, graph, cliques):
    if not P and not X:
        # Base case: Found a maximal clique
        cliques.append(R)
        return

    for v in P.copy():
        bron_kerbosch(
            R.union({v}),
            P.intersection(graph[v]),
            X.intersection(graph[v]),
            graph,
            cliques,
        )
        # Move v from P to X
        P.remove(v)
        X.add(v)


def read_input():
    graph = defaultdict(set)
    f = SAMPLE_INPUT.split("\n")
    with open("/Users/kennethlee/workspace/aoc/2024/input/d23.txt") as f:
        for line in f:
            line = line.strip()
            if line:
                a, b = line.split("-")
                graph[a].add(b)
                graph[b].add(a)
    return graph


def find_triangles(graph):
    triangles = set()
    for node in graph:
        neighbors = graph[node]
        for neighbor in neighbors:
            common_neighbors = graph[node] & graph[neighbor]
            for common_neighbor in common_neighbors:
                triangles.add(tuple(sorted([node, neighbor, common_neighbor])))

    return triangles


if __name__ == "__main__":
    graph = read_input()
    triangles = find_triangles(graph)
    count_t_in_triangles = 0
    for triangle in triangles:
        for node in triangle:
            if node.startswith("t"):
                count_t_in_triangles += 1
                break

    # Part 1
    # print(len(triangles))
    # print(count_t_in_triangles)

    # Part 2
    R = set()
    P = set(graph.keys())
    X = set()
    max_cliques = []
    bron_kerbosch(R, P, X, graph, max_cliques)
    nodes = None
    max_size = 0
    for clique in max_cliques:
        if len(clique) > max_size:
            max_size = len(clique)
            nodes = clique

    print("Password for part 2 is:", ",".join(sorted(nodes)))
