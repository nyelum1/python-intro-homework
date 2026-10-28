# Day Palnner: suggests an activity based n day and time of day

day = input("What day is it? ").strip().lower()
time = input("What time of day? ").strip().lower()

# Check for unrecognized input first

if day  != "monday" and day != "tuesday" and day != "saturday":
    print("Sorry, I don't recognize that day. Try: Monday, Tuesday, or Saturday.")
elif time != "morning" and time != "afternoon" and time != "evening":
    print("Sorry, I don't recognize that time of day. Try: morning, afternoon, or evening.")

# Monday
elif day == "monday":
    if time == "morning":
        print("Suggestion: Plan your week and make a to-do list.")
    elif time == "afternoon":
        print("Suggestion: Knock out your toughest homework while you're fresh.")
    else:
        print("Suggestion: Go for a walk to shake off the Monday stress.")

# Tuesday
elif day == "tuesday":
    if time == "morning":
        print("Suggestion: Morning Python class - great time to focus!")
    elif time == "afternoon":
        print("Suggestion: Get outside - try a hike or a bike ride.")
    else:
        print("Suggestion: Perfect night for a movie or trying a new recipe.")


# Saturday
else:
    if time == "morning":
        print("Suggestion: Sleep in and enjoy a slow breakfast.")
    elif time == "afternoon":
        print("Suggestion: Get outside - try a hike or a bike ride.")
    else:
        print("Suggestion: Perfect night for a movie or trying a new recipe.")
