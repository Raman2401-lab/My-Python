# Character Frequency

s = "hello"

freq = {}

for ch in s:
    freq[ch] = freq.get(ch, 0) + 1 # freq.get(ch, 0) --> if character not present, take 0 (Add +1 every time character appears)

print(freq)