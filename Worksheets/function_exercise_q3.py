# -*- coding: utf-8 -*-

def check_upper_lower(x):
    """
    Counts the number of upper case letters and lower case letter
    in string x and returns the numbers as a list [upper, lower].
    If x is not a string, returns 'ValueError, string expected!'.
    """
    if not isinstance(x, str):
        return 'ValueError, string expected!'
    else:
        upper = 0
        lower = 0
        for i in x:
            if i.isupper():
                upper += 1
            elif i.islower():
                lower += 1
        return [upper, lower]
