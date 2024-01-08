#!/usr/bin/python3
""" Simple list class """


class MyList(list):
    """
    This module sorts a list and prints it back
    """
    def print_sorted(self):
        temp = self.copy()
        temp.sort()
        print(temp)
