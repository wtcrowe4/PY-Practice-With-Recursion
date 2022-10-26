# Write code for algorithm 4 below
def exponent(x, n):
    if n == 0:
        return 1
    return x * exponent(x, n-1)

print(exponent(2, 10))