total = 0

for i in range(1, 6):
    marks = int(input(f"Enter marks of subject {i}: "))
    total = total + marks

percentage = (total / 500) * 100

if percentage >= 80:
    grade = "A"
elif percentage >= 70:
    grade = "B"
elif percentage >= 60:
    grade = "C"
elif percentage >= 50:
    grade = "D"
else:
    grade = "F"

print("\nTotal Marks:", total)
print("Percentage:", percentage, "%")
print("Grade:", grade)

if percentage >= 50:
    print("Result: Pass")
else:
    print("Result: Fail")