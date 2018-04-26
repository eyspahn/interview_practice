# Write a method to generate the nth fibonacci number
# Cracking the Coding Interview

# Are they asking: given n, return the nth number?

def nth_fib(n):
    """
    input: n = an integer
    output: nth fib number, also integer.
    """

    if n==0:
        return 0
    elif n==1:
        return 1
    else:
        return nth_fib(n-2)+nth_fib(n-1)
