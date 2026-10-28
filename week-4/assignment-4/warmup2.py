student = {
    "name": "Maria",
    "grade": 11,
    "subjects": ["Math",  "Biology", "English"]
}

# 1. Print each key-value pair
for key, value in student.items():
    print(f"{key}: {value}")

# 2. Add a new key
student["graduated"] = False

# 3. Print the updated dictionary
print(student)