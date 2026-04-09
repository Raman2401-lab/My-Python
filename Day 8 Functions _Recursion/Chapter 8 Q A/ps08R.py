'Write a recursive function to print all elements in a list.'
# Hint: use list & index as parameters.

Alpha = ["a", "b", "c", "d", "e"]


def print_List(list, idx=0):
    if (idx == len(list)):
        return 
    print(list[idx])
    print_List(list, idx+1)

print_List(Alpha)