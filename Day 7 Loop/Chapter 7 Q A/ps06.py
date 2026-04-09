'Search for a number x in this tuple using loop:'
'[1, 4, 9, 16, 25, 36, 49, 64, 81, 100]'

tuple = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100, 49]

x = int(input("Enter val of x: "))

idx = 0
for val in tuple:
    if (val == x):
        print("X found at idx", idx)
    idx += 1

    