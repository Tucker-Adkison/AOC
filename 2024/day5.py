def check_rules_1(ordering_rules, page_nums):
    for i in range(len(page_nums)):
        if i == 0 or page_nums[i] not in ordering_rules :
            continue 

        rules = ordering_rules[page_nums[i]]
        for j in range(0, i + 1):
            if page_nums[j] in rules:
                return False
            
    return True

def check_rules_2(ordering_rules, page_nums):
    incorrect = False

    for i in range(len(page_nums)):
        if i == 0 or page_nums[i] not in ordering_rules :
            continue 

        rules = ordering_rules[page_nums[i]]
        for j in range(0, i + 1):
            if page_nums[j] in rules:
                first, second = page_nums.index(page_nums[j]), page_nums.index(page_nums[i])
                page_nums[first], page_nums[second] = page_nums[second], page_nums[first]
                incorrect = True
            
    return incorrect

f = open('input_day4')

ordering_rules = {}
pages = []
result = 0

for line in f.readlines():
    if line == '\n':
        continue

    elif '|' in line:
        first, second = line.strip().split('|')

        if first not in ordering_rules:
            ordering_rules[first] = set([second]) 
        else:
            ordering_rules[first].add(second)
    else:
        page_nums = line.strip().split(',')

        if check_rules_1(ordering_rules, page_nums):
            result += int(page_nums[len(page_nums) // 2])


print(result)

#---------------------------------#

f = open('input_day4')

ordering_rules = {}
pages = []
result = 0

for line in f.readlines():
    if line == '\n':
        continue

    elif '|' in line:
        first, second = line.strip().split('|')

        if first not in ordering_rules:
            ordering_rules[first] = set([second]) 
        else:
            ordering_rules[first].add(second)
    else:
        page_nums = line.strip().split(',')

        if check_rules_2(ordering_rules, page_nums):
            result += int(page_nums[len(page_nums) // 2])

print(result)