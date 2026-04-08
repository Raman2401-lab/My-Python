# A Dictionary stores data in key-value pairs  (like map)

student = {
    #key    : values 
    "name"  : "Raman",
    "age"   : 22,
    "marks" : 85
}

# 1. type
print(student, type(student))

print(student["name"])    # Raman

# 2. Add / Update
student["city"] = "Pune"

# 3. get value safely
print(student.get("age"))

# 4. check key exists
if "sham" in student:
    print("Yes")
else:
    print("No")

print(student)

# 5.Length
print(len(student))

# 6.Copy Dictionary
new_std = student.copy()   # {'name': 'Raman', 'age': 22, 'marks': 85, 'city': 'Pune'}
print("new_std:- ",new_std) 

# 7. Merge Dictionaries 
collage ={
    "C_name" : "Dy patil"
}

student.update(collage)  # {'name': 'Raman', 'age': 22, 'marks': 85, 'city': 'Pune', 'C_name': 'Dy patil'}
print("After merge: ",student)

# 8. Get All keys / values
print(student.keys())   # dict_keys(['name', 'age', 'marks', 'city', 'C_name'])
print(student.values()) # dict_values(['Raman', 22, 85, 'Pune', 'Dy patil'])  
print(student.items())  # dict_items([('name', 'Raman'), ('age', 22), ('marks', 85),
#                                       ('city', 'Pune'), ('C_name', 'Dy patil')])

# 9 Remove item safely
student.pop("city", None) 
print("After pop:",student)