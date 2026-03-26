# 1. Changing Case
print("1. String changing case: ")
text = "hello world"

print(text.upper())         # HELLO WORLD
print(text.lower())         # hello world
print(text.title())         # Hello World
print(text.capitalize())    # Hello world

# 2. Removing Spaces
print("2. String  Removing Spaces: ")
text = " hello "

print(text.strip())
print(text.lstrip())
print(text.rstrip())

# 3. Finding & Counting
print("3. Finding & Counting: ")
text = "banana"

print(text.find("b"))  # find give index 
print(text.count("a")) # 3

# 4. Replacing Text
print("4. Replacing Text: ")

text = "I like Java"

print(text.replace("Java","Python")) # I like Python


