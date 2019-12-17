def main():
    base_input = readfile() + [0] * 1250
    print(base_input)
    index, relative_base = 0, 0
    done = False
    display, inner_display = [], []
    depth, length = 0, 0
    intersection_coords = []
    while not done:
        output = calc_index_zero(base_input, index, relative_base)
        if output == "done":
            done = True
        else:
            [ascii_index, index, relative_base] = output
            if chr(ascii_index) == "\n":
                display.append(inner_display)
                inner_display = []
                depth += 1
                length = 0
            else:
                inner_display.append(chr(ascii_index))
                if len(inner_display) >= 3 and depth >= 1:
                    if inner_display[length] == "#" and inner_display[length - 1] == "#" and inner_display[length - 2] == "#":
                        focus_x = length - 1
                        if display[depth - 1][focus_x] == "#":
                            intersection_coords.append((focus_x, depth))
                length += 1
    display = display[:-1] #Gets rid of the extra 1 linefeed at the end
    for intersection in intersection_coords:
        display[intersection[1]][intersection[0]] = "O"
    for line in display:
        print(line)
    print(sum(list(map(lambda x : x[0] * x[1], intersection_coords))))

def calc_index_zero(instruction, index, relative_base):
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
            input_value = int(input("Please input: "))
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