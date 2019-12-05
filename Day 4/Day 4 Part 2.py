def main():
    value_min, value_max = 145852, 616942
    passwords = []
    for code in range(145852, 616942):
        pair_checker = []
        pair_present = False
        temp_code = code
        prev = -1
        x = 5
        degree = 10 ** x
        while x > -1 and (prev <= temp_code // degree or prev == -1):
            prev = temp_code // degree
            temp_code %= degree
            x -= 1
            degree = 10 ** x
            if len(pair_checker) == 1 and prev != temp_code // degree:
                pair_present = True
            if x >= 0:
                if prev == temp_code // degree:
                    pair_checker.append(prev)
                if prev != temp_code // degree and len(pair_checker) != 0:
                    pair_checker = []

        if x == -1 and pair_present:
            passwords.append(code)
    return len(passwords)



print(main())