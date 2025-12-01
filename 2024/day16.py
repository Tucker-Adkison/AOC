import collections
from math import inf


def get_direction(adj):
    if adj == (0, 1):
        return 'E'
    elif adj == (0, -1):
        return 'W'
    elif adj == (1, 0):
        return 'S'
    elif adj == (-1, 0):
        return 'N'


def opp_dir(dir, dir2):
    if (dir == 'E' and dir2 == 'W'):
        return True
    elif (dir == 'W' and dir2 == 'E'):
        return True
    elif (dir == 'N' and dir2 == 'S'):
        return True
    elif (dir == 'S' and dir2 == 'N'):
        return True
    return False


def make_graph(start, edges, graph):
    stack = [start]
    visited = set()

    while (len(stack) > 0):
        curr = stack.pop()
        graph[curr] = []

        visited.add(curr)

        adj_to = []
        for adj in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
            next_pos = ((curr[0][0] + adj[0], curr[0][1] + adj[1]),
                        get_direction(adj))

            if (grid[next_pos[0][0]][next_pos[0][1]] != '#'):
                adj_to.append(next_pos)
                graph[curr].append(next_pos)

                if next_pos not in visited:
                    visited.add(next_pos)
                    stack.append(next_pos)

    return graph


"""
1  function Dijkstra(Graph, source):
 2
 3      for each vertex v in Graph.Vertices:
 4          dist[v] ← INFINITY
 5          prev[v] ← UNDEFINED
 6          add v to Q
 7      dist[source] ← 0
 8
 9      while Q is not empty:
10          u ← vertex in Q with minimum dist[u]
11          remove u from Q
12
13          for each neighbor v of u still in Q:
14              alt ← dist[u] + Graph.Edges(u, v)
15              if alt < dist[v]:
16                  dist[v] ← alt
17                  prev[v] ← u
18
19      return dist[], prev[]
"""


def dijkstras(graph, source):
    dist = {}
    prev = {}
    Q = []

    for v in graph.keys():
        dist[v] = inf
        prev[v] = []

        Q.append(v)

    dist[source] = 0

    while Q:
        min = inf
        u = -1

        for v in Q:
            if dist[v] < min:
                min = dist[v]
                u = v

        Q.remove(u)

        for v in graph[u]:
            amount = 1

            if u[1] != v[1]:
                amount += 1000
            else:
                amount = 1

            alt = dist[u] + amount
            if alt <= dist[v]:
                dist[v] = alt
                prev[v].append(u)

    return dist, prev


def bfs(source, end, graph, seen):
    seen.add(source)

    if (source == end):
        return

    for s in graph[source]:
        if (s not in seen):
            bfs(s, end, graph, seen)


f = open('inputs/input_16', 'r')

grid = []
start = None
end = None

edges = {}
i = 0
for line in f:
    j = 0
    temp = []

    for c in line:
        if (c == 'S'):
            start = (i, j)
        elif (c == 'E'):
            end = (i, j)

        if (c != '#'):
            edges[(i, j)] = []
        if (c == '\n'):
            break

        temp.append(c)
        j += 1

    grid.append(temp)

    i += 1

directions = ['N', 'S', 'E', 'W']

graph = {}
start_d = (start, 'E')
graph = make_graph(start_d, edges, graph)

dist, prev = dijkstras(graph, start_d)

end_d = None

for d in directions:
    end_d = (end, d)

    if (end_d in dist):
        break

# for p in prev:
#     print(p, prev)

seen = set()

bfs(end_d, start_d, prev, seen)

points = set()
for s in seen:
    points.add(s[0])
    grid[s[0][0]][s[0][1]] = "O"

print(len(points))
