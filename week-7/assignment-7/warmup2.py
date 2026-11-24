import csv

with open("../data/students.csv", "r", newline="") as file:
    reader = csv.DictReader(file)
    for row in reader:
        print(f"{row['name']}: {row['score']}")