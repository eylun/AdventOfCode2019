



def main():
    sum = 0
    count = 1
    with open("input","r") as f:
        line = f.readline()[:-1]
        while line != "":
            if line[-1] == "\n":
                line = line[:-1]
            line = int(line)
            line = divide(line)
            sum += line
            count += 1
            line = f.readline()
        f.close()
    print(sum)

def divide(value):
    value //= 3
    value -= 2
    if value <= 0:
        return 0
    else:
        return value + divide(value)

main()