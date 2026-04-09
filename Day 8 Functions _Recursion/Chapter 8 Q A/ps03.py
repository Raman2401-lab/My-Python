# write a program to find factorial of n.(n is the parameter)

n = int(input("enter n : "))

# fact = 1
# for i in range(1, n + 1):
#     fact *= i
# print(fact)

def cal_fact(n):
    fact = 1
    for i in range(1, n + 1):
        fact *= i
    return fact

print(cal_fact(n))  