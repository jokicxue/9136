'''
This program is designed as container system
User can select a container
1.User can select items to store in the container
2.User can check the details of container
3.Or quit the game
'''

import csv

class Container:
    '''
    define a class contains container's variables and methods
    '''

    def __init__(self, cont_name, cont_empty_weight, cont_capacity):
        '''
        set instance variables for containers name, empty weight, capacity and what items contained
        '''
        self.cont_name = cont_name
        self.cont_empty_weight = cont_empty_weight
        self.cont_capacity = cont_capacity
        self.cont_items = []

    def used_capacity(self)-> int:
        '''
        calculate how much capacity is being used
        '''
        return sum(item.item_weight for item in self.cont_items)

    def total_weight(self) -> int:
        '''
        calculate the total weight of the container
        '''
        return self.cont_empty_weight + self.used_capacity()

    def add_item(self, loot_item):
        '''
        add item into container
        '''
        # if the weight of the loot item is lighter than the remaining capacity
        if loot_item.item_weight <= self.cont_capacity - sum(item.item_weight for item in self.cont_items):

            # add loot item into container
            self.cont_items.append(loot_item)
            return True

        return False

    def show_items(self):
        '''
        show the items in the container
        '''
        # print container's details
        print(self)

        # print each item
        for item in self.cont_items:
            print(f"   {item}")

    def __str__(self):
        '''
        print the information of the container
        '''
        return f"{self.cont_name} (total weight: {self.total_weight()}, empty weight: {self.cont_empty_weight}, capacity: {self.used_capacity()}/{self.cont_capacity})"

    @classmethod
    def read_container(cls, file_name):
        '''
        read file of containers and set a list of Container objects
        '''
        # read csv file and set an empty container list
        containers = []
        with open(file_name, newline = "") as container_file:
            reader = csv.reader(container_file)
            next(reader)

        # add each container into containers list
            for row in reader:
                container = Container(row[0].strip(), int(row[1].strip()), int(row[2].strip()))
                containers.append(container)

        # return containers list and sort containers by name
        return sorted(containers, key=lambda x: x.cont_name)

class Item:
    '''
    define a class contains item's variables and methods
    '''

    def __init__(self, item_name, item_weight):
        '''
        set instance variables for item: name and weight
        '''
        self.item_name = item_name
        self.item_weight = item_weight

    def __str__(self):
        '''
        print the basic information of an item
        '''
        return f"{self.item_name} (weight: {self.item_weight})"

    @classmethod
    def read_item(cls, file_name):
        '''
        This function is to set item list
        '''
        # read csv file and set an empty items list
        items = []
        with open(file_name, newline = "") as item_file:
            reader = csv.reader(item_file)
            #skip the header
            next(reader)

        # add each item into items list
            for row in reader:
                item = Item(row[0].strip(), int(row[1].strip()))
                items.append(item)

        # return items list and sort items by name
        return sorted(items, key=lambda x: x.item_name)

class Gamesystem:
    '''
    This class is a basic game system contains method
    1. create new items
    2. pick container
    3. game table
    '''
    def __init__(self, items, containers):
        self.containers = containers
        self.items = items

    def pick_container(self):
        '''
        this function is to pick container
        '''
        while True:
            container_name = input("Enter the name of the container: ")
            for container in self.containers:
                if container_name == container.cont_name:
                    return container
            print(f'"{container_name}" not found. Try again.')

    def gametable(self):
        '''
        show the game table
        '''
        pick_container = self.pick_container()

        if pick_container:
            while True:
                print("==================================")
                print("Enter your choice:")
                print("1. Loot item.")
                print("2. List looted items.")
                print("0. Quit.")
                print("==================================")
                choice = input()
                if choice == "1":
                    while True:
                        choose_item = input("Enter the name of the item: ")
                        for item in self.items:
                            if choose_item == item.item_name:
                                if pick_container.add_item(item):
                                    print(f'''Success! Item "{item.item_name}" stored in container "{pick_container.cont_name}".''')
                                else:
                                    print(f'''Failure! Item "{item.item_name}" NOT stored in container "{pick_container.cont_name}".''')
                                break
                        else:
                            print(f'''"{choose_item}" not found. Try again.''')
                            continue
                        break
                elif choice == "2":
                    pick_container.show_items()
                elif choice == "0":
                    break

if __name__ == "__main__":
    # read 2 files one is container information, the other one is item information
    containers = Container.read_container("containers.csv")
    items = Item.read_item("items.csv")

    # calculate the number of all items including containers
    total_items = len(containers) + len(items)
    print(f"Initialised {total_items} items including {len(containers)} containers.\n")

    # start game
    gamestart = Gamesystem(items, containers)

    # show the table of game
    gamestart.gametable()