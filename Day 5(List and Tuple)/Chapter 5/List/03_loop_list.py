
list = [10, 20, 30, 40]

print(list[0])
print(list[-1])

for i in list:
    print(i)

print(*list)

# custom separator 
print(*list, sep=", ")

# using join() (for string only)
words =["hi", "hello"]
print(" ".join(words)) # here it make list to string

# using Loop 
for i in list:
    print(i, end="   ")