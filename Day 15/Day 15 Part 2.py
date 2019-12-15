def main():
    base_input = readfile() + [0] * 999
    print(base_input)
    direction_dict = {1 : [0, -1],
                      2 : [0, 1],
                      3 : [-1, 0],
                      4 : [1, 0]}
    grids = []
    count = 0
    while count < 4:
        instructions = base_input[:]
        if count == 0:
            order = [1, 4, 2, 3]
        elif count == 1:
            order = [4, 2, 3, 1]
        elif count == 4:
            order = [2, 3, 1, 4]
        else:
            order = [3, 1, 4, 2]
        relative_base, index = 0, 0
        output, curr_dir = -1, 1
        move_count = 0
        grid = [[" " for x in range(41)] for y in range(41)]
        grid[21][21] = "D"
        base_location = [21, 21]
        while output != 2:
            # for line in grid:
            #     print(line)
            order_index = 0
            curr_dir = order[order_index]
            attempts = 0
            focus_grid = [" ",]
            dead_end = False
            while grid[base_location[1] + direction_dict[curr_dir][1]][base_location[0] + direction_dict[curr_dir][0]] not in focus_grid:
                #print(grid[base_location[1] + direction_dict[curr_dir][1]][base_location[0] + direction_dict[curr_dir][0]])
                order_index = (order_index + 1) % 4
                curr_dir = order[order_index]
                attempts += 1
                if attempts > 4:
                    dead_end = True
                    focus_grid.append(".")
                if attempts > 8:
                    break
            [output, relative_base, index] = calc_index_zero(instructions, relative_base, index, curr_dir)
            if output == 0:
                grid[base_location[1] + direction_dict[curr_dir][1]][base_location[0] + direction_dict[curr_dir][0]] = "#"
            else:
                move_count = move_count - 1 if dead_end else move_count + 1
                grid[base_location[1]][base_location[0]] = "E" if dead_end else "."
                base_location[0] += direction_dict[curr_dir][0]
                base_location[1] += direction_dict[curr_dir][1]
                grid[base_location[1]][base_location[0]] = "D"
                if output == 2:
                    end_point = base_location
        grids.append(grid)
        count += 1
    for j in range(len(grids[0])):
        for i in range(len((grids[0][0]))):
            if grids[0][j][i] in ["#", " "] or grids[1][j][i] in ["#", " "] or grids[2][j][i] in ["#", " "] or grids[3][j][i] in ["#", " "]:
                grids[0][j][i] = "#"
            if grids[0][j][i] in [".", "E"] or grids[1][j][i] in [".", "E"] or grids[2][j][i] in [".", "E"] or grids[3][j][i] in [".", "E"]:
                grids[0][j][i] = "."
    final_grid = grids[0]
    final_grid[21][21] = "X"
    final_grid[end_point[1]][end_point[0]] = "O"
    print(part2(final_grid,end_point))
    # for line in final_grid:
    #     print(line)



def part2(grid, oxygen_point):
    def helper_recursion(grid, focus_grid, count):
        if grid[focus_grid[1]][focus_grid[0]] in ["#","O"] and count != 0:
            return count - 1
        directions = [[0, -1], [0, 1], [-1, 0], [1, 0]]
        grid[focus_grid[1]][focus_grid[0]] = "O"
        count_store = []
        for i in range(len(directions)):
            next_point = [focus_grid[0] + directions[i][0], focus_grid[1] + directions[i][1]]
            count_store.append(helper_recursion(grid, next_point, count + 1))
        print(max(count_store))
        return max(count_store)
    return helper_recursion(grid, oxygen_point, 0)

def calc_index_zero(instruction, relative_base, index, input_direction):
    while instruction[index] != 99:
        opcode = instruction[index]
        modes = [0, 0, 0]
        modecode = opcode // 100
        modes[2], modes[1], modes[0] = modecode // 100, modecode % 100 // 10, modecode % 10
        opcode %= 10
        instruction_index = [0, 0, 0]

        for i in range(len(modes)):
            if modes[i] == 0:
                instruction_index[i] = instruction[index + 1 + i]
            if modes[i] == 1:
                instruction_index[i] = index + 1 + i
            if modes[i] == 2:
                instruction_index[i] = relative_base + instruction[index + 1 + i]

        if opcode == 4:
            index += 2
            return [instruction[instruction_index[0]], relative_base, index]

        elif opcode == 3:
            instruction[instruction_index[0]] = input_direction
            index += 2

        elif opcode == 5 or opcode == 6:
            first_para = instruction[instruction_index[0]]
            if opcode == 5:
                if first_para != 0:
                    index = instruction[instruction_index[1]]
                else:
                    index += 3
            else:
                if first_para == 0:
                    index = instruction[instruction_index[1]]
                else:
                    index += 3

        elif opcode == 7 or opcode == 8:
            comp_values = [instruction[instruction_index[0]], instruction[instruction_index[1]]]
            if opcode == 7:
                instruction[instruction_index[2]] = 1 if comp_values[0] < comp_values[1] else 0
            else:
                instruction[instruction_index[2]] = 1 if comp_values[0] == comp_values[1] else 0
            index += 4

        elif opcode == 9:
            relative_base += instruction[instruction_index[0]]
            index += 2

        elif opcode == 1 or opcode == 2:
            if opcode == 1:
                instruction[instruction_index[2]] = instruction[instruction_index[0]] + instruction[instruction_index[1]]
            if opcode == 2:
                instruction[instruction_index[2]] = instruction[instruction_index[0]] * instruction[instruction_index[1]]
            index += 4

    return "done"



def readfile():
    with open("input", "r") as f:
        return list(map(lambda x: int(x), f.readline().split(",")))
main()