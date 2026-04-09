# Range functions returns a sequence of numbers, starting from 0 by default,
#  and increments by 1 (by default), and stops before a specified number.
'range (start?, stop, step? )' # step (how numch you want to increase)


#print(range(5))    # range(0, 5)

seq = range(5)

for i in seq:
    print(i)       # 0 1 2 3 4

for i in range(6):
    print(i)        # 0 1 2 3 4 5


for i in range(2, 10):       # range(start, stop)
    print(i)         # 2 3 4 5 6 7 8 9 


for i in range(2, 10, 2):       # range(start, stop, step)
    print(i)        # 2  4  6  8  