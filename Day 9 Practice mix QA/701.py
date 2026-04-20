# Check function number is prime 

def is_prime(n):
    if n < 2:
        return False
    
    for i in range(2, n):
        if n % i == 0:
            return False

    return True

print(is_prime(27))

# without function 

n = int(input("Enter number: "))

if n < 2:
    print("Not prime")
else:
    for i in range(2, n):
        if n % i == 0:
            print("Not prime")
            break
    else:
        print("Prime")
