# Interleave list of lists in Java
# Example:
# input = [[1,2,3], [9, 0], [5], [-4,-5,-2,-3,-1]];
# output = [1,9,5,-4,2,0,-5,3,-2,-3,-1]
#
# Obvs, I'm doing this in python...
#
# https://stackoverflow.com/questions/7946798/interleaving-two-lists-in-python/40954220?utm_medium=organic&utm_source=google_rich_qa&utm_campaign=google_rich_qa


from itertools import chain, zip_longest

def list_interleave(input)
    """
    input: list of lists to interleave
    output: single list of interleaved elements
    """

    return [x for x in chain(*zip_longest(*input)) if x is not None]
