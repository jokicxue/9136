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

    # set instance variables for containers name, empty weight, capacity and what items contained
    def __init__(self, cont_name, cont_empty_weight, cont_capacity):
        self.cont_name = cont_name
        self.cont_empty_weight = cont_empty_weight
        self.cont_capacity = cont_capacity
        self.cont_items = []

    # calculate how much capacity is being used
    def used_capacity(self):
        return sum(item.item_weight for item in self.cont_items)

    # calculate the total weight of the container
    def total_weight(self):
        return self.cont_empty_weight + self.used_capacity()

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


if __name__ == "__main__":
    # read the container and item files
    containers = Container.read_container("containers.csv")
    items = Item.read_item("items.csv")

    # calculate the number of items including containers
    total_items = len(containers) + len(items)

    #
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