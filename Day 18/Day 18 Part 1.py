def main():
    grid, lock_dict, key_dict, start_pos = readfile()
    for line in grid:
        print(line)








def readfile():
    lock_dict = {}
    key_dict = {}
    full_grid = []
    start_point = []
    with open("input","r") as f:
        line = f.readline().strip("\n")
        depth = 0
        length = 0
        while line != "":
            for char in line:
                if char not in ("#", "."):
                    if 97 <= ord(char) <= 122:
                        key_dict[char] = (length, depth)
                    elif 65 <= ord(char) <= 90:
                        lock_dict[char] = (length, depth)
                    if char == "@":
                        start_point = [length, depth]
                length += 1
            length = 0
            depth += 1
            full_grid.append(list(line))
            line = f.readline().strip("\n")
    f.close()
    return (full_grid, lock_dict, key_dict, start_point)


main()