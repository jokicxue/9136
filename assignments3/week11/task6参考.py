class Item:
    def __init__(self, name, weight):
        self.name = name
        self.weight = weight

    def __str__(self):
        return f"{self.name} (weight: {self.weight})"


class Container(Item):
    def __init__(self, name, empty_weight, capacity, is_magic=False):
        super().__init__(name, empty_weight)  # 调用Item的初始化
        self.capacity = capacity  # 当前容器的最大容量
        self.is_magic = is_magic  # 是否是魔法容器
        self.contents = []  # 容器中的物品列表

    def current_weight(self):
        # 计算当前容器的总重量（容器自重 + 所有物品重量）
        return self.weight + sum(item.weight for item in self.contents)

    def current_capacity(self):
        # 计算当前容器的已用容量
        return sum(item.weight for item in self.contents)

    def can_store(self, item):
        # 判断容器是否有足够的容量存储物品
        return self.current_capacity() + item.weight <= self.capacity

    def store_item(self, item):
        # 尝试将物品存储到容器中
        if self.can_store(item):
            self.contents.append(item)
            print(f'Success! Item "{item.name}" stored in container "{self.name}".')
        else:
            print(f'Failure! Item "{item.name}" NOT stored in container "{self.name}".')

    def store_item_recursively(self, item):
        # 尝试存储物品到当前容器或递归存储到内部容器
        if self.can_store(item):
            self.store_item(item)  # 直接存储物品
            return True

        # 如果当前容器无法存储，遍历内容物看是否有子容器可以存储
        for content in self.contents:
            if isinstance(content, Container) and content.store_item_recursively(item):
                if not content.is_magic:
                    self.weight += item.weight  # 如果不是魔法容器，更新重量
                return True

        return False

    def __str__(self):
        items_str = "\n   ".join(str(item) for item in self.contents)
        return f"{self.name} (total weight: {self.current_weight()}, empty weight: {self.weight}, capacity: {self.current_capacity()}/{self.capacity})\n   {items_str}"
