# A list is a collection that can be changed (mutable)

nums =[1,2,3]
print("Original list:",nums)         # [1, 2, 3]

nums[0] = 100
print(nums)                          # [100, 2, 3]

nums.append(4)                       # append() add at end → [100,2,3,4]
print("After add 4 at end:",nums)

nums.reverse()                       # [100, 4, 3, 2]
print("After reverse:",nums)

nums.sort()                          # sort in ascending order [2, 3, 4, 100]
print("After sort:",nums)

nums.insert(1,10)
print("After insert 10 at index 1:",nums) # [2, 10, 3, 4, 100]

nums.remove(100)                          # remove value from list 
print("After remove 100:",nums)           #  [2, 10, 3, 4]

nums.pop()                                #pop() # remove last → [1,10,3]
print("After pop:",nums) 