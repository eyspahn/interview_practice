#
# from https://www.careercup.com/question?id=5757912092770304
#
# Given an input of an an array of a string, verify if turned 180 degrees, it is the 'same'. For example:
# [1, 6, 0, 9, 1] -> return True
# [1, 7, 1] -> return False

def check180(input):
    """
    input = e.g. '1234'
    output = t or f, if it's same reversed.
    """
    input_reversed = input[::-1]
    if input_reversed == input:
        return True
    else:
        return False
