f = open('inputs/input_23', 'r')

graph = {}

for line in f:
    a, b = line.strip().split('-')

    if a in graph:
        graph[a].append(b)
    else:
        graph[a] = [b]

    if b in graph:
        graph[b].append(a)
    else:
        graph[b] = [a]

paths = set()
for k in graph.keys():
    arr = graph[k]
    for i in range(len(arr)):
        for j in range(i+1, len(arr)):
            two = arr[i]
            three = arr[j]

            if (two == three or two == k or three == k):
                continue

            if three in graph[two] and two in graph[three]:
                paths.add(tuple(sorted([k, two, three])))


t_paths = set()
for path in paths:
    for p in path:
        if 't' == p[0]:
            t_paths.add(path)
            break

print(len(t_paths))


# algorithm BronKerbosch2(R, P, X) is
#     if P and X are both empty then
#         report R as a maximal clique
#     choose a pivot vertex u in P ⋃ X
#     for each vertex v in P \ N(u) do
#         BronKerbosch2(R ⋃ {v}, P ⋂ N(v), X ⋂ N(v))
#         P := P \ {v}
#         X := X ⋃ {v}
def bors_kerbosch(R, P, X, G, C):
    if len(P) == 0 and len(X) == 0:
        C.append(sorted(R))
        return

    (d, pivot) = max([(len(G[v]), v) for v in P.union(X)])

    for v in P.difference(G[pivot]):
        bors_kerbosch(R.union(set([v])), P.intersection(
            G[v]), X.intersection(G[v]), G, C)
        P.remove(v)
        X.add(v)


cliques = []
bors_kerbosch(set([]), set(graph.keys()), set([]), graph, cliques)

largest = []

for p in cliques:
    if len(p) > len(largest):
        largest = p[:]

print(",".join(sorted(largest)))
