from itertools import permutations

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


def intcode(code, pos, inp1, inp2):
    fst = True
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
            if fst:
                code[code[pos + 1]] = inp1
                fst = False
            else:
                code[code[pos + 1]] = inp2
            offset = 2
        elif inst == "4":
            return mode_eval(code, pos, 1)
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


def single_config(input):
    result = 0
    for i in input:
        result = intcode(nums, 0, i, result)
    return (result, input)


def calc_result():
    all_results = []
    for lower, upper in [(0, 4), (5, 9)]:
        for config in permutations(range(lower, upper + 1)):
            all_results.append(single_config(config))

    print(all_results[:30])
    return max(all_results, key=lambda x: x[0])


print(calc_result())
