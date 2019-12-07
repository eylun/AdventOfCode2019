def main():
    base_input = readfile()
    instruction_memory = []
    signals = []
    amp_index = []

    def feedback_loop(instructions, amp_input, indexes):
        done = False
        count, output = 0, amp_input
        prev = amp_input
        while not done:
            count %= 5
            prev = output
            temp_output = calc_index_zero(instructions[count], output, 0, indexes[count], False)
            if temp_output == "Done":
                done = True
            else:
                output, indexes[count] = temp_output[0], temp_output[1]
                count += 1
        signals.append(prev)

    def helper_base_recursion(phases, amp_input):
        if len(phases) == 1:
            copy_input = base_input[:]
            new_amp_output = calc_index_zero(copy_input, amp_input, phases[0], 0, True)
            amp_index.append(new_amp_output[1])
            instruction_memory.append(copy_input[:])
            new_memory = []
            for memory in instruction_memory:
                new_memory.append(memory[:])
            feedback_loop(new_memory, new_amp_output[0], amp_index[:])
            #print(amp_input, instruction_memory[0])
            amp_index.pop(-1)
            instruction_memory.pop(-1)
        else:
            for i in range(len(phases)):
                copy_input = base_input[:]
                temp_phases = phases[:]
                base_phase_input = temp_phases.pop(i)
                new_amp_output = calc_index_zero(copy_input, amp_input, base_phase_input, 0, True)
                instruction_memory.append(copy_input[:])
                amp_index.append(new_amp_output[1])
                helper_base_recursion(temp_phases, new_amp_output[0])
                amp_index.pop(-1)
                instruction_memory.pop(-1)

    helper_base_recursion([5, 6, 7, 8, 9], 0)
    largest_signal = max(signals)

    return largest_signal



def calc_index_zero(instruction, amp_input, phase_input, starting_index, first_time):
    index = starting_index
    while instruction[index] != 99:
        #Guarenteed to be position mode
        if instruction[index] == 3:
            if first_time:
                input_value = phase_input
                first_time = False
            else:
                input_value = amp_input
            instruction[instruction[index + 1]] = input_value
            index += 2
        #Might not be position mode
        else:
            opcode = instruction[index]
            modes = [0, 0]  # 0 for parameter mode, 1 for immediate mode. Left index for parameter 1, right index for parameter 2
            modes[0], modes[1] = (opcode % 1000 - opcode % 100) // 100, opcode // 1000
            if opcode % 10 == 4:
                output_value = instruction[index + 1] if modes[0] == 1 else instruction[instruction[index + 1]]
                #print(output_value)
                index += 2
                return [output_value, index]

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

    return "Done"

def readfile():
    with open ('input','r') as file:
        instruction = file.readline().split(",")
    file.close()
    instruction = list(map(lambda x : int(x),instruction))
    return instruction

print(main())