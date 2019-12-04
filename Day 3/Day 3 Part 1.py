def main():
    wireA, wireB = readfile()
    settingsA, settingsB = setup_grid(wireA), setup_grid(wireB)
    gridxmax = max(settingsA[0], settingsB[0])
    gridymax = max(settingsA[1], settingsB[1])
    gridxmin = min(settingsA[2], settingsB[2])
    gridymin = min(settingsA[3], settingsB[3])

    origin = [abs(gridxmin), abs(gridymin)]
    currA, currB = origin, origin
    grid = [["" for x in range(gridxmax - gridxmin + 1)] for y in range(gridymax - gridymin + 1)]

    min_manhattan = -1

    countA, countB = 0, 0
    while len(wireA) > 0 or len(wireB) > 0:
        if len(wireA) > 0:
            if countA == int(wireA[0][1:]):
                countA = 0
                wireA.pop(0)
            else:
                currA = add_to_grid(grid, wireA, currA, "A")
                if "AB" in grid[currA[1]][currA[0]] or "BA" in grid[currA[1]][currA[0]]:
                    min_manhattan = manhattan_comp(currA, min_manhattan,origin)
                countA += 1
        if len(wireB) > 0:
            if countB == int(wireB[0][1:]):
                countB = 0
                wireB.pop(0)
            else:
                currB = add_to_grid(grid, wireB, currB, "B")
                if "AB" in grid[currB[1]][currB[0]] or "BA" in grid[currB[1]][currB[0]]:
                    min_manhattan = manhattan_comp(currB, min_manhattan,origin)
                countB += 1
    return min_manhattan
def add_to_grid(grid, wire, pos, char):
    if wire[0][0] == "R":
        newpos = [pos[0] + 1, pos[1]]
        grid[newpos[1]][newpos[0]] += char
    if wire[0][0] == "L":
        newpos = [pos[0] - 1, pos[1]]
        grid[newpos[1]][newpos[0]] += char
    if wire[0][0] == "U":
        newpos = [pos[0], pos[1] + 1]
        grid[newpos[1]][newpos[0]] += char
    if wire[0][0] == "D":
        newpos = [pos[0], pos[1] - 1]
        grid[newpos[1]][newpos[0]] += char
    return newpos

def manhattan_comp(pos, manhattan, origin):
    temp_distance = abs(pos[1] - origin[1]) + abs(pos[0] - origin[0])
    if manhattan == -1:
        min_manhattan = temp_distance
    else:
        min_manhattan = min(manhattan, temp_distance)
    return min_manhattan

def setup_grid(wire):
    xmax, ymax, xmin, ymin = 0, 0, 0, 0
    length, height = 0, 0
    for element in wire:
        if element[0] == "R":
            length += int(element[1:])
        if element[0] == "L":
            length -= int(element[1:])
        if element[0] == "U":
            height += int(element[1:])
        if element[0] == "D":
            height -= int(element[1:])

        if xmin > length:
            xmin = length
        if ymin > height:
            ymin = height
        if xmax < length:
            xmax = length
        if ymax < height:
            ymax = height
    return [xmax, ymax, xmin, ymin]

def readfile():
    with open ('input','r') as file:
        wireA,wireB = file.readlines()
        wireA,wireB = wireA[:-1].split(','),wireB.split(',')
    file.close()
    return [wireA,wireB]



print(main())