def main():
    base_input = readfile() + [0] * 999
    game_tile = [["" for i in range(42)] for j in range(24)]
    done = False
    index, relative_base = 0, 0
    player_score = 0
    ball_pos, paddle_pos = 0, 0
    tile_dict = {0 : " ", #Empty
                 1 : "W", #Wall
                 2 : "B", #Block
                 3 : "H", #Horizontal Paddle
                 4 : "O"} #Ball
    while not done:
        output = calc_index_zero(base_input, index, relative_base, game_tile, ball_pos, paddle_pos)
        #print(ball_pos, paddle_pos)
        if output == "done":
            done = True
        else:
            [tile_info, relative_base, index] = output
            [x_value, y_value, tile_id] = tile_info
            if x_value == -1 and y_value == 0:
                player_score = tile_id
            else:
                game_tile[y_value][x_value] = tile_dict[tile_id]
                if tile_id == 3:
                    paddle_pos = x_value
                elif tile_id == 4:
                    ball_pos = x_value
    block_count = 0
    for line in game_tile:
        block_count += len(list(filter(lambda x : x == "B", line)))
    print(player_score)
    return game_tile

def calc_index_zero(instruction, index, relative_base, game_board, ball_pos, paddle_pos):
    tile_info = []
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
            tile_info.append(instruction[instruction_index[0]])
            #print(instruction[instruction_index[0]])
            index += 2
            if len(tile_info) == 3:
                return [tile_info, relative_base, index]

        elif opcode == 3:
            for line in game_board:
                print(line)
            if ball_pos == paddle_pos - 1:
                input_value = -1
            elif ball_pos == paddle_pos + 1:
                input_value = 1
            else:
                input_value = 0
            print(ball_pos, paddle_pos)
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