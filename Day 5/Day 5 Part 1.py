def main():
    base_input = readfile()
    return calc_index_zero(base_input)

def calc_index_zero(instruction):
    index = 0
    while instruction[index] != 99:
        #Guarenteed to be parameter mode
        if instruction[index] == 1:
            instruction[instruction[index + 3]] = instruction[instruction[index + 1]] + instruction[instruction[index + 2]]
            index += 4
        elif instruction[index] == 2:
            instruction[instruction[index + 3]] = instruction[instruction[index + 1]] * instruction[instruction[index + 2]]
            index += 4
        elif instruction[index] == 3:
            input_value = int(input("Please input 1: "))
            instruction[instruction[index + 1]] = input_value
            index += 2
        elif instruction[index] == 4:
            print(instruction[instruction[index + 1]])
            index += 2

        #Guarenteed to not be parameter mode
        else:
            modes = [0, 0]  # 0 for parameter mode, 1 for immediate mode. Left index for parameter 1, right index for parameter 2
            opcode = instruction[index]
            if opcode % 10 == 4:
                print(instruction[index + 1],index)
                index += 2
            else:
                modes[0], modes[1] = (opcode % 1000 - opcode % 100) // 100, opcode // 1000
                if opcode % 10 == 1:
                    instruction[instruction[index + 3]] = (instruction[instruction[index + 1]] if modes[0] == 0 else instruction[index + 1]) + (instruction[instruction[index + 2]] if modes[1] == 0 else instruction[index + 2])
                if opcode % 10 == 2:
                    instruction[instruction[index + 3]] = (instruction[instruction[index + 1]] if modes[0] == 0 else instruction[index + 1]) * (instruction[instruction[index + 2]] if modes[1] == 0 else instruction[index + 2])
                index += 4

    return instruction[0]

def readfile():
    with open ('input','r') as file:
        instruction = file.readline()[:-1].split(",")
    file.close()
    instruction = list(map(lambda x : int(x),instruction))
    return instruction

main()