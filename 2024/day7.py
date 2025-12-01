f = open('inputs/input_7', 'r')


def is_valid(result, value, numbers, curr):
    if result == value and curr == len(numbers):
        return True
    elif curr == len(numbers):
        return False

    return is_valid(result + numbers[curr], value, numbers, curr+1) or is_valid(result * numbers[curr], value, numbers, curr+1) or is_valid(int(str(result) + str(numbers[curr])), value, numbers, curr+1)


count = 0

for line in f.readlines():
    value, equation = line.split(':')
    value = int(value)

    numbers = list(map(lambda x: int(x), equation.split()))

    if (is_valid(numbers[0], value, numbers, 1)):
        count += value

print(count)
