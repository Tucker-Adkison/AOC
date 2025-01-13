
from math import inf
from collections import Counter

def print_arr(arr):
    for a in arr:
        for i in a:
            print(i, end='')
        print()
        
def get_neighbors():
    return [(0, 1), (1, 0), (-1, 0), (0, -1)]

def in_bounds(pair, grid_size):
    return pair[0] >= 0 and pair[1] >= 0 and pair[0] < grid_size and pair[1] < grid_size

def dijkstras(source, vertexes):
    dist = {}
    prev = {}
    q = []
    for v in vertexes:
        dist[v] = inf 
        prev[v] = None 
        q.append(v)
        
    dist[source] = 0
    
    while q:
        u = -1
        m = inf 
        
        for v in q:
            if dist[v] <= m:
                u = v 
                m = dist[v]
        
        q.remove(u)
        
        for pair in get_neighbors():
            v = (u[0] + pair[0], u[1] + pair[1])
            if v in q and v in vertexes:
                alt = dist[u] + 1
                if alt < dist[v]:
                    dist[v] = alt
                    prev[v] = u
    
    return dist, prev

def get_path(start, prev):
    path = []
    
    while start:
        path.append(start)
        start = prev[start]
        
    return path

def trace_path(start_skip, end_skip, path):
    time = 0
    i = 0
    while (i < len(path)):
        pos = path[i]
        
        if (pos == start_skip):
            prev_i = i
            pos = end_skip
            i = path.index(pos)
            
            if (prev_i > i):
                return -1
     
        time += 1
        i += 1

    return time

f = open('input_20', 'r')
grid = []
vertexes = set()
walls = set()
outer_walls = set()
all_points = set()

start = None 
end = None 
for line in f:
    temp = []
    for c in line.strip():
        temp.append(c)
    
    grid.append(temp)
    
for i in range(len(grid)):
    for j in range(len(grid[i])):
        if j == 0 or j == len(grid[i]) - 1 or i == 0 or i == len(grid) - 1:
            outer_walls.add((i, j))
            continue
        
        c = grid[i][j]
        
        if (c != '#'):
            vertexes.add((i, j))
        else:
            walls.add((i, j))
        
        if (c == 'S'):
            start = (i, j)
        elif (c == 'E'):
            end = (i, j)
            
        all_points.add((i, j))
            
    
dist, prev = dijkstras(start, vertexes)
original_time = dist[end]
path = list(reversed(get_path(end, prev)))
result = 0
      
def dfs(initial, curr, depth, visited, path, times):
    if (depth == 21):
        return
    
    if initial != curr and curr in path:
        time = trace_path(initial, curr, path)
        diff_time = original_time - time - 1
        
        if (diff_time != original_time and diff_time > 0):
            times.append(diff_time)
            
    visited.add(curr)

    for n in get_neighbors():
        adj = (curr[0] + n[0], curr[1] + n[1])
        
        if not adj in visited and adj in all_points:
            dfs(initial, adj, depth+1, visited, path, times)
                
times = []

for v in path:
    dfs(v, v, 0, set(), path, times)

print(len(times))
print(Counter(times)[50])
