import os

# 1. Print the current working directory
print("Current directory:", os.getcwd())

# 2. Check whether expenses.csv exists
if os.path.exists("../data/expenses.csv"):
    print("expenses.csv found.")
else:
    print("expenses.csv not found.")

# 3. Build the path from its parts
expenses_path = os.path.join("..", "data", "expenses.csv")
print("Built path:", expenses_path)