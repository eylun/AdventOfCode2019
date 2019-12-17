def main():
    print(ord("8"))
    base_input = readfile() + [0] * 1250
    part_2_input = base_input[:]
    part_2_input[0] = 2
    index, relative_base = 0, 0
    done = False
    display, inner_display = [], []
    depth, length = 0, 0
    intersection_coords = []
    curr_point = []
    while not done:
        output = calc_index_zero(base_input, index, relative_base, "")
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
                if inner_display[length] in ["^", "<", "v", ">"]:
                    curr_point = [depth, length]
                if len(inner_display) >= 3 and depth >= 1:
                    if inner_display[length] == "#" and inner_display[length - 1] == "#" and inner_display[length - 2] == "#":
                        focus_x = length - 1
                        if display[depth - 1][focus_x] == "#":
                            intersection_coords.append((focus_x, depth))
                length += 1
    display = display[:-1] #Gets rid of the extra 1 linefeed at the end
    for intersection in intersection_coords:
        display[intersection[1]][intersection[0]] = "O"
    text_directions = move_vacuum_bot(display, curr_point)
    instructions = generate_A_B_C(text_directions)
    for instruction in instructions:
        instruction.append("\n")
    part2done = False
    part2index, part2relativebase = 0, 0
    part2instructionindex = 0
    while part2instructionindex < 4:
        [output, part2index, part2relativebase] = calc_index_zero(part_2_input, part2index, part2relativebase, instructions[part2instructionindex])
        part2instructionindex += 1
        print(output)

def generate_A_B_C(text_directions):

    def helper_recursion(reductible):
        index = 0
        track_string = ""
        done = False
        space_broken = False
        while track_string in reductible[index:] or index == 0:
            if reductible[index] == " " and track_string != "":
                space_broken = True
                break
            if reductible[index] != " ":
                track_string += reductible[index]
            index += 1
        collection = []
        while not done:
            new_string = reductible
            if not space_broken:
                for j in range(len(track_string) - 1, -1, -1):
                    if track_string[j].isalpha():
                        track_string = track_string[0:j]
                        break
            space_broken = False
            if len(track_string) == 0:
                break
            new_string = reductible.replace(track_string, " ")
            if "L" not in new_string and "R" not in new_string:
                break
            new = [track_string,] + helper_recursion(new_string)
            collection.append(new)
        minimum = 10
        focus = [track_string,]
        for item in collection:
            if len(item) < minimum:
                focus = item
                minimum = len(item)
        return focus

    instructions = helper_recursion(text_directions)
    index = 0
    instruction_dict = {0 : "A",
                        1 : "B",
                        2 : "C"}
    final_instructions = []
    temp_string = ""
    while index < len(text_directions):
        temp_string += text_directions[index]
        if temp_string in instructions:
            final_instructions.append(instruction_dict[instructions.index(temp_string)])
            temp_string = ""
        index += 1

    return [final_instructions, list(instructions[0]), list(instructions[1]), list(instructions[2])]



def move_vacuum_bot(grid, current):
    direction_dict = {"v" : [(0, -1),(0, 1)],
                      ">" : [(1, 0),(-1, 0)],
                      "^" : [(0, 1),(0, -1)],
                      "<" : [(-1, 0),(1, 0)],}
    done = False
    curr_direction = grid[current[0]][current[1]]
    text_dir_final = ""
    next_spot = []
    while not done:
        potential_directions = direction_dict[curr_direction]
        focus_dir = []
        text_dir = ""
        for x in range(len(potential_directions)):
            next_spot = [current[0] + potential_directions[x][0], current[1] + potential_directions[x][1]]
            if grid[next_spot[0]][next_spot[1]] == "#":
                focus_dir = potential_directions[x]
                text_dir = "L" if x == 1 else "R"
                if focus_dir == (-1, 0):
                    curr_direction = "^"
                if focus_dir == (1, 0):
                    curr_direction = "v"
                if focus_dir == (0, 1):
                    curr_direction = ">"
                if focus_dir == (0, -1):
                    curr_direction = "<"
                break
        movement_counter = 0
        movement_done = False
        while 0 <= next_spot[0] < len(grid) and 0 <= next_spot[1] < len(grid[0]) and not movement_done:
            if grid[next_spot[0]][next_spot[1]] != ".":
                current = next_spot
                movement_counter += 1
                next_spot = [current[0] + focus_dir[0], current[1] + focus_dir[1]]
            else:
                movement_done = True
        text_dir += str(movement_counter) if movement_counter != 0 else ""
        text_dir_final += text_dir
        if len(focus_dir) == 0:
            done = True
    return text_dir_final



#L4L4L10R4R4L4L4R8R10L4L4L10R4R4L10R10L4L4L10R4R4L10R10R4L4L4R8R10R4L10R10R4L10R10R4L4L4R8R100

def calc_index_zero(instruction, index, relative_base, input_value):
    print(input_value)
    ins_index = 0
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
            print(ins_index, input_value)
            instruction[instruction_index[0]] = ord(input_value[ins_index])
            index += 2
            ins_index += 1

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

#generate_A_B_C("".join(['R','8','R','8','R','4','R','4','R','8','L','6','L','2','R','4','R','4','R','8','R','8','R','8','L','6','L','2']))