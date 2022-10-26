# Write code for algorithm 1 below
def countDown(n):
    if n < 0:
        print('Please use a positive number')
        return
    if n == 0:
        print("Blastoff!")
    else:
        print(n)
        countDown(n-1)


countDown(10)