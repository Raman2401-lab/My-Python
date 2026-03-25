# 5. Checking Content
print("5. Checking Content: ")
text = "Hello123"

print(text.isalpha()) # False
#  isalpha() Checks: Only letters (A–Z, a–z), but here numbers also 

print(text.isdigit()) # False
# isdigit() Checks: Only digits (0–9), but here letter also

print(text.isalnum()) # True
# isalnum() Checks: Letters + Numbers (no symbols, no spaces)

print(text.islower()) # False
# islower() Checks: All letters are lowercase

print(text.isupper()) # False 
# isupper() Checks: All letters are uppercase


# 6. Splitting & Joining
print("6. Splitting & Joining: ")
text = "apple,banana,mango"

# split() → String ➝ List
print(text.split(",")) # ['apple', 'banana', 'mango']

# join() → List ➝ String
text = ['Hi', 'hello']
print("".join(text))  # Hihello
print(" ".join(text)) # Hi hello

# 7. Checking Start/End
print("7. Checking Start/End: ")

text = "Raman"

print(text.startswith("Ra"))   # True
print(text.startswith("an"))   # False

print(text.endswith("m"))      # False
print(text.endswith("an"))     # True

print("Check in String: ")
print("am" in text)   # True
print("xy" in text)   # False

# 8. Length Function
print("8. Length Function: ")
text = 'Raman'
print(len(text))      # 5

text = 'Raman ghule'
print(len(text))      # 11