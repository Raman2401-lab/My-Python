# Write a program to find the greatest of four numbers entered by the user.

n1 = int(input("Enter number1: "))
n2 = int(input("Enter number2: "))
n3 = int(input("Enter number3: "))
n4 = int(input("Enter number4: "))

if(n1 > n2 and n1 > n3 and n1 > n4 ):
    print(" n1 is greatest numbeer" )

elif(n2 > n1 and n2 > n3 and n2 > n4 ):
    print(" n2 is greatest numbeer" )

elif(n3 > n2 and n3 > n1 and n3 > n4 ):
    print(" n3 is greatest numbeer" )

elif(n4 > n2 and n4 > n3 and n4 > n1 ):
    print(" n4 is greatest numbeer" )


