base_input = [1,0,0,3,1,1,2,3,1,3,4,3,1,5,0,3,2,1,6,19,1,19,6,23,2,23,6,27,2,6,27,31,2,13,31,35,1,9,35,39,2,10,39,43,1,6,43,47,1,13,47,51,2,6,51,55,2,55,6,59,1,59,5,63,2,9,63,67,1,5,67,71,2,10,71,75,1,6,75,79,1,79,5,83,2,83,10,87,1,9,87,91,1,5,91,95,1,95,6,99,2,10,99,103,1,5,103,107,1,107,6,111,1,5,111,115,2,115,6,119,1,119,6,123,1,123,10,127,1,127,13,131,1,131,2,135,1,135,5,0,99,2,14,0,0]

#value in index 2 will determine the last 3 digits of the value in index 0.
#In order to get 19690720, the value in index 2 must be 0,10,20,30,40,50,60,70,80,90

#How this code works
#Binary check will deduce which noun will produce a 0-index value that has the same numbers after the hundredth place to 19690720
#If such a number is produced, that means the noun is correct.
#To find the verb, deduct the last 3 numbers of the produced value from 720. This is because we used 0 in our initial base_input.
#Therefore, the value 19690720 will definitely be larger than whatever that is produced from that specific noun.

#19690720

def main():
    print(binary_check(0,99))

def binary_check(start,end):
    input = base_input[:]
    midvalue = (start + end) // 2
    input[1],input[0] = midvalue,1
    key = calc_index_zero(input)
    if key // 1000 == 19690:
        return midvalue * 100 + 720 - key % 1000
    elif key // 1000 < 19690:
        return binary_check(midvalue + 1,end)
    else:
        return binary_check(start,midvalue)

def calc_index_zero(input):
    index = 0
    while input[index] != 99:
        if input[index] == 1:
            input[input[index + 3]] = input[input[index + 1]] + input[input[index + 2]]
        elif input[index] == 2:
            input[input[index + 3]] = input[input[index + 1]] * input[input[index + 2]]
        index += 4
    return input[0]

main()