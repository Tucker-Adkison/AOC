
from math import inf

def print_arr(arr):
    for a in arr:
        for i in a:
            print(i, end='')
        print()
        
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
        
        
        if u == (len(grid) - 1, len(grid) -1):
            break
        
        q.remove(u)
        
        for pair in [(0, 1), (1, 0), (-1, 0), (0, -1)]:
            v = (u[0] + pair[0], u[1] + pair[1])
            if i == 0 and j == 0 and not in_bounds(v, len(grid)):
                continue    
            if v in q:
                alt = dist[u] + 1
                if alt < dist[v]:
                    dist[v] = alt
                    prev[v] = u
    
    return dist, prev

f = open('input_18', 'r')
grid = [['.' for _ in range(71)] for _ in range(71)]
vertexes = []

for i in range(len(grid)):
        for j in range(len(grid)):
            if grid[i][j] == '.':
                vertexes.append((i, j))

i = 0
curr_path = []
for line in f:
    x, y = line.strip().split(',')
    grid[int(y)][int(x)] = "#"
    
    vertexes.remove((int(y), int(x)))
    
    if i >= 1024:
        if (int(y), int(x)) in curr_path or len(curr_path) == 0:
            dist, prev = dijkstras((0, 0), vertexes)
            
            if (dist[(70, 70)] == inf):
                print((x,y))
                break
            
            s = set()
            u = (70, 70)
            
            while u:
                s.add(u)
                u = prev[u]
                
            curr_path = s
    
    i += 1

# dist, prev = dijkstras((0, 0), vertexes)
# print(dist[(70, 70)])

# u = (70, 70)

# while u:
#     grid[u[0]][u[1]] = 'O'
#     u = prev[u]
    
# print_arr(grid)