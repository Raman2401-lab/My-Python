


f = open(r"D:\Python COURSE\Day 10 File Handling\Chapter 10\demo.txt ", "w")
f.write("this is a new line, which is overwiten by w.")
f.close

# to add more in this file. use apend ( a )
f = open(r"D:\Python COURSE\Day 10 File Handling\Chapter 10\demo.txt ", "a")
f.write("\nthis line is add by using append (a)")  # for new line \n
f.close


# for read
f = open(r"D:\Python COURSE\Day 10 File Handling\Chapter 10\demo.txt", "r")
data = f.read()
print(data)


# when you open file in mode w /a , OR if file not exist, Python will create file for you.
f = open("sample.txt", "w")    # YOU will see file in your folder structure 
f.close()

