import math


def mix_prune(value, num):
    return (value ^ num) % 16777216


def calculate(num):
    secret = num
    num *= 64
    num = mix_prune(secret, num)

    secret = num

    num = math.floor(num / 32)
    num = mix_prune(secret, num)

    secret = num

    num *= 2048
    num = mix_prune(secret, num)

    return num


f = open('inputs/input_22', 'r')

result = 0

for line in f:
    num = int(line.strip())
    for i in range(2000):
        num = calculate(num)

    result += num

print(result)


def calculate_price_change(num, n):
    changes = []
    for i in range(n):
        changes.append(int(str(num)[-1]))
        num = calculate(num)

    all_fours = {}
    i = 4

    while i < len(changes):
        fours = tuple([changes[i - j] - changes[i - j - 1] for j in range(4)])

        if fours not in all_fours:
            all_fours[fours] = changes[i]

        i += 1

    return all_fours


f = open('inputs/input_22', 'r')

all_fours = []
all_keys = set()
for secret in f:
    fours = calculate_price_change(int(secret.strip()), 2001)

    for key in fours.keys():
        all_keys.add(key)

    all_fours.append(fours)

m = 0
for key in all_keys:
    curr = 0
    for fours in all_fours:
        if key in fours:
            curr += fours[key]

    m = max(m, curr)

print(m)
