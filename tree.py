class BinarySearchTree:
    """
    二叉搜索树
    """
    def __init__(self, node):
        self.node = node
        self.left_node = -float('inf')
        self.right_node = float('inf')
        self.parent_node = None

    def __lt__(self, value):
        return self.node < value

    def __gt__(self, value):
        return self.node > value

    def __str__(self):
        return str(self.node)

    def insert_node(self, new_node):
        """
        插入节点，将形成两条单链，性能差
        :param new_node:数值型数据
        """
        if new_node > self.node:
            while new_node > self.node and new_node > self.right_node:
                self = self.right_node
            new_node = BinarySearchTree(new_node)
            new_node.parent_node = self
            new_node.right_node = self.right_node
            self.right_node = new_node
        elif new_node < self.node:
            while new_node < self.node and new_node < self.left_node:
                self = self.left_node
            new_node = BinarySearchTree(new_node)
            new_node.parent_node = self
            new_node.left_node = self.left_node
            self.left_node = new_node

    def insert_node2(self, value):
        """
        插入节点
        :param new_node:数值型数据
        """
        if value > self.node:
            if isinstance(self.right_node, float):
                new_node = BinarySearchTree(value)
                new_node.parent_node = self
                self.right_node = new_node
                return
            else:
                self.insert_node2(value, self.right_node)
        elif value < self.node:
            if isinstance(self.left_node, float):
                print('OK')
                new_node = BinarySearchTree(value)
                new_node.parent_node = self
                self.left_node = new_node
                return
            else:
                self.insert_node2(value, self.left_node)


def insert_node(new_node, tree):
    if new_node > tree.node:
        while new_node > tree.node and new_node > tree.right_node:
            tree = tree.right_node
        new_node = BinarySearchTree(new_node)
        new_node.parent_node = tree
        new_node.right_node = tree.right_node
        tree.right_node = new_node
    elif new_node < tree.node:
        while new_node < tree.node and new_node < tree.left_node:
            tree = tree.left_node
        new_node = BinarySearchTree(new_node)
        new_node.parent_node = tree
        new_node.left_node = tree.left_node
        tree.left_node = new_node


tree = BinarySearchTree(35)
print(tree)
print(tree.node)
print(tree.left_node)
print(tree.right_node)
print(tree.parent_node)

tree.insert_node(17)
tree.insert_node(39)
tree.insert_node(9)
tree.insert_node(56)
tree.insert_node(87)
tree.insert_node(65)
tree.insert_node(28)

print('================')
print(tree.left_node)
print(tree.right_node)
print(tree.parent_node)

print('================')
print(tree.node)
print(tree.left_node)
print(tree.left_node.left_node)
print(tree.left_node.right_node)
print(tree.right_node)
print(tree.right_node.right_node)
print(tree.right_node.right_node.left_node)
print(tree.right_node.right_node.right_node)
print(tree.right_node.right_node.right_node.right_node)

tree2 = BinarySearchTree(35)

insert_node(17, tree2)
insert_node(39, tree2)
insert_node(9, tree2)
insert_node(56, tree2)
insert_node(87, tree2)
insert_node(65, tree2)
insert_node(28, tree2)

print('================')
print(tree2.node)
print(tree2.left_node)
print(tree2.left_node.left_node)
print(tree2.left_node.right_node)
print(tree2.right_node)
print(tree2.right_node.right_node)
print(tree2.right_node.right_node.left_node)
print(tree2.right_node.right_node.right_node)
print(tree2.right_node.right_node.right_node.right_node)


tree3 = BinarySearchTree(35)
print(tree3)
print(tree3.node)
print(tree3.left_node)
print(tree3.right_node)
print(tree3.parent_node)

tree3.insert_node(17)
tree3.insert_node(39)
tree3.insert_node(9)
tree3.insert_node(56)
tree3.insert_node(87)
tree3.insert_node(65)
tree3.insert_node(28)

print('================')
print(tree3.node)
print(tree3.left_node)
print(tree3.left_node.left_node)
print(tree3.left_node.right_node)
print(tree3.right_node)
print(tree3.right_node.right_node)
print(tree3.right_node.right_node.left_node)
print(tree3.right_node.right_node.right_node)
print(tree3.right_node.right_node.right_node.right_node)
