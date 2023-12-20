#!/usr/bin/python3
def roman_to_int(roman_string):
    '''Roman numeral conversion'''
    if roman_string is None or not isinstance(roman_string, str):
        return 0
    roman_dict = {"M": 1000, "D": 500, "C": 100, "L": 50,
                  "X": 10, "V": 5, "I": 1, "0": 0}
    prev = "0"
    num = 0
    for i in roman_string:
        if i not in roman_dict:
            return 0
        if roman_dict[i] > roman_dict[prev]:
            num += roman_dict[i] - 2 * roman_dict[prev]
        else:
            num += roman_dict[i]
        prev = i
    return num
