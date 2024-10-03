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

    # set instance variables for containers name, empty weight, capacity and what items contained
    def __init__(self, cont_name, cont_empty_weight, cont_capacity):
        self.cont_name = cont_name
        self.cont_empty_weight = cont_empty_weight
        self.cont_capacity = cont_capacity
        self.cont_items = []

    # calculate how much capacity is being used
    def used_capacity(self):
        return sum(item.item_weight for item in self.cont_items)

    def add_item(self, loot_item):
        # if the weight of the loot item is lighter than the remaining capacity
        if loot_item.item_weight <= self.cont_capacity - sum(item.item_weight for item in self.cont_items):

            # add loot item into container
            self.cont_items.append(loot_item)
            return True

        return False

    # calculate the total weight of the container
    def total_weight(self):
        return self.cont_empty_weight + self.used_capacity()

    # show the items in the container
    def show_items(self):
        # print container's details
        print(self)

        # print each item
        for item in self.cont_items:
            print(f"   {item}")


    # print the information of the container
    def __str__(self):
        return f"{self.cont_name} (total weight: {self.total_weight()}, empty weight: {self.cont_empty_weight}, capacity: {self.used_capacity()}/{self.cont_capacity})"

    # class method to read file
    @classmethod
    def read_container(cls, file_name):
        '''
        This function is to set containers list
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

    # ser instance variables for item: name and weight
    def __init__(self, item_name, item_weight):
        self.item_name = item_name
        self.item_weight = item_weight

    def __str__(self):
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
            next(reader)

        # add each item into items list
            for row in reader:
                item = Item(row[0].strip(), int(row[1].strip()))
                items.append(item)

        # return items list and sort items by name
        return sorted(items, key=lambda x: x.item_name)

class Gamesystem:
    def __init__(self, items, containers):
        self.containers = containers
        self.items = items

    def pick_container(self):
        while True:
            container_name = input("Enter the name of the container: ")
            for container in self.containers:
                if container_name == container.cont_name:
                    return container
            print(f'"{container_name}" not found. Try again.')

    def gametable(self):
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
    containers = Container.read_container("../week11/containers.csv")
    items = Item.read_item("../week11/items.csv")

    total_items = len(containers) + len(items)
    print(f"Initialised {total_items} items including {len(containers)} containers.\n")

    gamestart = Gamesystem(items, containers)

    gamestart.gametable()