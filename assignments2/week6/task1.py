'''
This program is to create a database of rabbytes,
and record the name and age of the rabbits
'''

# Define a menu
def menu():
    # Create a dictonnary to record rabbits
    rabbits = {}

    # Show the menu
    while True:
        print("==================================")
        print("Enter your choice:")
        print("1. Create a Rabbit.")
        print("2. Input Age of a Rabbit.")
        print("3. List Rabbytes.")
        print("0. Quit.")
        print("==================================")
    
        choice = input()
        # To do the different task
        if choice == "1":
            create_rabbit(rabbits)
        elif choice == "2":
            input_age(rabbits)
        elif choice == "3":
            list_rabbit(rabbits)
        elif choice == "0":
            break
        else:
            continue

# Define a funcion to create rabbit
def create_rabbit(rabbits):
    while True:
        # Set a variable to recive the name
        name = input("Input the new rabbit's name:\n")
        if name in rabbits:
            print("That name is already in the database.")
        else:
            rabbits[name] = None
            break

# Define a function to collect age
def input_age(rabbits):
    while True:
        # Set a variable to check the name
        check_name = input("Input the rabbit's name:\n")

        # If the rabbit is in the database, ask the age
        if check_name in rabbits:
            age = int(input(f"Input {check_name}'s age:\n"))
            rabbits[check_name] = age
            break
        
        # If not in the database, tell the user and keep asking
        else:
            print("That name is not in the database.")

# Define a function to list all the rabbits
def list_rabbit(rabbits):
    print("Rabbytes:")

    # check the age before output
    for name,age in rabbits.items():
        if age != None:
            print(f"{name} ({age})")
        else:
            print(f"{name} (Unknown)")

if __name__ == "__main__":
    menu()