'''
GROUP:GRP398
Author:
Dingkun Yao(dyao0004@student.monash.edu)
Nikolai Xue(xxue0016@student.monash.edu)
This program is to create a database of rabbytes:
1. record the name and age of the rabbits
2. create parental relationship between them
- number of parents is between 0 and 2
- a rabbit cannot be their own ancester
3. list their relationship
4. record the relationship of cousins
#        AA1
#       |  |
#      A1   A2
#     | |   | |
#    a1 a2 a3 a4
- use "a1" find parents "A1"
- use "A1" find grandparents "AA1"
- use "AA1" find parent's sibling "A2"
- use "A2" find cousins "a3""a4"
'''

# Define a menu
def menu():
    # Create a dictonary to record rabbits
    rabbits = {}

    # Create a dictonary to record the parent and their kittens
    parents = {}

    # Create a dictonary to record the kitten and their parents
    kittens = {}

    # Show the menu
    while True:
        print("==================================")
        print("Enter your choice:")
        print("1. Create a Rabbit.")
        print("2. Input Age of a Rabbit.")
        print("3. List Rabbytes.")
        print("4. Create a Parental Relationship.")
        print("5. List Direct Family of a Rabbit.")
        print("6. Find Cousins of a Rabbit.")        
        print("0. Quit.")
        print("==================================")
    
        choice = input()
        # To do the different task
        if choice == "1":
            create_rabbit(rabbits,parents,kittens)
        elif choice == "2":
            input_age(rabbits)
        elif choice == "3":
            list_rabbit(rabbits)
        elif choice == "4":
            create_relationship(rabbits, parents, kittens)
        elif choice == "5":
            list_family(rabbits, parents, kittens)
        elif choice == "6":
            find_cousin(rabbits, parents, kittens)
        elif choice == "0":
            break
        else:
            continue

# Define a funcion to create rabbit
def create_rabbit(rabbits,parents,kittens):
    while True:
        # Set a variable to recive the name
        name = input("Input the new rabbit's name:\n")

        # if name in the rabbits list
        if name in rabbits:
            print("That name is already in the database.")
        # add the information
        else:
            rabbits[name] = None
            parents[name] = []
            kittens[name] = []
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
def create_relationship(rabbits, parents, kittens):
    while True:
        # Ask the user to input the parent's and kitten's name
        parent_name = input("Input the parent's name:\n")
        kitten_name = input("Input the kitten's name:\n")

        # Check the name in rabbits or not, if not add into rabbits
        if parent_name not in rabbits:
            rabbits[parent_name] = None
            parents[parent_name] = []
            kittens[parent_name] = []

        if kitten_name not in rabbits:
            rabbits[kitten_name] = None
            parents[kitten_name] = []
            kittens[kitten_name] = []
        
        # add the kitten name to the parent
        parents[parent_name].append(kitten_name)
        # add the parent name to the kitten
        kittens[kitten_name].append(parent_name)
        break

# Define a function to list the family
def list_family(rabbits, parents, kittens):
    while True:
        name = input("Input the rabbit's name:\n")

        # If name in rabbits
        if name in rabbits:
            # find the parents name in list kittens
            print(f"Parents of {name}:")
            for parent in sorted(kittens[name]):
                print(parent)

            # find the kittens name in list parents
            print(f"Kittens of {name}:")
            for kitten in sorted(parents[name]):
                print(kitten)
            break
        else:
            print("That name is not in the database.")

# Define a function to find the cousin
def find_cousin(rabbits, parents, kittens):
    while True:
        # Ask the user to input the name
        kitten_name = input("Input the rabbit's name:\n")
        if kitten_name in rabbits:

            # define a list to storage cousins' name
            cousin = []

            # 1.find the kitten's parents
            for parent in kittens[kitten_name]:
                # 2. find the kitten's grandparents(parent's parents)
                for grandparent in kittens[parent]:
                    # 3. find grandparent's other children(parent's sibling)
                    for parent_sibling in parents[grandparent]:
                        if parent != parent_sibling:
                            # 4. find the chlidren of parent's sibling
                            cousin += parents[parent_sibling]
            print(f"Cousins of {kitten_name}:")
            for every_cousin in sorted(cousin):
                print(every_cousin)
            break
        else:
            print("That name is not in the database.")            
 
if __name__ == "__main__":
    menu()