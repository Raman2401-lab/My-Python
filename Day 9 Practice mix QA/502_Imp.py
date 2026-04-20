# Remove Duplicates

nums = [1,2,2,3,4,4]
'''
# Using set()
unique = list(set(nums))
print(unique)
'''


result = []
for n in nums:
    if n not in result:     # checks duplicate
        result.append(n)    # append() --> (adds only unique values)

print(result)
