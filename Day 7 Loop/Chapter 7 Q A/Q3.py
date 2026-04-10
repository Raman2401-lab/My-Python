# Remove last digit 

num = 1234

while num > 0:
    digit = num % 10
    print("Digit: ", digit)
    num = num // 10    # Remove last digit
                       # (num = 1234 // 10 = 123)
                       # (num = 123 // 10 = 12)
                       # (num = 12 // 10 = 1)
