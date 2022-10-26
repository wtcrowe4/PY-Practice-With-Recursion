# Greatest Common Denominator

def gcd(a, b):
    if b == 0:
        return a
    else:
        return gcd(b, a % b)


print(gcd(12, 8))
print(gcd(12, 9))
print(gcd(30, 15))