def main():
    base_map = readfile()
    print(base_map)
    vectors = generate_all_vectors(base_map)
    print(vectors)
    asteroid_count_list = []
    asteroid_positions = []
    height = len(base_map[0])
    length = len(base_map)
    vectors_len = len(vectors)
    for y in range(height):
        for x in range(length):
            if base_map[y][x] == "#":
                asteroid_count, vector_index, multiplier = 0, 0, 1
                while vector_index != vectors_len:
                    x_vector, y_vector = vectors[vector_index]
                    asteroid_x, asteroid_y = x + x_vector * multiplier, y + y_vector * multiplier
                    if 0 <= asteroid_x <= length - 1 and 0 <= asteroid_y <= height - 1:
                        if base_map[asteroid_y][asteroid_x] == "#":
                            asteroid_count += 1
                            vector_index += 1
                            multiplier = 1
                        else:
                            multiplier += 1
                    else:
                        vector_index += 1
                        multiplier = 1

                asteroid_count_list.append(asteroid_count)
                asteroid_positions.append((x, y))
    print(asteroid_positions[asteroid_count_list.index(max(asteroid_count_list))])
    return max(asteroid_count_list)

def generate_all_vectors(map):
    vectors = []
    row_index_length = len(map[0]) - 1
    column_index_length = len(map) - 1
    x = 0 - row_index_length
    y = 0 - column_index_length
    while not (x == row_index_length and y == column_index_length):
        if not (x == 0 and y == 0):
            if x == 1 or x == -1 or y == 1 or y == -1:
                vectors.append((x,y))
            elif x != 0 and y != 0:
                if not common_factor(x, y):
                    if -1 <= x <= 1 or -1 <= y <= 1:
                        vectors.append((x,y))
                else:
                    vectors.append((x,y))
        if x == row_index_length:
            y += 1
            x = 0 - row_index_length
        else:
            x += 1
    return vectors

def common_factor(x, y): #Returns True if the only common factor is 1, else False
    count = 2
    x, y = abs(x), abs(y)
    while count <= x and count <= y:
        if (x / count).is_integer() and (y / count).is_integer():
            return False
        count += 1
    return True

def readfile():
    with open("input","r") as f:
        return f.read().split("\n")


main()
