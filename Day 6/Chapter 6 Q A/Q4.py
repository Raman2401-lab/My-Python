# What will be the length of following set s:
#    s = set()
#    s.add(20)
#    s.add(20.0)
#    s.add('20') # length of s after the operation


s = set()

s.add(20)
s.add(20.0)  # NOT added (because 20 == 20.0)
s.add('20')

print(len(s))  
print(s) 

# int and float with same value are treated as same