import csv
import os
from datetime import datetime


def generate_report(category):
    # 1. Check that the file exists
    expenses_path = os.path.join("..", "data", "expenses.csv")
    if not os.path.exists(expenses_path):
        print(f"Error: {expenses_path} not found.")
        return

    # 2. Read the CSV into a list of dictionaries
    with open(expenses_path, "r", newline="") as file:
        expenses = list(csv.DictReader(file))

    # 3. Convert amount to float
    for row in expenses:
        row["amount"] = float(row["amount"])

    # 4. Filter to the chosen category
    filtered = []
    for row in expenses:
        if row["category"] == category:
            filtered.append(row)

    # 5. Calculate the total
    total = 0
    for row in filtered:
        total += row["amount"]

    # 6. Write the report
    today = datetime.now().strftime("%B %d, %Y")
    report_name = f"{category.lower()}_report.txt"

    with open(report_name, "w", encoding="utf-8") as report:
        report.write(f"{category} Expense Report — generated {today}\n")
        for row in filtered:
            report.write(f"{row['date']}: ${row['amount']:.2f}\n")
        report.write(f"Total: ${total:.2f}\n")

    print(f"Report written to {report_name}")


def main():
    generate_report("Food")


main()