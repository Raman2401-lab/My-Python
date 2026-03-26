# tuple  = collection but immutable

a = (1,2,4)
print(type(a))      # <class 'tuple'>

b = (1,)
print(type(b))      # <class 'tuple'>

c = (1,45,342,False,"Rohan","Shivam")
print(type(c))      # <class 'tuple'>

# c[0] = 234
# print(c)            # error , tuple = immutable (can't change) 