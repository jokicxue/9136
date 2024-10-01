class Item:
    def __init__(self, name, weight):
        self.name = name
        self.weight = weight


class Backpack:
    def __init__(self, name, empty_weight, weight_capacity):
        self.name = name
        self.empty_weight = empty_weight
        self.weight_capacity = weight_capacity
        self.current_weight = 0
        self.items = []

    def add_item(self, item):
        if self.current_weight + item.weight <= self.weight_capacity:
            self.items.append(item)
            self.current_weight += item.weight
            return True
        return False

    def remaining_capacity(self):
        return self.weight_capacity - self.current_weight

    def total_weight(self):
        return self.empty_weight + self.current_weight

    def __str__(self):
        return (f"{self.name} (total weight: {self.total_weight()}, "
                f"empty weight: {self.empty_weight}, "
                f"capacity: {self.remaining_capacity()}/{self.weight_capacity})")

    def display_contents(self, indent=""):
        result = f"{indent}{self}\n"
        for item in self.items:
            result += f"{indent}   {item.name} (weight: {item.weight})\n"
        return result


class Container(Backpack):
    def __init__(self, name):
        super().__init__(name, empty_weight=0, weight_capacity=0)
        self.backpacks = []

    def add_backpack(self, backpack):
        self.backpacks.append(backpack)

    def display_contents(self, indent=""):
        result = super().display_contents(indent)
        for backpack in self.backpacks:
            result += backpack.display_contents(indent + "   ")
        return result


def create_items():
    return [
        Item("A rock", 1),
        Item("Pierre's outdated meme collection", 9001),
        Item("A normal cheese platter", 1000),
        Item("Taylor's ex-lovers list", 999),
        Item("Ed's forum posts", 678),
        # 这里可以添加更多的物品
    ]


def create_containers_and_backpacks():
    containers_data = [
        ("A coles shopping cart", ["A coles shopping bag", "A backpack", "A woolworths shopping bag", "A coles shopping bag"]),
        ("A suitcase", ["A backpack"]),
        # 这里可以添加更多的容器和背包
    ]
    
    containers = []
    for container_name, backpack_names in containers_data:
        container = Container(container_name)
        for backpack_name in backpack_names:
            backpack = Backpack(backpack_name, empty_weight=40, weight_capacity=5000)
            container.add_backpack(backpack)
        containers.append(container)
    
    return containers


def main():
    items = create_items()
    containers = create_containers_and_backpacks()
    
    print(f"Initialised {len(items)} items including {len(containers)} containers.")
    
    while True:
        container_name = input("Enter the name of the container: ")
        container = next((c for c in containers if c.name == container_name), None)

        if not container:
            print(f'"{container_name}" not found. Try again.')
            continue

        while True:
            print("==================================")
            print("Enter your choice:")
            print("1. Loot item.")
            print("2. List looted items.")
            print("0. Quit.")
            print("==================================")
            choice = input()

            if choice == '1':
                item_name = input("Enter the name of the item: ")
                item = next((i for i in items if i.name == item_name), None)

                if not item:
                    print(f'Failure! Item "{item_name}" NOT stored in container "{container.name}".')
                    continue

                if container.add_item(item):
                    print(f'Success! Item "{item.name}" stored in container "{container.name}".')
                else:
                    print(f'Failure! Item "{item.name}" NOT stored in container "{container.name}".')

            elif choice == '2':
                print(container.display_contents())

            elif choice == '0':
                break


if __name__ == "__main__":
    main()
