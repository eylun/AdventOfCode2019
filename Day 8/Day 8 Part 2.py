def main():
    canvas = [[0 for i in range(25)] for j in range(6)]
    layers = []
    image_data = readfile()
    image_data_degree = 10 ** (len(image_data) - 1)
    image_data = int(image_data)
    y_index, x_index = 0, 0
    while image_data_degree != 0:
        x_index %= 25
        canvas[y_index][x_index] = image_data // image_data_degree
        image_data %= image_data_degree
        image_data_degree //= 10
        x_index += 1
        if x_index == 25:
            if y_index == 5:
                layers.append(canvas)
                canvas = [[0 for i in range(25)] for j in range(6)]
                y_index = 0
            else:
                y_index += 1
    final_canvas =  generate_final_canvas(layers)
    for line in final_canvas:
        print(line)

def generate_final_canvas(layers):
    final_canvas = [[2 for i in range(25)] for j in range(6)]
    for layer in layers:
        x_index, y_index = 0, 0
        while y_index != 6:
            x_index %= 25
            if final_canvas[y_index][x_index] == 2:
                final_canvas[y_index][x_index] = layer[y_index][x_index]

            x_index += 1
            if x_index == 25:
                y_index += 1
    return final_canvas

def readfile():
    with open("input","r") as file:
        return file.readline()

main()