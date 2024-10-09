'''
This program is designed to read 2 files and list the details of the information.
container.csv: is the information about different type of containers
items.csv: is the information about different times
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

    def used_capacity(self) -> int:
        '''
        calculate how much capacity is being used
        '''
        return sum(item.item_weight for item in self.cont_items)

    def total_weight(self) -> int:
        '''
        calculate the total weight of the container
        '''
        return self.cont_empty_weight + self.used_capacity()

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
            next(reader)

        # add each item into items list
            for row in reader:
                item = Item(row[0].strip(), int(row[1].strip()))
                items.append(item)

        # return items list and sort items by name
        return sorted(items, key=lambda x: x.item_name)


if __name__ == "__main__":
    # read the container and item files
    containers = Container.read_container("containers.csv")
    items = Item.read_item("items.csv")

    # calculate the number of items including containers
    total_items = len(containers) + len(items)
    print(f"Initialised {total_items} items including {len(containers)} containers.\n")

    # print all items
    print("Items:")
    for item in items:
        print(item)

    # print all containers
    print("\nContainers:")
    for container in containers:
        print(container)
    print("")