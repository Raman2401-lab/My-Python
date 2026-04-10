# First Non-Repeating Character

s = "swiss"

for ch in s:
    if s.count(ch) == 1:  # here Character count == 1 print. (repeated character count is more than 1)
        print(ch)
        break       # when got first ch break works , get only first (if you don't write break you got all non repeating  ch) 