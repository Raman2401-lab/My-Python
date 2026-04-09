# Recursion = a function calling itself 
''' Every recursive function must have :
        1. Base Case --> stop the function
        2. Recursive Call --> function calls itself
'''

# Q. Print numbers 1 to 5
def printNum(n):
    if n == 6:         # base case (stop)
        return
    print(n)
    printNum(n + 1)    # recursive call

printNum(1) 


print("Another Q A")


# Q.prints n to 1 backward
def show(n):
    if (n == 0):         # base case (stop)
        return
    print(n)
    show(n-1)            # recursive call
    
show(5)  # 5, 4= n-1, 3= n-2, 2= n-3, 1
