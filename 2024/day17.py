import math

f = open("input_17", "r")

def run(nums, reg_A, reg_B, reg_C):
    result = []
    i = 0
    
    while i < len(nums) - 1:
        opcode = nums[i]
        operand = get_operand(nums[i+1], reg_A, reg_B, reg_C)
        literal_op = nums[i+1]
        
        if opcode == 0:
            reg_A = math.trunc(reg_A / (2 ** operand))
        elif opcode == 1:
            reg_B = reg_B ^ literal_op
        elif opcode == 2:
            reg_B = operand % 8 
        elif opcode == 3:
            if reg_A != 0:
                i = literal_op
                continue
        elif opcode == 4:
            reg_B = reg_B ^ reg_C
        elif opcode == 5:
            result.append(operand % 8)
        elif opcode == 6:
            reg_B =  math.trunc(reg_A / (2 ** operand))
        elif opcode == 7:
            reg_C =  math.trunc(reg_A / (2 ** operand))
            
        i += 2
            
    return result

def get_operand(operand, reg_A, reg_B, reg_C):
    if operand >= 0 and operand <= 3:
        return operand
    if operand == 4:
        return reg_A
    elif operand == 5:
        return reg_B
    elif operand == 6:
        return reg_C
    
def backtrack(A, reg_B, reg_C, depth, nums):
    if (depth == len(nums)):
        return A
   
    for i in range(0, 8):
        reg_A = (A * 8) + i
        result = run(nums, reg_A, reg_B, reg_C)
        start = len(nums) - depth - 1
        
        if (result == nums[start:]):
            result = backtrack(reg_A, reg_B, reg_C, depth + 1, nums)
            
            if(result):
                return result
    
    return None
        
for line in f:
    if "Register A:" in line:
        reg_A = int(line.split("Register A:")[1])
    elif "Register B:" in line:
        reg_B = int(line.split("Register B:")[1])
    elif "Register C:" in line:
        reg_C = int(line.split("Register C:")[1])
    elif "Program: " in line:
        program = line.split("Program: ")[1]
        nums = list(map(lambda x: int(x), program.split(',')))
        
        print(backtrack(0, 0, 0, 0, nums))