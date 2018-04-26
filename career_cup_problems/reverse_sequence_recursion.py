#
# From Goodrich's Data Structures & Algorithms sec 4.4
#
# Reversing a sequence with recursion
# Switch the first and last element of sequence.
# Then move to the second and next to last element and switch them.
# recursively switch ending elements until you can't anymore.

def reverse(S, start, stop):
    if start < stop - 1:    # if at least 2 elements in list
        S[start], S[stop-1] = S[stop-1], S[start]   # swap first and last
        reverse(S, start+1, stop-1)         # recur on the rest
    return S
