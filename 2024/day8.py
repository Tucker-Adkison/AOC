from math import sqrt
from pprint import pprint

f = open('inputs/input_8', 'r')

antennas = {}

count = 0
height = 0
width = 0
grid = []


def check(width, height, point):
    return point[0] >= 0 and point[0] < width and point[1] >= 0 and point[1] < height


for line in f.readlines():
    chars = list(line.strip())
    grid.append(chars)
    for i in range(len(chars)):
        if chars[i] != '.':
            if chars[i] not in antennas:
                antennas[chars[i]] = list()

            antennas[chars[i]].append((width, i))
    height = len(chars)

    width += 1

antinodes = set()

for k in antennas.keys():
    for i in range(len(antennas[k])):
        for j in range(i+1, len(antennas[k])):
            x_1, y_1 = antennas[k][i]
            x_2, y_2 = antennas[k][j]

            y = y_2 - y_1
            x = x_2 - x_1

            points = [(x_1 - x, y_1 - y), (x_1 + x, y_1 + y),
                      (x_2 - x, y_2 - y), (x_2 + x, y_2 + y)]
            point_1 = antennas[k][i]
            point_2 = antennas[k][j]

            for p in points:
                if p == point_1 or p == point_2:
                    continue
                if check(width, height, p):
                    grid[p[0]][p[1]] = '#'
                    antinodes.add(p)


print(len(antinodes))

# -----------------------------------------------#


antinodes = set()

for k in antennas.keys():
    for i in range(len(antennas[k])):
        for j in range(i+1, len(antennas[k])):
            x_1, y_1 = antennas[k][i]
            x_2, y_2 = antennas[k][j]

            y = y_2 - y_1
            x = x_2 - x_1

            t = 1
            p = (x_1 - x, y_1 - y)
            while (check(width, height, p)):
                antinodes.add(p)
                t += 1
                p = (x_1 - t * x, y_1 - t * y)

            t = 1
            p = (x_1 + x, y_1 + y)
            while (check(width, height, p)):
                antinodes.add(p)
                t += 1
                p = (x_1 + t * x, y_1 + t * y)

            t = 1
            p = (x_2 - x, y_2 - y)
            while (check(width, height, p)):
                antinodes.add(p)
                t += 1
                p = (x_2 - t * x, y_2 - t * y)

            t = 1
            p = (x_2 + x, y_2 + y)
            while (check(width, height, p)):
                antinodes.add(p)
                t += 1
                p = (x_2 + t * x, y_2 + t * y)

print(len(antinodes))
