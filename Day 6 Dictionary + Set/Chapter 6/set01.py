# Set Methods (Operations)

s = {1,2,3}
print(s)             # {1, 2, 3}

''' 1. Add Elements '''
s.add(4)             # {1, 2, 3, 4}
#print(s)

''' 2. Remove Elements '''
s.remove(2)          # {1, 3, 4}  
# s.remove(10)       # error, if value not found 
# s.pop()            # removes random element
#print(s)        

''' 3.Clear Set ''' 
# s.clear()            # removes all elements
# print(s)  

''' 4. Copy Set '''    
new_set_A = s.copy()   # {1, 3, 4}
#print(new_set_A)    

''' 5. Union (Combine Sets) '''   
a = {1,2,3}
b = {3,4,5}

print(a.union(b))  # {1, 2, 3, 4, 5}, remove duplicate and add 
#  OR
print(a | b)       # {1, 2, 3, 4, 5}

''' 6. Intersection (Common Elements) '''
print(a.intersection(b))   # {3}
#   OR 
print(a & b)               # {3}


''' 7. Difference '''
print(a.difference(b))     # {1,2}, diff = not common
# OR
print(a - b)               # {1,2}

''' 8. Symmetric Difference '''
# Elements in either set but NOT both
print(a.symmetric_difference(b))   # {1, 2, 4, 5} NOT common 
# OR
print(a ^ b)  # {1, 2, 4, 5}

''' 9. Subset / Superset '''
p = {1,2}
q = {1,2,3}

print(p.issubset(q))   # True
print(p.issuperset(q)) # False

print(q.issuperset(p)) # True

''' 10. Disjoint Sets '''
m = {1,2}
n = {3,4}

print(m.isdisjoint(n)) # True



