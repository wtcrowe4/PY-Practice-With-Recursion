# Write code for algorithm 3 below
def fibonacci(n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    return fibonacci(n-1) + fibonacci(n-2)

print(fibonacci(10))
n = 10
for i in range(n+1):
    print(fibonacci(i))

