import keyword
import re

# define a list containing the symbols we don't want to store.
drop_symbol = ["+", "-", "*", "**", "/", "=", "!=", "+=", "-=", "==", ">=", "<=", "for", "in", ">", "<", "//", "%",
               ":"] + keyword.kwlist

# define 2 lists, one stores program, one stores variables
program = []
variable = []


# define a function to list choices
def menu():
    while True:
        print("==================================")
        print("Enter your choice:")
        print("1. Print program.\n2. List.\n3. Format.\n4. Rename.\n0. Quit.")
        print("==================================")

        choice = input()
        if choice == "1":
            print_program(program)
        elif choice == "2":
            list_variable(variable)
        elif choice == "3":
            format_variable(program, variable)
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
        user_program = input()
        if user_program != "end":
            program.append(user_program)

            # divide the program into variables and store the variables
            for user_variable in user_program.split():

                # drop the symbols we don't need
                if user_variable not in drop_symbol:
                    if user_variable not in variable:
                        variable.append(user_variable)
        else:
            break


# define a function to print all programs
def print_program(program):
    print("Program:")
    for every_program in program:
        print(every_program)


# define a function to print all variables
def list_variable(variable):
    print("Variables:")
    for every_variable in sorted(variable):
        print(every_variable)


# define a function to format variables to snake_case
def format_variable(program, variable):
    print("Pick a variable:")
    chosen_variable = input()

    # Check if the variable name exactly matches one in the variable list
    if chosen_variable in variable:
        # Convert the variable to snake_case only if it matches exactly
        snake_case_variable = re.sub(r'(?<!^)(?=[A-Z])', '_', chosen_variable).lower()

        # Update the variable in the program using regex for exact matches
        for i in range(len(program)):
            # Use regex to find the exact match of the variable, respecting word boundaries
            program[i] = re.sub(r'\b' + re.escape(chosen_variable) + r'\b', snake_case_variable, program[i])

        # Update the variable list
        variable[variable.index(chosen_variable)] = snake_case_variable

    else:
        print("This is not a variable name.")
        format_variable(program, variable)


# define a function to rename a variable
def rename_variable(program, variable):
    print("Pick a variable:")
    chosen_variable = input()

    # Check if the variable name exactly matches one in the variable list
    if chosen_variable in variable:
        print("Pick a new variable name:")
        new_variable = input()

        # Check if the new variable name is not already in use
        if new_variable not in variable:
            # Update the variable in the program using regex for exact matches
            for i in range(len(program)):
                program[i] = re.sub(r'\b' + re.escape(chosen_variable) + r'\b', new_variable, program[i])

            # Update the variable list
            variable[variable.index(chosen_variable)] = new_variable
        else:
            print("This is already a variable name.")
            rename_variable(program, variable)
    else:
        print("This is not a variable name.")
        rename_variable(program, variable)


# run the program to collect the program
all_program(program, variable)

# run the menu
if __name__ == "__main__":
    menu()
