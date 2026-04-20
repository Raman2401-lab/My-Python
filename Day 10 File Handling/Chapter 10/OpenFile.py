# if file is not in same folder, then give full path.
# if file is in same folder then you can give only name of file.

f = open(r"D:\Python COURSE\Day 10 File Handling\Chapter 10\demo.txt", "r")

data = f.read()   # reads entire file
print(data)
print(type(data))

f.close()        # always close file when you open 

