def main():
    base_input = readfile()
    return calc_index_zero(base_input)

def calc_index_zero(instruction):
    index = 0
    while instruction[index] != 99:
        #Guarenteed to be position mode
        if instruction[index] == 3:
            input_value = int(input("Please input: "))
            instruction[instruction[index + 1]] = input_value
            index += 2
        #Might not be position mode
        else:
            opcode = instruction[index]
            modes = [0, 0]  # 0 for parameter mode, 1 for immediate mode. Left index for parameter 1, right index for parameter 2
            modes[0], modes[1] = (opcode % 1000 - opcode % 100) // 100, opcode // 1000
            if opcode % 10 == 4:
                print(instruction[index + 1]) if modes[0] == 1 else print(instruction[instruction[index + 1]])
                index += 2

            elif opcode % 10 == 5 or opcode % 10 == 6:
                first_para = instruction[instruction[index + 1]] if modes[0] == 0 else instruction[index + 1]
                if opcode % 10 == 5:
                    if first_para != 0:
                        index = instruction[instruction[index + 2]] if modes[1] == 0 else instruction[index + 2]
                    else:
                        index += 3
                else:
                    if first_para == 0:
                        index = instruction[instruction[index + 2]] if modes[1] == 0 else instruction[index + 2]
                    else:
                        index += 3

            elif opcode % 10 == 7 or opcode % 10 == 8:
                comp_values = [instruction[instruction[index + 1]] if modes[0] == 0 else instruction[index + 1], instruction[instruction[index + 2]] if modes[1] == 0 else instruction[index + 2]]
                #For the variable comp_values, index 0 is parameter 1, index 1 is parameter 2
                if opcode % 10 == 7:
                    instruction[instruction[index + 3]] = 1 if comp_values[0] < comp_values[1] else 0
                else:
                    instruction[instruction[index + 3]] = 1 if comp_values[0] == comp_values[1] else 0
                index += 4
            elif opcode % 10 == 1 or opcode % 10 == 2:
                if opcode % 10 == 1:
                    instruction[instruction[index + 3]] = (instruction[instruction[index + 1]] if modes[0] == 0 else instruction[index + 1]) + (instruction[instruction[index + 2]] if modes[1] == 0 else instruction[index + 2])
                if opcode % 10 == 2:
                    instruction[instruction[index + 3]] = (instruction[instruction[index + 1]] if modes[0] == 0 else instruction[index + 1]) * (instruction[instruction[index + 2]] if modes[1] == 0 else instruction[index + 2])
                index += 4

    return instruction[0]

def readfile():
    with open ('input','r') as file:
        instruction = file.readline().split(",")
    file.close()
    instruction = list(map(lambda x : int(x),instruction))
    return instruction

main()