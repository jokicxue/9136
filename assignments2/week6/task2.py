'''
This program is to create a database of rabbytes:
1. record the name and age of the rabbits
2. create parental relationship between them
- number of parents is between 0 and 2
- a rabbit cannot be their own ancester
3. list their relationship
'''

# Define a menu
def menu():
    # Create a dictonary to record rabbits
    rabbits = {}

    # Create a dictonary to record the Relationship
    relation = {}

    # Show the menu
    while True:
        print("==================================")
        print("Enter your choice:")
        print("1. Create a Rabbit.")
        print("2. Input Age of a Rabbit.")
        print("3. List Rabbytes.")
        print("4. Create a Parental Relationship.")
        print("5. List Direct Family of a Rabbit.")        
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
        elif choice == "4":
            create_relation()
        elif choice == "5":
            list_family()
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

# Define a function to record the relationship
def create_relation(relation,rabbits):
    parent_name = input("Input the parent's name:\n")
    kitten_name = input("Input the kitten's name:\n")

    # Check the name in rabbits or not
    if parent_name in rabbits:
        if parent_name in relation:
            


if __name__ == "__main__":
    menu()