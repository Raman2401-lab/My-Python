# number is divisible by 3 and 5 

num = int(input("Enter num : "))

if(num % 3 == 0 and num % 5 == 0):
    print("FizzBuzz")
else:
    print("Not divisible by one off them")
