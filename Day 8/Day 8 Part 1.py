def main():
    canvas = [[0 for i in range(25)] for j in range(6)]
    layers, layers_zeros, zero_count = [], [], 0
    image_data = readfile()
    image_data_degree = 10 ** (len(image_data) - 1)
    image_data = int(image_data)
    y_index, x_index = 0, 0
    while image_data_degree != 0:
        x_index %= 25
        canvas[y_index][x_index] = image_data // image_data_degree
        zero_count += 1 if canvas[y_index][x_index] == 0 else 0
        image_data %= image_data_degree
        image_data_degree //= 10
        x_index += 1
        if x_index == 25:
            if y_index == 5:
                layers.append(canvas)
                layers_zeros.append(zero_count)
                canvas = [[0 for i in range(25)] for j in range(6)]
                y_index, zero_count = 0, 0
            else:
                y_index += 1
    fewest_zeros_layer = layers[layers_zeros.index(min(layers_zeros))]
    ones_count, twos_count = 0, 0
    for line in fewest_zeros_layer:
        for number in line:
            if number == 1:
                ones_count += 1
            if number == 2:
                twos_count += 1
    return ones_count *twos_count



def readfile():
    with open("input","r") as file:
        return file.readline()

print(main())