'''
This program is designed as container system
User can select a container and add multi containers
1.User can select items to store in the container
2.User can check the details of container
3.Or quit the game
'''

import pandas as pd
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
            # print(f'''Success! Item "{loot_item.item_name}" stored in container "{self.cont_name}".''')
            return True

        # or tell user can not store the loot item
        # else:
            # print(f'''Failure! Item "{loot_item.item_name}" NOT stored in container "{self.cont_name}".''')
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
    def read_container(cls,file_name):
        '''
        This function is to set containers list
        '''
        # read csv file and set an empty container list
        ct = pd.read_csv(file_name)
        containers = []

        # add each container into containers list
        for index, row in ct.iterrows():
            container = Container(row["Name"], row[" Empty Weight"], row[" Weight Capacity"])
            containers.append(container)

        # return containers list and sort containers by name
        return sorted(containers, key=lambda x: x.cont_name)

class MultiContainer(Container):
    def __init__(self, name, containers):
        total_empty_weight = sum(cont.cont_empty_weight for cont in containers)
        total_capacity = sum(cont.cont_capacity for cont in containers)
        super().__init__(name, total_empty_weight, total_capacity)
        self.containers = containers

    def used_capacity(self):
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
    '''
    define a class contains container's variables and methods
    '''

    # set instance variables for containers name, empty weight, capacity and what items contained
    def __init__(self, cont_name, cont_empty_weight, cont_capacity):
        super().__init__(cont_name, cont_empty_weight, cont_capacity)
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
            # print(f'''Success! Item "{loot_item.item_name}" stored in container "{self.cont_name}".''')
            return True

        # or tell user can not store the loot item
        # else:
            # print(f'''Failure! Item "{loot_item.item_name}" NOT stored in container "{self.cont_name}".''')
        return False

    # calculate the total weight of the container
    def total_weight(self):
        return self.cont_empty_weight

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
    def read_magic_container(cls, file_name, containers):
        '''
        This function is to set containers list
        '''
        with open(file_name, newline='') as original_data:
            reader = csv.reader(original_data)
            next(reader)
            magic_containers = []

            for row in reader:
                clean_row = [field.strip() for field in row]
                sub_container_name = clean_row[1]

                containers_list = []
                match_container = None
                for cont in containers:
                    if cont.cont_name == sub_container_name:
                        match_container = cont
                        break

                if match_container:

                    magic_container = MagicContainer(
                        cont_name=clean_row[0],
                        cont_empty_weight=match_container.cont_empty_weight,
                        cont_capacity=match_container.cont_capacity
                    )
                    magic_containers.append(magic_container)

        return magic_containers

class MagicMultiContainer(Container):
    '''
    define a class contains container's variables and methods
    '''

    # set instance variables for containers name, empty weight, capacity and what items contained
    def __init__(self, name, containers):
        #total_empty_weight = sum(cont.cont_empty_weight for cont in containers)
        #total_capacity = sum(cont.cont_capacity for cont in containers)
        total_empty_weight = 0
        total_capacity = 0
        super().__init__(name, total_empty_weight, total_capacity)
        self.containers = containers

    def used_capacity(self):
        # calculate sub containers capacity
        return "0"
        #return sum(cont.used_capacity() for cont in self.containers)

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

    # print the information of the container
    def __str__(self):
        return f"{self.cont_name} (total weight: 0, empty weight: 0, capacity: 0/0)"

    # class method to read file
    @classmethod
    def read_magic_multi_container(cls, file_name, multi_containers_file, containers, multi_containers):
        '''
        This function is to set containers list


        with open(multi_containers_file, newline='') as original_data:
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
        '''
        with open(file_name, newline='') as original_data:
            reader = csv.reader(original_data)
            next(reader)
            magic_multi_containers = []

            for row in reader:
                clean_row = [field.strip() for field in row]
                sub_container_name = clean_row[1]

                containers_list = []
                match_container = None
                for cont in range(len(multi_containers)):
                    if multi_containers[cont].cont_name == sub_container_name:
                        match_container = multi_containers[cont].cont_name
                        break
                '''
                if match_container:
                    # create a new container with the same default value
                    new_container = Container(
                        cont_name=match_container.cont_name,
                        cont_empty_weight=match_container.cont_empty_weight,
                        cont_capacity=match_container.cont_capacity
                    )
                    containers_list.append(new_container)
                '''
                magic_multi_container = MultiContainer(clean_row[0], multi_containers[cont].containers)
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
        # read csv file and set an empty container list
        item_file = pd.read_csv(file_name)
        items = []

        # add each container into containers list
        for index, row in item_file.iterrows():
            item = Item(row["Name"], row[" Weight"])
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
            for magic_container in self.magic_containers:
                if container_name == magic_container.cont_name:
                    return magic_container
            for magic_multi_container in self.magic_multi_containers:
                if container_name == magic_multi_container.cont_name:
                    return magic_multi_container
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
    multi_containers = MultiContainer.read_multi_container("multi_containers.csv", containers)
    magic_containers = MagicContainer.read_magic_container("magic_containers.csv", containers)
    magic_multi_containers = MagicMultiContainer.read_magic_multi_container("magic_multi_containers.csv","multi_containers.csv",  containers, multi_containers)
    # calculate the number of all items including containers
    total_items = len(containers) + len(items) + len(multi_containers) + len(magic_containers) + len(magic_multi_containers)
    total_containers = len(containers)+len(multi_containers) + len(magic_containers) + len(magic_multi_containers)
    print(f"Initialised {total_items} items including {total_containers} containers.\n")
    # start game
    gamestart = Gamesystem(items, containers, multi_containers, magic_containers, magic_multi_containers)

    # show the table of game
    gamestart.gametable()