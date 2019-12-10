import math

def main():
    base_map = readfile()
    vectors = generate_all_vectors(base_map)
    asteroid_count_list = []
    asteroid_index_list = []
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
                asteroid_index_list.append((x, y))
    coordinates = asteroid_index_list[asteroid_count_list.index(max(asteroid_count_list))]
    lazer_vectors = list(filter(lambda x: 0 <= x[0] + coordinates[0] < length and 0 <= x[1] + coordinates[1] < height, vectors))
    vector_sort(lazer_vectors)
    print(zap(coordinates, lazer_vectors, base_map))
    return max(asteroid_count_list)

def zap(coordinates, vectors, base_map):
    count, vectors_len, vector_index, multiplier = 1, len(vectors), 0, 1
    [x, y] = coordinates
    height = len(base_map[0])
    length = len(base_map)
    zapped = [0, 0]
    while count != 201:
        x_vector, y_vector = vectors[vector_index]
        asteroid_x, asteroid_y = x + x_vector * multiplier, y + y_vector * multiplier
        if 0 <= asteroid_x <= length - 1 and 0 <= asteroid_y <= height - 1:
            if base_map[asteroid_y][asteroid_x] == "#":
                zapped[0], zapped[1] = asteroid_x, asteroid_y
                vector_index += 1
                multiplier = 1
                count += 1
                base_map[asteroid_y][asteroid_x] = "."
            else:
                multiplier += 1
        else:
            vector_index += 1
            multiplier = 1
        if vector_index == vectors_len - 1:
            vector_index = 0
            for map_line in base_map:
                print(map_line)
    return zapped[0] * 100 + zapped[1]

def vector_sort(vectors): #Sorts vectors from smallest angle to the vector (0,1) to the largest
    for i in range(len(vectors) ):
        for j in range(len(vectors) - i - 1):
            angle_store = [0, 0]
            for k in range(len(angle_store)):
                if vectors[j + k][0] <= 0 and vectors[j + k][1] > 0:
                    angle_store[k] = math.pi
                if vectors[j + k][0] >= 0 and vectors[j + k][1] < 0:
                    angle_store[k] = 0
                if vectors[j + k][0] < 0 and vectors[j + k][1] <= 0:
                    angle_store[k] = 3 * math.pi / 2
                if vectors[j + k][0] > 0 and vectors[j + k][1] >= 0:
                    angle_store[k] = math.pi / 2
            [curr, new] = angle_store
            if vectors[j] not in ((0, 1), (1, 0), (-1, 0), (0, -1)):
                if curr == math.pi / 2 or curr == 3 * math.pi / 2:
                    curr += math.pi / 2 - math.atan(abs(vectors[j][0]) / abs(vectors[j][1]))
                else:
                    curr += math.atan(abs(vectors[j][0]) / abs(vectors[j][1]))
            if vectors[j + 1] not in ((0, 1), (1, 0), (-1, 0), (0, -1)):
                if new == math.pi / 2 or new == 3 * math.pi / 2:
                    new += math.pi / 2 - math.atan(abs(vectors[j + 1][0]) / abs(vectors[j + 1][1]))
                else:
                    new += math.atan(abs(vectors[j + 1][0]) / abs(vectors[j + 1][1]))
            if curr > new:
                vectors[j], vectors[j + 1] = vectors[j + 1], vectors[j]

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
        temp = f.read().split("\n")
        f.close()
    new_list = []
    for line in temp:
        new_list.append(list(line))
    return new_list

main()
