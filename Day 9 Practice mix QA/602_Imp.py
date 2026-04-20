# Find Duplicates 

nums = [1,2,3,2,4,1]

seen = set()
duplicates = set()

for n in nums:
    if n in seen:
        duplicates.add(n)
    else:
        seen.add(n)

print(list(duplicates))
# print(list(seen))