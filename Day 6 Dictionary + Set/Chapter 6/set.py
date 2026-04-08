# A Set stores unique values only (no duplicates)
# Set is a collection of non-repetitive elements.

s = {1,2,3,4}   # Set 

# s = (1,2,3,4)   ❌ Without {} -> Python treats it as tuple
# s = { } this is NOT a Set -> it is dictionary

T = {1, 2, 32, 54, "Jack"}
print(T,type(T))   # <class 'set'>

A = set() # correct way to write empty set

''' Remember 
            {}    -> Dictionary
            {1,2} -> Set
            (1,2) -> Tuple
'''

#         ----- PROPERTIES OF SETS -----
# 1. Sets are inordered => element's order doesn't matter
# 2. Sets are unindexed => can not access elements by index
# 3. there is no way to change items in sets.
# 4. Sets can not contain dupliccate values.


