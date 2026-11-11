def greet(name, greeting="Hello"):
    print(f"{greeting}, {name}!")

# 1. Only a name
greet("Alex")

# 2. Name and a custom greeting
greet("Alex", "Good morning")

# 3. Greeting as a keyword argument
greet("Alex", greeting="Hello")