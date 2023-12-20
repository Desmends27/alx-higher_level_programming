#!/usr/bin/python3
def best_score(a_dictionary):
    if a_dictionary is None:
        return None
    Max = 0
    best = None
    for i in a_dictionary:
        if a_dictionary[i] > Max:
            Max = a_dictionary[i]
            best = i
    return best
