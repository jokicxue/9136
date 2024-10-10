'''
This program is designed as container system
User can select a container and add multi containers, add magic containers and magic multi containers.
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
        """
        container should have name, empty weight, capacity and a list of items it contains
        """
        self.cont_name = cont_name
        self.cont_empty_weight = cont_empty_weight
        self.cont_capacity = cont_capacity
        self.cont_items = []

    def total_weight(self)-> int:
        """
        container's total weight equals its own weight plus the capacity used
        """
        return self.cont_empty_weight + self.used_capacity()

    def used_capacity(self)-> int:
        """
        used capacity equals to total weight of all items
        """
        return sum(item.item_weight for item in self.cont_items)

    def add_item(self, loot_item):
        '''
        add_item into container
        '''
        # if the weight of the loot item is lighter than the remaining capacity
        if loot_item.item_weight <= self.cont_capacity - sum(item.item_weight for item in self.cont_items):
            # add loot item into container
            self.cont_items.append(loot_item)
            return True

        # or tell user can not store the loot item
        # else:
        # print(f'''Failure! Item "{loot_item.item_name}" NOT stored in container "{self.cont_name}".''')
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
        print the information of container
        '''
        return f"{self.cont_name} (total weight: {self.total_weight()}, empty weight: {self.cont_empty_weight}, capacity: {self.used_capacity()}/{self.cont_capacity})"

    @classmethod
    def read_container(cls, file_name):
        '''
        read file of containers and set a list of Container objects
        '''
        containers = []
        with open(file_name, newline = "") as container_file:
            reader = csv.reader(container_file)
            # Skip the header
            next(reader)

            for row in reader:
                # set Container object name, empty weight and capacity
                container = Container(row[0].strip(), int(row[1].strip()), int(row[2].strip()))
                # add to containers list
                containers.append(container)

        # return containers list and sort containers by name
        return sorted(containers, key=lambda x: x.cont_name)


class MultiContainer(Container):
    '''
    set child class to contain multiple containers
    '''
    def __init__(self, name, containers):
        '''
        multi container contains many container, so it's empty weight and capacity are the sum of all sub containers.
        '''
        total_empty_weight = sum(cont.cont_empty_weight for cont in containers)
        total_capacity = sum(cont.cont_capacity for cont in containers)
        super().__init__(name, total_empty_weight, total_capacity)
        self.containers = containers

    def used_capacity(self):
        '''
        the sum of used capacity of all sub containers
        '''
        # calculate sub containers capacity
        return sum(cont.used_capacity() for cont in self.containers)

    def add_item(self, loot_item):
        for cont in self.containers:
            # check the capacity
            if loot_item.item_weight <= cont.cont_capacity - cont.used_capacity():
                # add the item into container
                cont.cont_items.append(loot_item)
                return True
        # else not one can store the item, return False
        return False

    def show_items(self):
        # print(f"{self.cont_name} (total weight: {self.total_weight()}, empty weight: {self.cont_empty_weight}, capacity: {self.used_capacity()}/{self.cont_capacity})")
        print(self)
        for cont in self.containers:
            print(f"   {cont}")
            for item in cont.cont_items:
                print(f"      {item}")

    def __str__(self):
        return f"{self.cont_name} (total weight: {self.total_weight()}, empty weight: {self.cont_empty_weight}, capacity: 0/0)"

    @classmethod
    def read_multi_container(cls, file_name, containers):
        '''
        This function is to set containers list
        '''

        with open(file_name, newline='') as original_data:
            reader = csv.reader(original_data)
            next(reader)  # Skip the header
            multi_containers = []

            for row in reader:
                containers_list = []
                clean_row = [field.strip() for field in row]

                for each_sub_container in clean_row[1:]:
                    # find the container with the same name in containers
                    match_container = None
                    for cont in containers:
                        if cont.cont_name == each_sub_container:
                            match_container = cont
                            break

                    if match_container:
                        # create a new container with the same default value
                        new_container = Container(
                            cont_name=match_container.cont_name,
                            cont_empty_weight=match_container.cont_empty_weight,
                            cont_capacity=match_container.cont_capacity
                        )
                        containers_list.append(new_container)

                multi_container = MultiContainer(clean_row[0], containers_list)
                multi_containers.append(multi_container)

        return multi_containers


class MagicContainer(Container):
    def __init__(self, name, original_container):
        super().__init__(name, original_container.cont_empty_weight, original_container.cont_capacity)
        self.base_container = original_container

    def total_weight(self):
        return self.cont_empty_weight

    @classmethod
    def read_magic_containers(cls, file_name, containers):
        with open(file_name, newline="") as original_data:
            reader = csv.reader(original_data)
            next(reader)
            magic_containers = []

            for row in reader:
                magic_containers_list = []
                clean_row = [field.strip() for field in row]

                for each_magic_cont in clean_row[1:]:
                    match_container = None
                    for cont in containers:
                        if cont.cont_name == each_magic_cont:
                            match_container = cont
                            break

                magic_container = MagicContainer(clean_row[0], match_container)
                magic_containers.append(magic_container)

        return magic_containers


class MagicMulticontainer(MultiContainer):
    def __init__(self, name, containers):
        super().__init__(name, containers)

    def total_weight(self):
        # override total weight = empty weight
        return self.cont_empty_weight

    @classmethod
    def read_magic_multicontainer(cls, file_name, multi_containers):
        magic_multi_containers = []
        with open(file_name, newline='') as original_data:
            reader = csv.reader(original_data)
            next(reader)  # Skip the header

            for row in reader:
                clean_row = [field.strip() for field in row]

                for each_multi_container in clean_row[1:]:
                    # find the container with the same name in containers
                    match_container = None
                    for multi_cont in multi_containers:
                        if multi_cont.cont_name == each_multi_container:
                            match_container = multi_cont
                            break

                    if match_container:
                        magic_multi_container = cls(clean_row[0], match_container.containers)
                        magic_multi_containers.append(magic_multi_container)
        return magic_multi_containers


class Item:
    '''
    define a class contains item's variables and methods
    '''

    # set instance variables for item: name and weight
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
    def __init__(self, items, containers, multi_containers, magic_containers, magic_multi_containers):
        self.containers = containers + multi_containers + magic_containers + magic_multi_containers
        self.multi_containers = multi_containers
        self.magic_containers = magic_containers
        self.magic_multi_containers = magic_multi_containers
        self.items = items

    def pick_container(self):
        '''
        this function is to pick container
        '''

        while True:
            container_name = input("Enter the name of the container: ")

            # if the container in the containers list
            for container in self.containers:
                if container_name == container.cont_name:
                    return container
            for multi_container in self.multi_containers:
                if container_name == multi_container.cont_name:
                    return multi_container
            # else tell user choose again
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
                                    print(
                                        f'''Success! Item "{item.item_name}" stored in container "{pick_container.cont_name}".''')
                                else:
                                    print(
                                        f'''Failure! Item "{item.item_name}" NOT stored in container "{pick_container.cont_name}".''')
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
    multi_containers = MultiContainer.read_multi_container("multi_containers.csv", containers)
    magic_containers = MagicContainer.read_magic_containers("magic_containers.csv", containers)
    magic_multi_containers = MagicMulticontainer.read_magic_multicontainer("magic_multi_containers.csv", multi_containers)

    # calculate the number of all items including containers
    total_items = len(containers) + len(items) + len(multi_containers) + len(magic_containers) + len(magic_multi_containers)
    total_containers = len(containers) + len(multi_containers) + len(magic_containers) + len(magic_multi_containers)
    print(f"Initialised {total_items} items including {total_containers} containers.\n")

    # start game
    gamestart = Gamesystem(items, containers, multi_containers, magic_containers, magic_multi_containers)

    # show the table of game
    gamestart.gametable()