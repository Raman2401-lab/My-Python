# create an empty dictionary . Allow 4 friends to enter their favorite language as value and use key as their names. 
# Assume that the names are unique.

A = {}

name = input("Enter name of Friends: ")
lang = input("enter Language name: ")
A.update({name : lang})

name = input("Enter name of Friends: ")
lang = input("enter Language name: ")
A.update({name : lang})

name = input("Enter name of Friends: ")
lang = input("enter Language name: ")
A.update({name : lang})

name = input("Enter name of Friends: ")
lang = input("enter Language name: ")
A.update({name : lang})

print(A)