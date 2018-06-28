import numpy as np


class BinarySearchTree:
    def __init__(self, node_list):
        # self.No_of_nodes = len(node_list)
        self.node_list = list(node_list)
        self.tree = self._insert_node(node_list)

    def _insert_node(self, node_list):
        tree = {}
        try:
            node_list = sorted(node_list)
        except TypeError as e:
            node_list = [node_list]
            print(e)
        if len(node_list) == 0:
            return tree
        mapping_list = np.arange(len(node_list))
        node_index = (mapping_list[0] + mapping_list[-1] + 1) // 2
        node_value = node_list[node_index]
        tree[node_value] = [{}, {}]
        slice_list = [slice(0, node_index), slice(node_index + 1, mapping_list[-1] + 1)]
        for j in range(2):
            tree[node_value][j] = self._insert_node(node_list[slice_list[j]])
        return tree

    def insert_node(self, node_list, flag=0):
        tree = {}
        if not flag:
            node_list = self.node_list + node_list
            self.node_list = node_list
        try:
            node_list = sorted(node_list)
        except TypeError as e:
            node_list = [node_list]
            print(e)
        if len(node_list) == 0:
            return tree
        mapping_list = np.arange(len(node_list))
        node_index = (mapping_list[0] + mapping_list[-1] + 1) // 2
        node_value = node_list[node_index]
        tree[node_value] = [{}, {}]
        slice_list = [slice(0, node_index), slice(node_index + 1, mapping_list[-1] + 1)]
        for j in range(2):
            tree[node_value][j] = self.insert_node(node_list[slice_list[j]], 1)
        self.tree = tree

        return tree

    def is_exist(self, node):
        if node in self.node_list:
            print("Find the node %s in the tree!" % node)
            return 1
        else:
            print("Cannot find the node %s in the tree!" % node)
            return 0

    def delete_node(self, node_list):
        if isinstance(node_list, (tuple, list, dict, set)) and len(node_list) > 0:
            pass
        else:
            node_list = [node_list]
        for node in node_list:
            if self.is_exist(node):
                self.node_list.pop(self.node_list.index(node))
            else:
                print("Cannot delete this node %s because it doesn't exist in the tree!" % node)
        self.tree = self._insert_node(self.node_list)
        return self.tree

    def change_node(self, old_node_list, new_node_list):
        if isinstance(old_node_list, (tuple, list, dict, set)) and isinstance(new_node_list, (tuple, list, dict, set)):
            if len(old_node_list) == len(new_node_list) and len(old_node_list) > 0:
                pass
            else:
                print("The input elements 'old_node_list' and 'new_node_list' must have same length and large than 0!")
                return 0
        else:
            print("The input elements 'old_node_list' and 'new_node_list' must be iterable!")
            return 0
        for i in range(len(old_node_list)):
            old_node = old_node_list[i]
            new_node = new_node_list[i]
            if self.is_exist(old_node):
                index = self.node_list.index(old_node)
                self.node_list.pop(index)
                self.node_list.insert(index, new_node)
            else:
                print("Cannot delete this node %s because it doesn't exist in the tree!" % old_node)
        self.tree = self._insert_node(self.node_list)

        return self.tree


if __name__ == '__main__':
    a = np.arange(120)
    b = BinarySearchTree(a)
    print("======function insert_node() test=========")
    c = b.insert_node([-23, 45, 453, 232])
    print("b.node_list:", b.node_list)
    print("b.tree: ", b.tree)

    print("======functions is_exist() and delete_node() test=======")
    b.is_exist(-1213)
    b.is_exist(12)
    b.is_exist(46)
    b.is_exist(100)
    b.delete_node([12, 46, 100])
    b.is_exist(12)
    b.is_exist(46)
    b.is_exist(100)
    print("b.tree: ", b.tree)

    print("=======function change_node() test=======")
    b.is_exist(2)
    b.is_exist(4)
    b.is_exist(10)
    b.is_exist(11)
    b.is_exist(12)
    b.is_exist(17)
    print('----------------------------------')
    b.is_exist(-2)
    b.is_exist(-4)
    b.is_exist(-10)
    b.is_exist(-11)
    b.is_exist(-12)
    b.is_exist(-17)
    print('----------------------------------')

    b.change_node([2, 4, 10, 11, 12, 17], [-2, -4, -10, -11, -12, -17])
    print("b.tree: ", b.tree)

    b.is_exist(2)
    b.is_exist(4)
    b.is_exist(10)
    b.is_exist(11)
    b.is_exist(12)
    b.is_exist(17)
    print('----------------------------------')
    b.is_exist(-2)
    b.is_exist(-4)
    b.is_exist(-10)
    b.is_exist(-11)
    b.is_exist(-12)
    b.is_exist(-17)