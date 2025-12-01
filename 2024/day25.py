def convert_to_pins(lines):
    pins = []
    for j in range(len(lines[0])):
        column = ""
        for i in range(len(lines)):
            column += lines[i][j]

        pins.append(column.count("#") - 1)

    return pins


def parse_schemantic(lines, locks, keys):
    line_len = len(lines[0])
    pins = convert_to_pins(lines)

    if lines[0].count("#") == line_len and lines[6].count(".") == line_len:
        locks.append(pins)
    else:
        keys.append(pins)


f = open('inputs/input_25', 'r')

schemantic = []
lines = []
locks = []
keys = []
for line in f:
    if len(line.strip()) == 0:
        parse_schemantic(lines, locks, keys)

        lines.clear()
        continue

    lines.append(line.strip())

parse_schemantic(lines, locks, keys)

result = 0

for lock in locks:
    for key in keys:
        count = 0
        for i in range(len(lock)):
            if 5 - (lock[i] + key[i]) < 0:
                break

            count += 1

        if count == len(lock):
            result += 1

print(result)
