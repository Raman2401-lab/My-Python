# Sum of Digits

num = 1234

total = 0

while num > 0:
    total += num % 10 
    num = num // 10    # ( //10 = remove last digit )

print("Sum of Digits:", total)