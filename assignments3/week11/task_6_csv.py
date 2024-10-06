"""
This program is designed as container system
User can select a container and add items into the container
1.User can select items(including containers) to store in the container
2.User can check the details of container
3.Or quit the game
"""

import csv

class Item:
    """
    set class Item as superclass. Containers are subclass, because containers are items too
    """
    def __init__(self, name: str, weight: int) -> None:
        """
        All items have 3 base value name weight and type
        """
        self.name = name
        self.weight = weight
        self.type = "item"

    def total_weight(self) -> int:
        """
        the total weight of the item is its own weight
        """
        return self.weight

    def __str__(self) -> str:
        """
        print the basic information of a item
        """
        return f"{self.name} (weight: {self.weight})"

    @classmethod
    def read_item(cls, file_name):
        """
        This method reads the file of items and set a list of objects
        """

        # set a empty list to store objects
        items = []
        with open(file_name, newline="") as item_file:
            reader = csv.reader(item_file)
            # Skip the header
            next(reader)
            for row in reader:
                # each row create object use name(row0) and weight(row1)
                item = Item(row[0].strip(), int(row[1].strip()))

                # add objects into items list
                items.append(item)
        # sort the items by name
        return sorted(items, key=lambda x: x.name)


class Container(Item):
    """
    Set subclass Container
    """
    def __init__(self, cont_name: str, cont_empty_weight: int, cont_capacity: int):
        """
        container should have name, empty weight, capacity and a list of items it contains
        """
        super().__init__(cont_name, cont_empty_weight)
        self.cont_capacity = cont_capacity
        self.cont_items = []
        self.type = "container"

    def total_weight(self) -> int:
        """
        container's total weight equals its own weight plus the capacity used
        """
        return self.weight + self.used_capacity()

    def used_capacity(self) -> int:
        """
        used capacity equals to total weight of all items
        """
        return sum(item.weight for item in self.cont_items)

    def add_item(self, item):
        """
        add_item into container
        """
        # if item's weight is less than the remaining capacity
        if item.weight <= self.cont_capacity - self.used_capacity():
            # add item into container
            self.cont_items.append(item)
            return True

        # else item's weight is bigger than the remaining capacity
        else:
            # find other containers in the container
            for search_container in self.cont_items:
                if search_container.type != "item":
                    if search_container.add_item(item):
                        return True
        return False

    def show_items(self, pri_space=0):
        """
        show the items in the container
        """
        # print the container's information
        print(' ' * pri_space + str(self))
        for item in self.cont_items:
            # pri_space add 3 and call method again if object is container
            if item.type != "item":
                item.show_items(pri_space + 3)
            # add 3 spaces and print if object is item
            else:
                print(' ' * (pri_space + 3) + str(item))

    def __str__(self):
        """
        print the information of container
        """
        return f"{self.name} (total weight: {self.total_weight()}, empty weight: {self.weight}, capacity: {self.used_capacity()}/{self.cont_capacity})"

    @classmethod
    def read_container(cls, file_name):
        """
        read file of containers and set a list of Container objects
        """
        containers = []
        with open(file_name, newline="") as container_file:
            reader = csv.reader(container_file)
            # Skip the header
            next(reader)
            for row in reader:
                # set Container object name, empty weight and capacity
                container = Container(row[0].strip(), int(row[1].strip()), int(row[2].strip()))
                # add to containers list
                containers.append(container)
        return sorted(containers, key=lambda x: x.name)


class MultiContainer(Container):
    """
    set child class
    """
    def __init__(self, name: str, containers: list):
        """
        multi container contains many container, so it's empty weight and capacity are the sum of all sub containers.
        """
        total_empty_weight = sum(cont.weight for cont in containers)
        total_capacity = sum(cont.cont_capacity for cont in containers)
        super().__init__(name, total_empty_weight, total_capacity)
        self.containers = containers
        self.type = "multi_container"

    def used_capacity(self):
        """
        the sum of used capacity of all sub containers
        """
        return sum(cont.used_capacity() for cont in self.containers)

    def add_item(self, loot_item):
        """
        add_item to sub containers
        hint:
        when add item to sub container both container and sub container will add weight
        So if the item's weight is bigger than remaining capacity, the item can ONLY store in magic container
        """
        for cont in self.containers:
            # add to container, if item's weight less than remaining capacity
            if loot_item.weight <= cont.cont_capacity - cont.used_capacity():
                cont.cont_items.append(loot_item)
                return True

            # or find magic container to store the item
            else:
                for search_container in cont.cont_items:
                    if search_container.type == "magic_container" or search_container.type == "magic_multi_container":
                        if search_container.add_item(loot_item):
                            return True
        return False

    def show_items(self, pri_space=0):
        """
        show the information of the container
        """
        print(' ' * pri_space + str(self))
        # traverse all sub containers
        for cont in self.containers:
            print(' ' * (pri_space + 3) + str(cont))
            # traverse all items
            for item in cont.cont_items:
                # if item is container, call show_items again
                if item.type != "item":
                    item.show_items(pri_space + 6)
                else:
                    print(' ' * (pri_space + 6) + str(item))

    def __str__(self):
        """
        print the information of multi container
        """
        return f"{self.name} (total weight: {self.total_weight()}, empty weight: {self.weight}, capacity: 0/0)"

    @classmethod
    def read_multi_container(cls, file_name, containers):
        """
        This function is to set containers list
        """
        with open(file_name, newline='') as original_data:
            reader = csv.reader(original_data)
            # Skip the header
            next(reader)
            multi_containers = []

            for row in reader:
                containers_list = []
                clean_row = [field.strip() for field in row]

                for each_sub_container in clean_row[1:]:
                    # find the container with the same name in containers
                    match_container = None
                    # traverse all container
                    for cont in containers:
                        # if the name mach the container
                        if cont.name == each_sub_container:
                            match_container = cont
                            break

                    # create a new container with the same default value
                    if match_container:
                        new_container = Container(
                            cont_name=match_container.name,
                            cont_empty_weight=match_container.weight,
                            cont_capacity=match_container.cont_capacity
                        )
                        containers_list.append(new_container)
                # set a multi container object
                multi_container = MultiContainer(clean_row[0], containers_list)
                # add multi container into multi containers list
                multi_containers.append(multi_container)

        return multi_containers


class MagicContainer(Container):
    """
    set child class MagicContainer, the only difference is the weight of magic container does not change
    """
    def __init__(self, name, original_container):
        super().__init__(name, original_container.weight, original_container.cont_capacity)
        self.base_container = original_container
        self.type = "magic_container"

    # the weight of magic container will not change
    def total_weight(self):
        return self.weight

    @classmethod
    def read_magic_containers(cls, file_name, containers):
        """
        read file of magic containers and set object list of magic containers
        """
        magic_containers = []
        with open(file_name, newline="") as original_data:
            reader = csv.reader(original_data)
            # skip the header
            next(reader)
            
            for row in reader:
                clean_row = [field.strip() for field in row]
                match_container = None
                # traverse container in containers
                for cont in containers:
                    # if name matches the name of container
                    if cont.name == clean_row[1]:
                        match_container = cont
                        break
                
                if match_container:
                    # set magic container object
                    magic_container = MagicContainer(clean_row[0], match_container)
                    # add object into list
                    magic_containers.append(magic_container)

        return magic_containers


class MagicMulticontainer(MultiContainer):
    """
    set child class MagicMulticontainer the ONLY difference is weight of magic multi container does not change
    """
    def __init__(self, name, containers):
        """
        the same sub containers as the parent class
        """
        super().__init__(name, containers)
        self.type = "magic_multi_container"

    def total_weight(self):
        """
        total weight will not change
        """
        return self.weight

    @classmethod
    def read_magic_multicontainer(cls, file_name, multi_containers):
        """
        read file of magic multi containers and set a list of magic multi containers
        """
        magic_multi_containers = []
        with open(file_name, newline='') as original_data:
            reader = csv.reader(original_data)
            # skip the header
            next(reader)  

            for row in reader:
                clean_row = [field.strip() for field in row]
                # find the container with the same name in containers
                match_container = None
                for multi_cont in multi_containers:
                    if multi_cont.name == clean_row[1]:
                        match_container = multi_cont
                        break

                if match_container:
                    magic_multi_container = cls(clean_row[0], match_container.containers)
                    magic_multi_containers.append(magic_multi_container)

        return magic_multi_containers


class Gamesystem:
    """
    This class is a basic game system contains method
    1. create new items
    2. pick container
    3. game table
    """
    def __init__(self, items, containers, multi_containers, magic_containers, magic_multi_containers):
        self.items = items
        self.containers = containers + multi_containers + magic_containers + magic_multi_containers
        self.multi_containers = multi_containers

    def create_new_items(self, loot_items):
        """
        VERY IMPORTANT
        this method like a factory
        when user choose one item we create a new object
        """
        new_container = None
        if loot_items.type == "item":
            return Item(loot_items.name, loot_items.weight)
        elif loot_items.type == "container":
            new_container = Container(loot_items.name, loot_items.weight, loot_items.cont_capacity)
        elif loot_items.type == "multi_container":
            new_container = MultiContainer(loot_items.name,
                                           [Container(cont.name, cont.weight, cont.cont_capacity) for cont in
                                            loot_items.containers])
        elif loot_items.type == "magic_container":
            new_container = MagicContainer(loot_items.name, loot_items.base_container)
        elif loot_items.type == "magic_multi_container":
            new_container = MagicMulticontainer(loot_items.name,
                                                [Container(cont.name, cont.weight, cont.cont_capacity) for cont in
                                                 loot_items.containers])
        return new_container

    def pick_container(self):
        """
        ask user to choose a container
        """
        while True:
            container_name = input("Enter the name of the container: ")
            # traverse all container
            for container in self.containers:
                # if container name matches user's choose
                if container.name == container_name:
                    return self.create_new_items(container)
            print(f'"{container_name}" not found. Try again.')

    def gametable(self):
        """
        show the game table
        """
        # ask user to choose container
        pick_container = self.pick_container()
        
        # show game table
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
                        # set a variable to check the item
                        found = False

                        # check the choose item in items list
                        for item in self.items:
                            if item.name == choose_item:
                                new_item = self.create_new_items(item)
                                if pick_container.add_item(new_item):
                                    print(
                                        f'''Success! Item "{new_item.name}" stored in container "{pick_container.name}".''')
                                else:
                                    print(
                                        f'''Failure! Item "{new_item.name}" NOT stored in container "{pick_container.name}".''')
                                found = True
                                break

                        # check the choose item in containers list
                        if not found:
                            for container in self.containers:
                                if container.name == choose_item:
                                    new_container = self.create_new_items(container)
                                    if pick_container.add_item(new_container):
                                        print(
                                            f'''Success! Item "{new_container.name}" stored in container "{pick_container.name}".''')
                                    else:
                                        print(
                                            f'''Failure! Item "{new_container.name}" NOT stored in container "{pick_container.name}".''')
                                    found = True
                                    break

                        if not found:
                            print(f"'{choose_item}' not found. Try again.")
                            continue
                        break
                elif choice == "2":
                    pick_container.show_items()
                elif choice == "0":
                    break


if __name__ == "__main__":
    # read all the files
    containers = Container.read_container("containers.csv")
    items = Item.read_item("items.csv")
    multi_containers = MultiContainer.read_multi_container("multi_containers.csv", containers)
    magic_containers = MagicContainer.read_magic_containers("magic_containers.csv", containers)
    magic_multi_containers = MagicMulticontainer.read_magic_multicontainer("magic_multi_containers.csv", multi_containers)
    
    # add all items including containers
    total_items = len(containers) + len(items) + len(multi_containers) + len(magic_containers) + len(magic_multi_containers)
    
    # add all containers
    total_containers = len(containers) + len(multi_containers) + len(magic_containers) + len(magic_multi_containers)
    print(f"Initialised {total_items} items including {total_containers} containers.\n")
    
    # start game
    gamestart = Gamesystem(items, containers, multi_containers, magic_containers, magic_multi_containers)
    gamestart.gametable()
