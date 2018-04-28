#
# From Goodrich's Data Structures & Algorithms sec 4.4
#
# we want to calculate power(x, n) = x^n
# Note x^n = x*x^(n-1)

def power(x, n):
    if n==0:
        return 1
    else:
    return x*power(x,n-1)
