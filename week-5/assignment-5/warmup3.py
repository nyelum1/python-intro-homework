names = ["Priya", "Eli", "Sara", "Marcus", "Mia", "Jazmine"]

target = input("Enter a name to search for: ")

found_index = -1

for i in range (len(names)):
    if names[i] == target:
        found_index = i
        break

if found_index != -1:
    print(f'Found  "{target}" at index {found_index}.')
else:
    print(f'"{target}" was not found in the list.')