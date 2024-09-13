'''
GROUP:GRP398
Author:
Dingkun Yao(dyao0004@student.monash.edu)
Nikolai Xue(xxue0016@student.monash.edu)
This program is to show, create, and delete tables. 
1. You can see the data about the number of columns and rows of all tables. 
2. You can see the details of each table.
3. Copy table
4. Copy data from one table in the new order
5. Delete table
6. Delete column
7. Restore table
hint
to address the deletion and restore
we create a shadow_table to represent the original table
shadow_table = [1,1,1,1]
if delete table 0, shadow_table[0] change to 0
shadow_table = [0,1,1,1]
if restore table 0, shadow_table[0] change to 1
shadow_table = [1,1,1,1]
'''
import csv
from tabulate import tabulate
import copy

# define a function to show the menu
def menu():
    table,shadow_table = set_table()

    while True:
        print("==================================")
        print("Enter your choice:")
        print("1. List tables.")
        print("2. Display table.")
        print("3. Duplicate table.")
        print("4. Create table.")
        print("5. Delete table.")
        print("6. Delete column.")
        print("7. Restore table.")       
        print("0. Quit.")
        print("==================================")

        # create a variable to save the user input
        choice = input()

        if choice == '1':
            list_table(table,shadow_table)
        elif choice == '2':
            display_table(table,shadow_table)
        elif choice == '3':
            duplicate_table(table,shadow_table)
        elif choice == "4":
            create_table(table,shadow_table)
        elif choice == "5":
            delete_table(table,shadow_table)
        elif choice == "6":
            delete_column(table,shadow_table)
        elif choice == "7":
            restore_table(table,shadow_table)
        elif choice == '0':
            break
# define a function to read csv files and change table
def set_table()->list:
    table = []

    # this shadow_table uses 0 or 1 to record the status of each table
    shadow_table = []

    files = ['grades.csv', 'class_students.csv', 'rabbytes_club_students.csv', 'rabbytes_data.csv']
    for every_file in files:
        with open(every_file,"r") as file:
            # read all the rows
            reader = csv.reader(file)

            # storage the header lines
            header = next(reader)

            # storage the left rows in one list
            rows = [row for row in reader]

            table.append((header,rows))

            # "1" means table is available, "0" means table is been deleted
            shadow_table.append(1)

    return table,shadow_table

# define a function to calculate columns and rows and show them 
def list_table(table:list,shadow_table:list):
    
    # set a table_list to save the columns and rows
    table_list = []
    for i,(header,row) in enumerate (table):

        # check the status of the table, "1" print
        if shadow_table[i] == 1:
            table_list.append([i,len(header),len(row)+1])
        
        # "0" doesn't print
        else:
            pass
    print(tabulate(table_list,headers = ["Index", "Columns", "Rows"]))

# define a function to display the table
def display_table(table:list,shadow_table:list):
    while True:
        # create a variable to save table index
        choose = int(input("Choose a table index (to display):\n"))

        # check the input value
        if choose in range(len(table)) and shadow_table[choose] == 1:
            print(tabulate(table[choose][1],headers=table[choose][0]))
            break
        
        # tell the user input is not right
        else:
            print("Incorrect table index. Try again.")

# define a function to copy the table
def duplicate_table(table:list,shadow_table:list)->list:
    while True:
        choose = int(input("Choose a table index (to duplicate):\n"))
        
        # check the input in shadow list
        if choose in range(len(table)) and shadow_table[choose] == 1:

            # deepcopy the table and add to table list
            dup_table = copy.deepcopy(table[choose])
            table.append(dup_table)

            # shadow_table add one value 1
            shadow_table.append(1)
            break
        else:
            print("Incorrect table index. Try again.")

# define a function to copy the table's specified columns
def create_table(table:list,shadow_table:list)->list:
    while True:
        choose = int(input("Choose a table index (to create from):\n"))
        
        # check the input
        if choose in range(len(table)) and shadow_table[choose] == 1:

            # set a list to storage columns
            columns = input("Enter the comma-separated indices of the columns to keep:\n")
            columns_list = columns.split(",")

            # create 3 lists to storage header and data of new table
            new_table = []
            new_table_header = []
            new_table_data = []

            # find and set the new header in new order
            for column in columns_list:
                new_table_header.append(table[choose][0][int(column)])
            
            # in selected table, find the new data
            for every_data in table[choose][1]:

                # set a list to storage new data
                new_every_data = []
                for column in columns_list:

                    # add the data in new order
                    new_every_data.append(every_data[int(column)])
                new_table_data.append(new_every_data)
            
            new_table = [new_table_header,new_table_data]
            
            # add the new_table to table list
            table.append(new_table)

            # shadow_table add one value 1
            shadow_table.append(1)
            break
        else:
            print("Incorrect table index. Try again.")

# define a function to delete the table
def delete_table(table:list,shadow_table:list):
    while True:
        # create a variable to save table index
        choose = int(input("Choose a table index (for table deletion):\n"))
        
        # check the input and table exists
        if choose in range(len(table)) and shadow_table[choose] == 1:

            # change it into delete
            shadow_table[choose] = 0
            break
        else:
            print("Incorrect table index. Try again.")

# define a function to delete column
def delete_column(table:list,shadow_table:list):
    while True:
        # create a variable to save table index
        choose = int(input("Choose a table index (for column deletion):\n"))
        
        # check the input
        if choose in range(len(table)) and shadow_table[choose] == 1:

            # set a variable to storage column number
            column = int(input("Enter the index of the column to delete:\n"))

            # create the 3 list to storage the data after deletion
            del_table = []
            del_table_header = []
            del_table_data = []

            # count every item, don't add the item when count number equal to column number
            for count,every_header in enumerate(table[choose][0]):
                if count != column:
                    del_table_header.append(every_header)
            
            # search every row of data
            for every_data in table[choose][1]:

                # define a variable to storage each row
                every_table_data = []

                # choose value not in the seleted column
                for count,every_value in enumerate(every_data):
                    if count != column:
                        every_table_data.append(every_value)
                del_table_data.append(every_table_data)
            
            # add data into del_table
            del_table = [del_table_header,del_table_data]

            # replace the original item
            table[choose] = del_table

            break
        else:
            print("Incorrect table index. Try again.")

# define a function to restore the table
def restore_table(table:list,shadow_table:list):
    while True:
        # create a variable to save table index
        choose = int(input("Choose a table index (for restoration):\n"))
        
        # check the input, if table status is 0 change it into 1(available)
        if choose in range(len(table)) and shadow_table[choose] == 0:
            shadow_table[choose] = 1
            break
        else:
            print("Incorrect table index. Try again.")

if __name__ == "__main__":
    menu()