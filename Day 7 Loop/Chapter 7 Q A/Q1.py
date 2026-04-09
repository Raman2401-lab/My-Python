' Write a program to find the sum of first n natural numbers.(using while) '

n = int(input("Enter number: "))

sum = 0

i = 1
while i <= n:
   sum += i
   i += 1

# for i in range(1, n + 1):
#    sum += i

print("total sum : ", sum)