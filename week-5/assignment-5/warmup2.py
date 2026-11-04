while True:
    user_input = input("Enter a positive integer: ")
    try:
        number = int(user_input)
        if number > 0:
            print(f"Got it: {number}")
            break
        else:
            print("That's not a positive integer. Try again.")
    except ValueError:
        print("That's not a positive integer. Try again.")
