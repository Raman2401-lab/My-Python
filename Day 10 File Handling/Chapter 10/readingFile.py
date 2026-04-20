

f = open(r"D:\Python COURSE\Day 10 File Handling\Chapter 10\demo.txt", "r")

# if you want specific number character read
# data = f.read(5)   # first 5 characters
# print(data)

line1 = f.readline()   # reads one line at a time
print(line1)


line2 = f.readline()   # reads one line at a time
print(line2)

f.close()