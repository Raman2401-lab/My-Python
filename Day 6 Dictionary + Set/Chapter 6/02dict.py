
marks ={#key   : values 
        "Raman": 99,
        "Shyam": 56,
        "Rohan": 23,
        0 : "Ajay"
}

# print(marks.items())
# print(marks.keys())

print(marks.values())

#marks.update({"Rohan":35})
marks.update({"Rohan":35, "Rani":70})
print(marks)

print(marks.get("Raj"))    # None
print(marks.get("Rohan"))  # 35 

print(marks["Rohan2"])      # return error bcs key doesn't exist.