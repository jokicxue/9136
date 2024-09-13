'''
GROUP:GRP398
Author:
Nikolai Xue(xxue0016@student.monash.edu)
Dingkun Yao(dyao0004@student.monash.edu)
This program is designed to collect the program from user.
1.it can list all the variables.
2.it can change the variables format.
3.it can change the variables names
(the different between task5 and task6 is to rename the variables)
'''
import keyword
import re

# define a list containing the symbols we don't want to store.
drop_symbol = ["+", "-", "*", "**", "/", "=", "!=", "+=", "-=", "==", ">=", "<=", "for", "in", ">", "<", "//", "%",
               ":"] + keyword.kwlist

# define 2 lists, one stores program, one stores variables
program = []
variable = []


# define a function to list choises
def menu():
    while True:
        print("==================================")
        print("Enter your choice:")
        print("1. Print program.\n2. List.\n3. Format.\n4. Rename.\n0. Quit.")
        print("==================================")

        # create a variable to save the user input
        choice = input()
        if choice == "1":
            print_program(program)
        elif choice == "2":
            list_variable(variable)
        elif choice == "3":
            change_format(program, variable)
        elif choice == "4":
            rename_variable(program, variable)
        elif choice == "0":
            break
        else:
            continue


# define a function to collect the program
def all_program(program, variable):
    print("Enter the Python program to analyze, line by line. Enter 'end' to finish.")
    while True:

        # create a variable to save the user input
        user_program = input()

        # check the user input
        if user_program != "end":

            # add the variable into list
            program.append(user_program)

            # devide the program into variables and store the variables
            for user_variable in user_program.split():

                # drop the symbol we don't need
                if user_variable not in drop_symbol:
                    if user_variable not in variable:
                        variable.append(user_variable)
        else:
            break


# define a function to print all programs
def print_program(program):
    print("Program:")

    # print each program
    for every_program in program:
        print(every_program)


# define a function to print all variables
def list_variable(variable):
    print("Variables:")
    for every_variable in sorted(variable):
        print(every_variable)


# define a function to change the format of variable
def change_format(program, variable):
    while True:
        print("Pick a variable:")

        # create a variable to save the user input
        pick_variable = input()

        # create a variable to save the new format
        snake_variable = ""


        if pick_variable in variable:
            for count in range(len(pick_variable)):

                # if the letter is uppercase, change it into lowercases
                if pick_variable[count].isupper():
                    if count != 0:
                        snake_variable += "_" + pick_variable[count].lower()
                    
                    # if the letter is lowercase, just add it
                    else:
                        snake_variable += pick_variable[count].lower()
                else:
                    snake_variable += pick_variable[count].lower()

            # replace pick_variable with snake_variable in variable list
            variable[variable.index(pick_variable)] = snake_variable

            # replace pick_variable with snake_variable in program list
            for i in range(len(program)):
                program[i] = re.sub(rf'\b{pick_variable}\b', snake_variable, program[i])
            break
        else:
            print("This is not a variable name.")
            continue

# define a function to rename the variables
def rename_variable(program, variable):

    # ask the user to pick a variable
    while True:
        print("Pick a variable:")
        pick_variable = input()

        # check the pick_variable
        if pick_variable in variable:
            while True:
                new_name_variable = input("Pick a new variable name:\n")

                # check the new name in variable list, it must be a new variable name
                if new_name_variable not in variable:
                    # replace pick_variable with new_name_variable in variable list
                    variable[variable.index(pick_variable)] = new_name_variable

                    # replace pick_variable with new_name_variable in program list
                    for i in range(len(program)):
                        program[i] = re.sub(rf'\b{pick_variable}\b', new_name_variable, program[i])
                    break
                # if the name already exists, tell the user and ask for a new one.
                else:
                    print("This is already a variable name.")
                    continue

            break
        else:
            print("This is not a variable name.")
            continue

# run the program to collect the program
all_program(program, variable)

# run the menu
if __name__ == "__main__":
    menu()