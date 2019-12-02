content = []
with open("input.txt", "r") as f:
    content = f.read()

source = [int(i) for i in content.split(",")]
nums = source[:]


def intcode(code, pos):
    while code[pos] != 99:
        op1 = code[code[pos + 1]]
        op2 = code[code[pos + 2]]
        if code[pos] == 1:
            code[code[pos + 3]] = op1 + op2
        elif code[pos] == 2:
            code[code[pos + 3]] = op1 * op2
        else:
            raise Exception("Unknown opcode.")
        pos += 4
    return code[0]


# First puzzle
nums[1] = 12
nums[2] = 2
print(intcode(nums, 0))

# Second puzzle
i = 0
solved = False
while not solved and i < 100:
    j = 0
    while not solved and j < 100:
        nums = source[:]
        nums[1] = i
        nums[2] = j
        result = intcode(nums, 0)
        solved = result == 19690720
        if solved:
            print("Result: " + str(result) +
                  ", i: " + str(i) + ", j: " + str(j))
        j += 1
    i += 1
