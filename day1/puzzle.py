def fuel(mass):
    return mass // 3 - 2


lines = []
with open("input.txt", "r") as f:
    lines = f.readlines()

lines = [int(l) for l in lines]
result_1 = sum([fuel(l) for l in lines])
print(result_1)


def fuel_for_fuel(mass):
    result = fuel(mass)
    if result <= 0:
        return 0
    else:
        return result + fuel_for_fuel(result)


result_2 = sum([fuel_for_fuel(l) for l in lines])
print(result_2)
