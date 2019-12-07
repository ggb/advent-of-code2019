content = []
with open("input.txt", "r") as f:
    content = f.read()

source = [int(i) for i in content.split(",")]
nums = source[:]


def mode_eval(code, pos, offset):
    opcode = str(code[pos])[::-1][2:]
    if len(opcode) < offset or opcode[offset - 1] == "0":
        return code[code[pos + offset]]
    elif opcode[offset - 1] == "1":
        return code[pos + offset]


def intcode(code, pos):
    while code[pos] != 99:
        offset = 0
        inst = str(code[pos])[-1]
        if inst == "1":
            op1 = mode_eval(code, pos, 1)
            op2 = mode_eval(code, pos, 2)
            code[code[pos + 3]] = op1 + op2
            offset = 4
        elif inst == "2":
            op1 = mode_eval(code, pos, 1)
            op2 = mode_eval(code, pos, 2)
            code[code[pos + 3]] = op1 * op2
            offset = 4
        elif inst == "3":
            code[code[pos + 1]] = int(input("Input single digit: "))
            offset = 2
        elif inst == "4":
            print("Output: " + str(mode_eval(code, pos, 1)))
            offset = 2
        elif inst == "5":
            if mode_eval(code, pos, 1) != 0:
                pos = mode_eval(code, pos, 2)
                continue
            offset = 3
        elif inst == "6":
            if mode_eval(code, pos, 1) == 0:
                pos = mode_eval(code, pos, 2)
                continue
            offset = 3
        elif inst == "7":
            op1 = mode_eval(code, pos, 1)
            op2 = mode_eval(code, pos, 2)
            if op1 < op2:
                code[code[pos + 3]] = 1
            else:
                code[code[pos + 3]] = 0
            offset = 4
        elif inst == "8":
            op1 = mode_eval(code, pos, 1)
            op2 = mode_eval(code, pos, 2)
            if op1 == op2:
                code[code[pos + 3]] = 1
            else:
                code[code[pos + 3]] = 0
            offset = 4
        else:
            raise Exception("Unknown opcode.")
        pos += offset
    return code[pos]


# First and second puzzle
print(intcode(nums, 0))
