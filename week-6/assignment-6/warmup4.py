def is_valid_score(score):
    return isinstance(score, int) and 0 <= score <= 100


try:
    user_score = int(input("Enter a score: "))
except ValueError:
    user_score = None

if is_valid_score(user_score):
    print("Valid score.")
else:
    print("Invalid score — must be between 0 and 100.")