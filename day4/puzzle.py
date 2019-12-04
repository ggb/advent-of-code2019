input = (108457, 562041)

# First Puzzle


def rule_three(i):
    return i[0] == i[1] or i[1] == i[2] or i[2] == i[3] or i[3] == i[4] or i[4] == i[5]


def rule_four(i):
    return i[0] <= i[1] and i[1] <= i[2] and i[2] <= i[3] and i[3] <= i[4] and i[4] <= i[5]


def check_rules(i):
    return rule_three(str(i)) and rule_four(str(i))


result = [i for i in range(input[0], input[1]) if check_rules(i)]
print("Puzzle 1: " + str(len(result)))

# Second Puzzle


def check_additional_rule(i):
    return 2 in [i.count(s) for s in i]


result2 = [i for i in result if check_additional_rule(str(i))]
print("Puzzle 2: " + str(len(result2)))
