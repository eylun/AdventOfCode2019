def main():
    base_input = readfile() + [0] * 999
    grid = []
    affected_point_count = 0
    top_left_corners = []
    for y in range(50):
        row = []
        consecutive = 0
        for x in range(50):
            instruction_copy = base_input[:]
            [output, index, relative_base] = calc_index_zero(instruction_copy, 0, 0, [x, y])
            if output == 1:
                row.append("#")
                affected_point_count += 1
                consecutive += 1
            elif output == 0:
                row.append(".")
        grid.append(row)
    for line in grid:
        print(line)
    print(affected_point_count)

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
main()