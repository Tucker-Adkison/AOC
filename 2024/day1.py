f = open("inputs/input_1", "r")

left = []
right = []

for line in f:
    i, j = line.split()
    left.append(int(i))
    right.append(int(j))

left.sort()
right.sort()

sum = 0

for pair in zip(left, right):
    sum += abs(pair[0] - pair[1])

print(sum)

# -----------------------------------------------#

f = open("input", "r")

left = []
occurances = {}

for line in f:
    i, j = line.split()

    num_j = int(j)

    left.append(int(i))

    if num_j in occurances:
        occurances[num_j] = occurances[num_j] + 1
    else:
        occurances[num_j] = 1

sum = 0

for i in left:
    if i in occurances:
        sum += occurances[i] * i

print(sum)
