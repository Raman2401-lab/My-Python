# write a program to accept marksof 6 student and display them in a sorted manner.

marks = []

M1 = int (input("Enter marks: "))
marks.append(M1)

M2 = int (input("Enter marks: "))
marks.append(M2)

M3 = int (input("Enter marks: "))
marks.append(M3)

M4 = int (input("Enter marks: "))
marks.append(M4)

M5 = int (input("Enter marks: "))
marks.append(M5)

M6 = int (input("Enter marks: "))
marks.append(M6)

marks.sort()

print(marks)