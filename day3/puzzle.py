content = []
with open("input.txt", "r") as f:
    content = f.readlines()

fst = content[0]
scd = content[1]

test1_fst = "R98,U47,R26,D63,R33,U87,L62,D20,R33,U53,R51"
test1_scd = "U98,R91,D20,R16,D67,R40,U7,R15,U6,R7"


def create_points(origin, target):
    x, y = origin
    dir, dist = target
    result = []
    while dist > 0:
        if dir == "L":
            result.append((x - dist, y))
        elif dir == "R":
            result.append((x + dist, y))
        elif dir == "U":
            result.append((x, y + dist))
        else:
            result.append((x, y - dist))
        dist -= 1
    result.reverse()
    return result


def line_to_points(line):
    splitted = [(l[0], int(l[1:])) for l in line.split(",")]
    point = (0, 0)
    result = []
    for s in splitted:
        points = create_points(point, s)
        point = points[-1]
        result += points
    return result


fst_points = line_to_points(fst)
scd_points = line_to_points(scd)
intersections = set(fst_points) & set(scd_points)

# First puzzle
point = min(intersections,
            key=lambda x: abs(x[0]) + abs(x[1]))
distance = abs(point[0]) + abs(point[1])
print(str(point) + ", Distance: " + str(distance))


# Second puzzle
closest = min(intersections,
              key=lambda x: fst_points.index(x) + scd_points.index(x))
# + 2, because (0,0) is omitted for both pathes
distance = fst_points.index(closest) + scd_points.index(closest) + 2
print(str(closest) + ", Steps: " + str(distance))
