'WAP to find a number if odd return string odd , if even return string even.'

n = int(input("Enter a number: "))

def Odd_Even(n):
    if n % 2 != 0:
        return '"ODD"'
    else:
        return '"EVEN"'

print(Odd_Even(n))
    