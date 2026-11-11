# Example 1: A variable inside a function can't be seen outside it

def make_message():
    secret_message = "Hello from inside the function!"

make_message()
# print(secret_message)

# Error when the line above was run:
# Traceback (most recent call last):
#   File "C:\...\warmup3.py", line 7, in <module>
#     print(secret_message)
# NameError: name 'secret_message' is not defined


# Example 2: return sends the value out of the function

def make_message_fixed():
    secret_message = "Hello from inside the function!"
    return secret_message

message = make_message_fixed()
print(message)