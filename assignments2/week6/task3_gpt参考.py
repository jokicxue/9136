# Define a menu
def menu():
    # Create dictionaries to record rabbits and their relationships
    rabbits = {}
    parents = {}
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
            create_rabbit(rabbits, parents, kittens)
        elif choice == "2":
            input_age(rabbits)
        elif choice == "3":
            list_rabbit(rabbits)
        elif choice == "4":
            create_parental_relationship(rabbits, parents, kittens)
        elif choice == "5":
            list_direct_family(rabbits, parents, kittens)
        elif choice == "6":
            find_cousins(rabbits, parents, kittens)
        elif choice == "0":
            break
        else:
            continue


# Define a function to create a rabbit
def create_rabbit(rabbits, parents, kittens):
    while True:
        name = input("Input the new rabbit's name:\n")
        if name in rabbits:
            print("That name is already in the database.")
        else:
            rabbits[name] = None
            parents[name] = []
            kittens[name] = []
            break


# Define a function to collect age
def input_age(rabbits):
    while True:
        check_name = input("Input the rabbit's name:\n")

        if check_name in rabbits:
            age = int(input(f"Input {check_name}'s age:\n"))
            rabbits[check_name] = age
            break
        else:
            print("That name is not in the database.")


# Define a function to list all the rabbits
def list_rabbit(rabbits):
    print("Rabbytes:")
    for name, age in rabbits.items():
        if age is not None:
            print(f"{name} ({age})")
        else:
            print(f"{name} (Unknown)")


# Define a function to create a parental relationship
def create_parental_relationship(rabbits, parents, kittens):
    while True:
        parent_name = input("Input the parent's name:\n")
        kitten_name = input("Input the kitten's name:\n")

        if parent_name not in rabbits:
            rabbits[parent_name] = None
            parents[parent_name] = []
            kittens[parent_name] = []

        if kitten_name not in rabbits:
            rabbits[kitten_name] = None
            parents[kitten_name] = []
            kittens[kitten_name] = []

        parents[kitten_name].append(parent_name)
        kittens[parent_name].append(kitten_name)
        break


# Define a function to list direct family of a rabbit
def list_direct_family(rabbits, parents, kittens):
    while True:
        rabbit_name = input("Input the rabbit's name:\n")

        if rabbit_name in rabbits:
            print(f"Parents of {rabbit_name}:")
            for parent in sorted(parents[rabbit_name]):
                print(parent)
            print(f"Kittens of {rabbit_name}:")
            for kitten in sorted(kittens[rabbit_name]):
                print(kitten)
            break
        else:
            print("That name is not in the database.")


# Define a function to find cousins of a rabbit
def find_cousins(rabbits, parents, kittens):
    while True:
        rabbit_name = input("Input the rabbit's name:\n")
        print(f"parents:{parents}\n",f"kittens:{kittens}")

        if rabbit_name in rabbits:
            cousins = set()
            for parent in parents[rabbit_name]:
                for sibling in kittens[parent]:
                    if sibling != rabbit_name:
                        cousins.update(kittens[sibling])
            sorted_cousins = sorted(cousins - {rabbit_name})
            print(f"Cousins of {rabbit_name}:")
            for cousin in sorted_cousins:
                print(cousin)
            break
        else:
            print("That name is not in the database.")


if __name__ == "__main__":
    menu()
