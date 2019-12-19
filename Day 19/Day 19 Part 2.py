def main():
    base_input = readfile() + [0] * 999
    grid = []
    dimension = 100
    first_hex = 0
    to_add = dimension - 1
    hex_amount = 0
    for y in range(2620):
        row = ["."] * first_hex if first_hex != 0 else []
        consecutive = 0
        x = first_hex
        top_left_corners = []
        while x < 2000:
            instruction_copy = base_input[:]
            [output, index, relative_base] = calc_index_zero(instruction_copy, 0, 0, [x, y])
            if output == 1:
                if consecutive == 0:
                    first_hex = x if x != 0 else 0
                if hex_amount != 0:
                    row += ["#"] * hex_amount
                    consecutive += hex_amount
                    x += hex_amount - 1
                    hex_amount = 0
                else:
                    row.append("#")
                    consecutive += 1
                if consecutive >= dimension:
                    top_left_corners.append((x, y))

            elif output == 0:
                row.append(".")
                if consecutive != 0:
                    row += ["."] * (2000 - x)
                    hex_amount = to_add if consecutive > to_add else consecutive - 1
                    x = 10000
            x += 1
        grid.append(row)
        for coords in top_left_corners:
            if grid[coords[1] - to_add][coords[0]] == grid[coords[1] - to_add][coords[0] - to_add] == grid[coords[1]][coords[0] - to_add] == "#":
                return (coords[0] - to_add) * 10000 + coords[1] - to_add
    # print(top_left_corners)
    # return_value = 0
    # for coords in top_left_corners:
    #     if grid[coords[1] + to_add][coords[0]] == grid[coords[1] + to_add][coords[0] + to_add] == grid[coords[1]][coords[0] + to_add] == "#":
    #         return_value = coords[0] * 10000 + coords[1]
    #         break
    # print(return_value)

def calc_index_zero(instruction, index, relative_base, input_lst):
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
            return [instruction[instruction_index[0]], index, relative_base]

        elif opcode == 3:
            input_value = input_lst.pop(0)
            instruction[instruction_index[0]] = input_value
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
print(main())