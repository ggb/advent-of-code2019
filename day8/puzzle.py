content = []
with open("input.txt", "r") as f:
    content = f.read()


source = [int(i) for i in content]
nums = source[:]

width = 25
height = 6


def chunk(arr, size):
    result = []
    while len(arr) != 0:
        result.append(arr[:size])
        arr = arr[size:]
    return result


def count_num(arr, n):
    return len([i for i in arr if i == n])


layers = chunk(nums, width * height)

# First puzzle
fewest_zeros = min([(count_num(c, 0), c)
                    for c in layers], key=lambda x: x[0])[1]
count_1 = count_num(fewest_zeros, 1)
count_2 = count_num(fewest_zeros, 2)

print(count_1 * count_2)


# Second puzzle
result = []
for i in range(len(layers[0])):
    pixels = [layer[i] for layer in layers]
    not_transparent = next((x for x in pixels if x != 2), None)
    result.append(not_transparent)

for line in chunk(result, width):
    print("".join(["⬛" if p == 1 else "⬜" for p in line]))
