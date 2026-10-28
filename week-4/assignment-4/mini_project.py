# Student Roaster Analyzer

# Paste the students list from week-4/data/roaster.py here
students = [
    {"name": "Jazmine", "score": 88, "subject": "Python"},
    {"name": "Luis",    "score": 74, "subject": "Data"},
    {"name": "Sara",    "score": 91, "subject": "Python"},
    {"name": "Marcus",  "score": 68, "subject": "Web"},
    {"name": "Priya",   "score": 95, "subject": "Data"},
    {"name": "Devon",   "score": 72, "subject": "Python"},
    {"name": "Mia",     "score": 83, "subject": "Web"},
    {"name": "Eli",     "score": 79, "subject": "Data"},
]

# 1. Top scorer
top_name = students[0]["name"]
top_score = students[0]["score"]
for student in students:
    if student["score"] > top_score:
        top_score = student["score"]
        top_name = student["name"]

# 2. Class average
total = 0
for student in students:
    total += student["score"]
average = total / len(students)

# 3. Unique subjects
subjects = set()
for student in students:
    subjects.add(student["subject"])

# 4. High scorers
high_scorers = []
for student in students:
    if student["score"] > 75:
        high_scorers.append(student["name"])

print (f"Top scorer:        {top_name}  ({top_score})")
print (f"Class average:     {average:.2f}")
print (f"Subjects offered:  {subjects}")
print (f"High scorers:      {high_scorers}")
