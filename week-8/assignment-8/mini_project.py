import csv


def main():
    file_path = "../data/messy_data.csv"
    clean_rows = []
    skipped = []
    attempted = 0

    # 1. Open the file safely
    try:
        with open(file_path, "r", newline="") as file:
            # 2. Read with DictReader
            reader = csv.DictReader(file)

            for row_number, row in enumerate(reader, start=1):
                attempted += 1

                # Guard: extra columns are stored under a None key
                if None in row:
                    skipped.append(f"Row {row_number}: extra column detected — skipped")
                    continue

                # 3. Process each row safely
                try:
                    clean_rows.append({
                        "name": row["name"],
                        "category": row["category"],
                        "amount": float(row["amount"]),
                    })
                except ValueError:
                    skipped.append(
                        f"Row {row_number}: ValueError — could not convert '{row['amount']}' to float"
                    )
                except KeyError as error:
                    skipped.append(f"Row {row_number}: KeyError — missing column {error}")
                except TypeError:
                    skipped.append(f"Row {row_number}: missing amount — skipped")

    except FileNotFoundError:
        print(f"Error: {file_path} was not found. Please check the file path and try again.")
        return

    # 5. Print the summary
    print("=== CSV Report ===")
    print(f"Rows attempted: {attempted:>3}")
    print(f"Rows parsed:    {len(clean_rows):>3}")
    print(f"Rows skipped:   {len(skipped):>3}")

    print()
    print("Skipped rows:")
    for message in skipped:
        print(f"  {message}")

    print()
    print("Clean data:")
    for row in clean_rows:
        print(f"  {row['name']} | {row['category']} | ${row['amount']:.2f}")


main()