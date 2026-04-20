# Power Function (Recursion)

def power(x,n):
    if n == 0:
        return 1 
    return x * power(x, n-1)  # x^n = x * x^n−1

print(power(2,3))   


# power(2, 3)
# = 2 * power(2, 2)
# = 2 * (2 * power(2, 1))
# = 2 * (2 * (2 * power(2, 0)))
# = 2 * (2 * (2 * 1))
# = 8