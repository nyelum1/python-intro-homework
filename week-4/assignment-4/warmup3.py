list_a = ["Python", "JavaScript", "Java", "SQL"]
list_b = ["Python", "C++", "SQL", "Go"]

set_a = set(list_a)
set_b = set(list_b)

print("Union:     ", set_a | set_b)
print("Intersection: ", set_a & set_b)
print("Difference: ", set_a - set_b)