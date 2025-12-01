import re


def find_matches(line):
    return len(re.findall(r"(?=(XMAS))", line,)) + \
        len(re.findall(r"(?=(SAMX))", line))


f = open("inputs/input_4", "r")

lines = []

for line in f.readlines():
    lines.append(list(line.strip()))

max_col = len(lines[0])
max_row = len(lines)
cols = [[] for _ in range(max_col)]
rows = [[] for _ in range(max_row)]
fdiag = [[] for _ in range(max_row + max_col - 1)]
bdiag = [[] for _ in range(len(fdiag))]
min_bdiag = -max_row + 1

for line in f:
    lines.append(list(line))

for x in range(max_col):
    for y in range(max_row):
        cols[x].append(lines[y][x])
        rows[y].append(lines[y][x])
        fdiag[x+y].append(lines[y][x])
        bdiag[x-y-min_bdiag].append(lines[y][x])

result = 0

for line in cols + rows + fdiag + bdiag:
    result += find_matches(''.join(line))

print(result)

# -----------------------------------------------#

f = open("inputs/input_4", "r")

lines = []

for line in f.readlines():
    lines.append(list(line.strip()))

result = 0

for i in range(len(lines)):
    for j in range(len(lines[i])):
        matrix = []
        c = 0
        for k in [-1 + i, i, 1 + i]:
            line = []
            for l in [-1 + j, j, 1 + j]:
                if (k >= len(lines) or k < 0 or l >= len(lines[i]) or l < 0):
                    continue
                c += 1
                line.append(lines[k][l])

            matrix.append(line)
        if c == 9:
            diag = ''.join([row[i] for i, row in enumerate(matrix)])
            other_diag = ''.join([row[-i-1] for i, row in enumerate(matrix)])

            if ((diag == 'MAS' or diag == 'SAM') and (other_diag == 'MAS' or other_diag == 'SAM')):
                result += 1

print(result)
