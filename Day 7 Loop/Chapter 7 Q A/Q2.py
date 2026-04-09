'write a program to find the factorial of first n numberes.(using for)'

n = int(input("Enter number: "))

fact = 1

# i = 1 
# while i <= n:
#    fact *= i
#    i += 1


for i in range (1, n+1):
    fact *= i

print("Factorial = ", fact)