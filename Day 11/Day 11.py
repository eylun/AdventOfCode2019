def main():
    base_input = readfile() + [0] * 999
    surface = [["." for i in range(100)] for j in range(100)]
    surface[45][45] = "#"
    done = False
    robot_pos = [45, 45]
    directions = [ (-1, 0), (0, 1), (1, 0), (0, -1)]
    robot_dir = 0
    index, relative_base = 0, 0
    painted_pos = []
    while not done:
        if surface[robot_pos[1]][robot_pos[0]] == ".":
            input_value = 0
        elif surface[robot_pos[1]][robot_pos[0]] == "#":
            input_value = 1
        output = calc_index_zero(base_input, input_value, index, relative_base)
        if output == "Done":
            done = True
        else:
            [instructions, index, relative_base] = output
            if instructions[0] == 0:
                surface[robot_pos[0]][robot_pos[1]] = "."
            else:
                surface[robot_pos[0]][robot_pos[1]] = "#"
            if (robot_pos[0], robot_pos[1]) not in painted_pos:
                painted_pos.append((robot_pos[0], robot_pos[1]))
            if instructions[1] == 0:
                robot_dir += 1
                if robot_dir > 3:
                    robot_dir = 0
            else:
                robot_dir -= 1
                if robot_dir < 0:
                    robot_dir = 3
            robot_pos[0] += directions[robot_dir][0]
            robot_pos[1] += directions[robot_dir][1]
    for line in surface:
        print(line)
    return len(painted_pos)

def calc_index_zero(instruction, input_value, index, relative_base):
    output = []
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
            output.append(instruction[instruction_index[0]])
            index += 2
            if len(output) == 2:
                return [output, index, relative_base]

        elif opcode == 3:
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

    return "Done"



def readfile():
    with open("input", "r") as f:
        return list(map(lambda x: int(x), f.readline().split(",")))
main()