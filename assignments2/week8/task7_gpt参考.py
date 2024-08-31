# write your program here
import csv
from tabulate import tabulate

def read_csv_files():
    tables = []
    filenames = ['grades.csv', 'class_students.csv', 'rabbytes_club_students.csv', 'rabbytes_data.csv']
    for filename in filenames:
        with open(filename, 'r') as file:
            reader = csv.reader(file)
            headers = next(reader)
            rows = [row for row in reader]
            tables.append((headers, rows))
    return tables

'''
def read_csv_files():
    tables = []
    filenames = ['grades.csv', 'class_students.csv', 'rabbytes_club_students.csv', 'rabbytes_data.csv']
    for filename in filenames:
        with open(filename, 'r') as file:
            reader = csv.reader(file)
            headers = next(reader)
            rows = [row for row in reader]
            rows.insert(0, headers)  # 将 headers 插入到 rows 的第一行
            tables.append(rows)
    return tables
'''
def list_tables(tables):
    data = []
    for i, (headers, rows) in enumerate(tables):
        data.append([i, len(headers), len(rows)])
    print(tabulate(data, headers=["Index", "Columns", "Rows"], tablefmt="plain"))

def display_table(tables):
    while True:
        try:
            index = int(input("Choose a table index (to display):\n"))
            if 0 <= index < len(tables):
                headers, rows = tables[index]
                print(tabulate(rows, headers=headers, tablefmt="plain"))
                break
            else:
                print("Incorrect table index. Try again.")
        except ValueError:
            print("Incorrect input. Please enter a valid integer.")

def duplicate_table(tables):
    while True:
        try:
            index = int(input("Choose a table index (to duplicate):\n"))
            if 0 <= index < len(tables):
                headers, rows = tables[index]
                tables.append((headers, rows.copy()))
                break
            else:
                print("Incorrect table index. Try again.")
        except ValueError:
            print("Incorrect input. Please enter a valid integer.")

def main():
    tables = read_csv_files()

    while True:
        print("==================================")
        print("Enter your choice:")
        print("1. List tables.")
        print("2. Display table.")
        print("3. Duplicate table.")
        print("0. Quit.")
        print("==================================")

        choice = input()

        if choice == '1':
            list_tables(tables)
        elif choice == '2':
            display_table(tables)
        elif choice == '3':
            duplicate_table(tables)
        elif choice == '0':
            break

if __name__ == "__main__":
    main()
