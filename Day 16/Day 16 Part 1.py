def main():
    value = readfile()
    offset = value[0:7]
    print(offset)
    phase = 0
    pattern = [0 ,1, 0, -1]
    while phase < 100:
        new_value = []
        pattern_index = 1
        for i in range(len(value)):
            new_pattern = []
            for x in pattern:
                new_pattern += [x] * (i + 1)
            if len(new_pattern) < len(value) + 1:
                new_pattern *= len(value) // len(new_pattern) + 1
            # print(value)
            #print(new_pattern[1:len(value) + 1])
            #print(abs(sum(list(map(lambda x, y : x * int(y), new_pattern[1:len(value) + 1], value)))))
            pattern_value = abs(sum(list(map(lambda x, y : x * int(y), new_pattern[1:len(value) + 1], value)))) % 10
            #print(pattern_value)
            pattern_index += 1
            pattern_index %= 4
            new_value.append(str(pattern_value))
        value = new_value
        #print('--------')
        #print(value)
        phase += 1
    print(value[:8])


def readfile():
    with open("input", "r") as f:
        value = f.read()
    f.close()
    output = []
    for char in value:
        output.append(char)
    return output
main()