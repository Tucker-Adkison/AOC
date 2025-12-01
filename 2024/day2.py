def isSafe(nums):
    dec = 0
    inc = 0
    total = 0
    for i in range(len(nums) - 1):
        num_1 = int(nums[i])
        num_2 = int(nums[i+1])

        if abs(num_1 - num_2) >= 1 and abs(num_1 - num_2) <= 3:
            if num_1 > num_2:
                dec += 1
            if num_1 < num_2:
                inc += 1
        total += 1

    if inc == total or dec == total:
        return True


f = open("inputs/input_2", "r")

safe = 0

for line in f:
    nums = line.split()

    if isSafe(nums):
        safe += 1

print(safe)

# -----------------------------------------------#

f = open("inputs/input_2", "r")

safe = 0

for line in f:
    nums = line.split()
    if isSafe(nums):
        safe += 1
    else:
        len_nums = len(nums)

        for i in range(len_nums):
            new_nums = nums[:]
            new_nums.pop(i)
            if isSafe(new_nums):
                safe += 1
                break

print(safe)
