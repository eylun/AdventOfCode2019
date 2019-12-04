def main():
    wireA, wireB = readfile()
    #wireA, wireB = ['R75','D30','R83','U83','L12','D49','R71','U7','L72'],['U62','R66','U55','R34','D71','R55','D58','R83']
    #wireA, wireB = ['R98', 'U47', 'R26', 'D63', 'R33', 'U87', 'L62', 'D20', 'R33', 'U53', 'R51'],['U98', 'R91', 'D20', 'R16', 'D67', 'R40', 'U7', 'R15', 'U6', 'R7']
    #wireA, wireB = ['L50','U50','R50'],['U50','L40','L10','D60']
    settingsA, settingsB = setup_grid(wireA), setup_grid(wireB)
    gridxmax = max(settingsA[0], settingsB[0])
    gridymax = max(settingsA[1], settingsB[1])
    gridxmin = min(settingsA[2], settingsB[2])
    gridymin = min(settingsA[3], settingsB[3])

    origin = [abs(gridxmin), abs(gridymin)]
    currA, currB = origin, origin
    grid = [[0 for x in range(gridxmax - gridxmin + 1)] for y in range(gridymax - gridymin + 1)]
    steplist = []
    countA, countB = 0, 0
    total_countA, total_countB = 0, 0
    while len(wireA) > 0:
        if countA == int(wireA[0][1:]):
            countA = 0
            wireA.pop(0)
        else:
            total_countA += 1
            countA += 1
            currA = add_to_grid(grid, wireA, currA, total_countA)
    while len(wireB) > 0:
        if countB == int(wireB[0][1:]):
            countB = 0
            wireB.pop(0)
        else:
            total_countB += 1
            countB += 1
            currB = add_to_grid(grid, wireB, currB, 0)
            if grid[currB[1]][currB[0]] > 0:
                steplist.append(grid[currB[1]][currB[0]] + total_countB)
    return min(steplist)

def add_to_grid(grid, wire, pos, char):
    if wire[0][0] == "R":
        newpos = [pos[0] + 1, pos[1]]
        curr_value = grid[newpos[1]][newpos[0]]
        if curr_value == 0:
            grid[newpos[1]][newpos[0]] += char
    if wire[0][0] == "L":
        newpos = [pos[0] - 1, pos[1]]
        curr_value = grid[newpos[1]][newpos[0]]
        if curr_value == 0:
            grid[newpos[1]][newpos[0]] += char
    if wire[0][0] == "U":
        newpos = [pos[0], pos[1] + 1]
        curr_value = grid[newpos[1]][newpos[0]]
        if curr_value == 0:
            grid[newpos[1]][newpos[0]] += char
    if wire[0][0] == "D":
        newpos = [pos[0], pos[1] - 1]
        curr_value = grid[newpos[1]][newpos[0]]
        if curr_value == 0:
            grid[newpos[1]][newpos[0]] += char
    return newpos

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