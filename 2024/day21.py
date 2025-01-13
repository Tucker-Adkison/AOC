from math import inf

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

def make_paths(graph, curr, line, index, path, seqs):
    if (index == len(line)):
        seqs.add("".join(path))
        
        return
    
    l = line[index]
    
    paths = []
    _, prev = dijkstras(graph, curr, l)
    
    get_paths(l, prev, [], paths)
    
    for p in paths:
        make_paths(graph, l, line, index + 1, path + p, seqs)
        

f = open('inputs/input_21', 'r')

result = 0

for line in f: 
    robot1s = set()
    make_paths(n_keypad, 'A', line.strip(), 0, [], robot1s)
    
    robot2s = set()
    for robot1 in robot1s:
        make_paths(d_keypad, 'A', robot1.strip(), 0, [], robot2s)
        
    robot3s = set()
    for robot2 in robot2s:
        make_paths(d_keypad, 'A', robot2.strip(), 0, [], robot3s)
     
    robot3 = min(robot3s, key=len)
    result += len(robot3) * int(line.strip()[:-1])
    
    print(robot3)
    
print(result)       