'''
GROUP:GRP398
Author:
Nikolai Xue(xxue0016@student.monash.edu)
Dingkun Yao(dyao0004@student.monash.edu)
This program is to show and copy tables. 
1. You can see the data about the number of columns and rows of all tables. 
2. You can see the details of each table.
3. Copy table
'''
import csv
from tabulate import tabulate
import copy

# define a function to show the menu
def menu():
    table = set_table()
    while True:
        print("==================================")
        print("Enter your choice:")
        print("1. List tables.")
        print("2. Display table.")
        print("3. Duplicate table.")
        print("0. Quit.")
        print("==================================")

        # create a variable to save the user input
        choice = input()

        if choice == '1':
            list_table(table)
        elif choice == '2':
            display_table(table)
        elif choice == '3':
            duplicate_table(table)
        elif choice == '0':
            break

# define a function to read csv files and convert to table
def set_table():
    # create a table list to save all the data
    table = []

    files = ['grades.csv', 'class_students.csv', 'rabbytes_club_students.csv', 'rabbytes_data.csv']
    for every_file in files:
        with open(every_file, 'r') as file:
            # find the row
            reader = csv.reader(file)
    
            # find the header
            headers = next(reader)
            rows = [row for row in reader]
            '''
            the table have 4 items represent 4 csv
            In each item has 2 items,[0] is header, [1] is data
            [
            [h1,h2,h3],
            [
            [v0,v0,v0],
            [v1,v1,v1]
            ]
            ]
            '''
            table.append((headers, rows))
    return table

# define a function to calculate columns and rows and show them 
def list_table(table):

    # storage table number, columns and rows
    table_list = []
    for i,(headers, rows) in enumerate(table):
        table_list.append([i, len(headers), len(rows)+1])

    print(tabulate(table_list, headers=["Index", "Columns", "Rows"]))

# define a function to display the table
def display_table(table):
    while True:
        choose = int(input("Choose a table index (to display):\n"))

        # check the input
        if choose in range(len(table)):

            # choose is the number of the table
            # so [choose][1]is the data, [choose][0]is the header
            print(tabulate(table[choose][1], headers=table[choose][0]))
            break
        else:
            print("Incorrect table index. Try again.")

# define a function to copy the table
def duplicate_table(table):
    while True:
        # create a variable to save the user input
        choose = int(input("Choose a table index (to duplicate):\n"))
        
        # check the input
        if choose in range(len(table)):

            # deepcopy the table and add to table list
            dup_table = copy.deepcopy(table[choose])
            table.append(dup_table)
            break
        else:
            print("Incorrect table index. Try again.")


if __name__ == "__main__":
    menu()