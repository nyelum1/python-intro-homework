# Number Cruncher

numbers = [42, 17, 83, 5, 61, 29, 74, 8, 55, 93, 31, 66, 14, 47, 78, 3, 59, 22, 86, 40]

while True:
    print()
    print("=== Number Cruncher ===")
    print("1. Find minimum")
    print("2. Find maximum")
    print("3. Search for a number")
    print("4. Sort the list")
    print("5. Quit")
    choice = input("Choose an option (1-5): ").strip()

    # 1. Find minimum
    if choice == "1":
        smallest = numbers[0]
        for num in numbers:
            if num < smallest:
                smallest = num
        print(f"Minimum: {smallest}")

    # 2. Find maximum
    elif choice == "2":
        largest = numbers[0]
        for num in numbers:
            if num > largest:
                largest = num
        print(f"Maximum: {largest}")

    # 3. Search
    elif choice == "3":
        try:
            target = int(input("Enter a number to search for: "))
        except ValueError:
            print("Please enter a whole number.")
            continue

        found_index = -1
        for i in range(len(numbers)):
            if numbers[i] == target:
                found_index = i
                break

        if found_index != -1:
            print(f"Found {target} at index {found_index}.")
        else:
            print(f"{target} was not found in the list.")

    # 4. Bubble sort
    elif choice == "4":
        sorted_list = numbers.copy()
        swapped = True
        while swapped:
            swapped = False
            for i in range(len(sorted_list) - 1):
                if sorted_list[i] > sorted_list[i + 1]:
                    sorted_list[i], sorted_list[i + 1] = sorted_list[i + 1], sorted_list[i]
                    swapped = True
        print(f"Sorted list: {sorted_list}")

    # 5. Quit
    elif choice == "5":
        print("Goodbye!")
        break

    else:
        print("Invalid choice. Please enter a number from 1 to 5.")