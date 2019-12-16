import time

start_time = time.time()

def main():
    value = readfile()
    print(len(value) * 10000)
    value *= 10000
    offset = int("".join(map(str,value[0:7])))
    phase = 0
    pattern = [0 ,1, 0, -1]
    i = 0
    specified_pattern = []
    for x in pattern:
         specified_pattern += [x] * (offset)
    specified_pattern = specified_pattern[1:len(value) + 1]
    i_base = specified_pattern.index(1)
    int_value = list(map(int, value))
    while phase < 100:
        i = i_base
        new_value = [0] * i
        new_int_value = [0] * i
        sum_of_values = sum(int_value[i:])
        while i < len(value):
            pattern_value = sum_of_values % 10
            sum_of_values -= int_value[i]
            new_value.append(str(pattern_value))
            new_int_value.append(pattern_value)
            i += 1
        phase += 1
        value = new_value
        int_value = new_int_value
    print(value[offset:offset + 8])


def readfile():
    with open("input", "r") as f:
        value = f.read()
    f.close()
    output = []
    for char in value:
        output.append(char)
    return output
main()
print("Your code execution time is: ", time.time() - start_time)
