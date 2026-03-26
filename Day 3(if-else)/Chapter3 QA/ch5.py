num = 27

if num > 10 and num < 50 and not (num % 5 == 0):
    print("Valid number")
else:
    print("Invalid number")

# num > 10 → True
# num < 50 → True
# num % 5 == 0 → False (27 not divisible by 5)
# not False → True

# Final: True and True and True → ✅ True