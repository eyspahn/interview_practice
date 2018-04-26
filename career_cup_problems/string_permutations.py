#
# Write a method to compute all the permutations of a string.
#
# From the recursion section in Cracking the Coding Interview.
# https://stackoverflow.com/questions/13109274/python-recursion-permutations?utm_medium=organic&utm_source=google_rich_qa&utm_campaign=google_rich_qa
#

# from itertools import permutations
#
# def get_perms(s):
#     return permutations(s)

def rec_get_permutations(s):
    if len(s)==1:
        return [s]

    perm_list = []
    for a in s:
        remaining_elements = [x for x in s if x != a]
        z = rec_get_permutations(remaining_elements)

        for t in z:
            perm_list.append([a]+t)
            
    return perm_list
