def main():
    value_min, value_max = 145852, 616942
    passwords = [] #Storing passwords in case part 2 requires them
    for code in range(145852, 616942):
        consecutive_present = False
        temp_code = code
        prev = -1
        x = 5
        degree = 10 ** x
        while x > -1 and (prev <= temp_code // degree or prev == -1):
            prev = temp_code // degree
            temp_code %= degree
            x -= 1
            degree = 10 ** x
            if prev == temp_code // degree:
                consecutive_present = True
        if x == -1 and consecutive_present:
            passwords.append(code)
    print(passwords)
    return len(passwords)



print(main())