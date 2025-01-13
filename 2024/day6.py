def move(guard, direction):
    verticle, horizontal = (guard[0] + direction[0], guard[1] + direction[1])

    if verticle < 0 or verticle >= len(grid) or horizontal < 0 or horizontal >= len(grid[verticle]):
        return None, None

    if grid[verticle][horizontal] == '#':
        direction = (direction[1], -direction[0])

        return (guard[0] + direction[0], guard[1] + direction[1]), direction

    return (guard[0] + direction[0], guard[1] + direction[1]), direction

def check(guard, direction):
    verticle, horizontal = (guard[0] + direction[0], guard[1] + direction[1])

    if verticle < 0 or verticle >= len(grid) or horizontal < 0 or horizontal >= len(grid[verticle]):
        return True
    
    return grid[verticle][horizontal] == '#'


f = open('input_day6', 'r')

grid = []
guard = (-1, -1)
line_count = 0
direction = (-1, 0)
visited = set([guard])

for line in f.readlines():
    if '^' in line:
        guard = (line_count, line.index('^'))

    grid.append(list(line.strip()))

    line_count += 1

initial_guard = guard
initial_dir = direction

# generate path
while True:
    guard, direction = move(guard, direction)
    if guard:
        visited.add(guard)
    else:
        break

print(len(visited))

guard = initial_guard
direction = initial_dir

count = 0

while True:
    if guard:
        new_dir = (direction[1], -direction[0])
        if not check(guard, new_dir):
            new_guard, new_dir = move(guard, new_dir)

            seen = set([(guard, direction)])

            while new_guard != None:
                if ((new_guard, new_dir) in seen):
                    count += 1
                    break
                
                seen.add((new_guard, new_dir))
                new_guard, new_dir = move(new_guard, new_dir)

    else:
        break
    
    guard, direction = move(guard, direction)

print(count)