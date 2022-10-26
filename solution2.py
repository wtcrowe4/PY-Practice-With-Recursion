# Write code for algorithm 2 below
def count(x,y):
    if x > y:
        print('Please put the smaller number first')
        return
    if x == y:
        print(x)
    else:
        print(x)
        count(x+1,y)

count(10, 20)