from math import inf
import time

def all_dists(graph, ori):
    num_vertex = len(ori)
    
    distance = [[0 for _ in range(len(graph))] 
                 for _ in range(len(graph))]
    
    for i in range(num_vertex):
        for j in range(num_vertex):
            if i == j:
                continue
            
            source = ori[i]
            target = ori[j]
            
            dist, _ = dijkstras(graph, source, target)
            distance[i][j] = dist[target]
                
    return distance

def get_dist(dists, source, target, ori):
    i = ori.index(source)
    j = ori.index(target)
    
    return dists[i][j]
    
def get_paths(target, prev, path, paths):
    if len(prev[target]) == 0:
        paths.append(list(reversed(path)) + ['A'])
        return
    
    for curr in prev[target]:
        get_paths(curr[0], prev, path + [curr[1]], paths)
        
def dijkstras(graph, source, target):
    dist = {}
    prev = {}
    q = []
    for v in graph.keys():
        dist[v] = inf 
        prev[v] = []
        q.append(v)
        
    dist[source] = 0
    
    while q:
        u = -1
        m = inf 
        
        for v in q:
            if dist[v] <= m:
                u = v 
                m = dist[v]
                
        if u == target:
            break
        
        q.remove(u)
        
        for (v, d) in graph[u]:
            if v in q:
                alt = dist[u] + 1
                
                if alt <= dist[v]:
                    dist[v] = alt
                    prev[v].append((u, d))
    
    return dist, prev

def perform_clicks(graph, initial, l, depth, memo):
    if ((initial, l, depth) in memo):
        return memo[(initial, l, depth)]
    
    best_path = ''
    paths = []
    _, prev = dijkstras(graph, initial, l)
    
    get_paths(l, prev, [], paths)
    
    best_dist = inf
    paths = list(map(lambda x: "".join(x), paths))
    
    for path in paths:
        i = 0    
        dist = 0 
        
        while i < len(path) - 1:
            dist += get_dist(d_dists, path[i], path[i+1], d_ori)
            
            i += 1
            
        if dist <= best_dist:
            best_path = path
            best_dist = dist
       
    dist = 0
    
    if depth == 2:  
        return len(best_path)
    else:
        init = 'A'
        for p in best_path:
            dist += perform_clicks(d_keypad, init, p, depth + 1, memo)  
            
            init = p
            
    memo[(initial, l, depth)] = dist
    
    return dist

if __name__ == '__main__':
    n_keypad = {
        '9': [('6', 'v'), ('8', '<')],
        '8': [('5', 'v'), ('7', '<'), ('9', '>')],
        '7': [('4', 'v'), ('8', '>')],
        '6': [('3', 'v'), ('5', '<'), ('9', '^')],
        '5': [('2', 'v'), ('4', '<'), ('6', '>'), ('8', '^')],
        '4': [('1', 'v'), ('7', '^'), ('5', '>')],
        '3': [('2', '<'), ('6', '^'), ('A', 'v')],
        '2': [('1', '<'), ('3', '>'), ('5', '^'), ('0', 'v')],
        '1': [('4', '^'), ('2', '>')],
        '0': [('A', '>'), ('2', '^')],
        'A': [('0', '<'), ('3', '^')],
    }

    d_keypad = {
        '^': [('v', 'v'), ('A', '>')],
        'A': [('>', 'v'), ('^', '<')],
        '>': [('v', '<'), ('A', '^')],
        'v': [('<', '<'), ('>', '>'), ('^', '^')],
        '<': [('v', '>')],
    }

    d_keypad_verticies = {
        '^': {'v' 'A'},
        'A': {'>', '^'},
        '>': ['v', 'A'],
        'v': {'<', '>', '^'},
        '<': {'v'},
    }

    n_ori = [
        str(9 - i) for i in range(10)
    ] + ['A']

    d_ori = [
        '^', 'A', '>', 'v', '<'
    ]
    
    n_dists = all_dists(n_keypad, n_ori)
    d_dists = all_dists(d_keypad, d_ori)

    f = open('inputs/input_21', 'r')
    result = 0
    
    memo = {}
        
    for line in f: 
        initial = 'A'
        dist = 0
        for l in line.strip():
            dist += perform_clicks(n_keypad, initial, l, 0, memo)
        
            initial = l
                        
        result += dist * int(line.strip()[:-1])
        
    print(result)       