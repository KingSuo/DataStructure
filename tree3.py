import numpy as np


class BinarySearchTree:
    def __init__(self, node_list):
        self.No_of_nodes = len(node_list)
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


def find_node(value, tree):
    """
    查找节点
    :param value:
    :param tree:
    :return:
    """
    flag = 0
    for node in tree:
        if value == node:
            print("Find %s in the tree." % value)
            flag = 1
        elif value < node:
            if not tree[node][0]:
                print("%s is not in the tree." % value)
                flag = 0
            else:
                flag = find_node(value, tree[node][0])
        elif value > node:
            if not tree[node][1]:
                print("%s is not in the tree." % value)
                flag = 0
            else:
                flag = find_node(value, tree[node][1])
    return flag


def delete_node(value, tree, trace=[], tree_bak=None, tree_bak2=None, merge_to="right"):
    """
    删除节点
    :param value:删除的节点数值
    :param tree:树
    :param trace:记录节点数值，无需赋值
    :param tree_bak:树备份，无需赋值
    :param tree_bak2:树备份，无需赋值
    :param merge_to:当删除节点时，指定删除后合并方向
    :return:删除节点后的树
    """
    if not trace:
        tree_bak = tree     # 利用浅拷贝“顶层复制”性质保存内部节点数据
        tree_bak2 = tree
    for node in tree:
        if value == node:
            print("Find %s in the tree." % value)
            if not tree[node][0] and not tree[node][1]:
                # print("trace:", trace)
                if trace:
                    for i in range(len(trace) -1):
                        trace_node, j = trace[i]
                        tree_bak = tree_bak[trace_node][j]
                    trace_node, j = trace[-1]
                    tree_bak[trace_node][j] = {}
                else:
                    tree = {}
            elif not tree[node][0] and tree[node][1]:
                # print("trace:", trace)
                if trace:
                    for i in range(len(trace) - 1):
                        trace_node, j = trace[i]
                        tree_bak = tree_bak[trace_node][j]
                    trace_node, j = trace[-1]
                    tree_bak[trace_node][j] = tree[node][1]
                else:
                    tree = tree[node][1]
            elif tree[node][0] and not tree[node][1]:
                # print("trace:", trace)
                if trace:
                    for i in range(len(trace) - 1):
                        trace_node, j = trace[i]
                        tree_bak = tree_bak[trace_node][j]
                    trace_node, j = trace[-1]
                    tree_bak[trace_node][j] = tree[node][0]
                else:
                    tree = tree[node][0]
            elif tree[node][0] and tree[node][1]:
                print("trace:", trace)
                sub_trace = [[], []]        # 存放被删除节点的子节点信息
                for i in range(2):
                    tree_bak3 = tree
                    sub_trace[i].append((node, i))
                    tree_bak3 = tree_bak3[node][i]
                    sub_node = [temp for temp in tree_bak3.keys()][0]
                    sub_trace[i].append((sub_node, 1 - i))
                    while tree_bak3[sub_node][1 - i]:
                        tree_bak3 = tree_bak3[sub_node][1 - i]
                        sub_node = [temp for temp in tree_bak3.keys()][0]
                        sub_trace[i].append((sub_node, 1 - i))

                if merge_to == "right":
                    t = 1
                elif merge_to == "left":
                    t = 0
                else:
                    print("Error for merge_to input! You can only input 'right' or 'left'!")
                    return 0
                total_trace = trace + sub_trace[t]
                for i in range(len(total_trace) - 1):
                    trace_node, j = total_trace[i]
                    tree_bak = tree_bak[trace_node][j]
                for i in range(len(trace) -1):
                    trace_node, j = trace[i]
                    tree_bak2 = tree_bak2[trace_node][j]
                trace_node, j = total_trace[-1]
                tree_bak[trace_node][j] = tree[node][1 - t]
                trace_node3, j3 = trace[-1]
                tree_bak2[trace_node3][j3] = tree_bak
        elif value < node:
            if not tree[node][0]:
                print("Cannot delete %s because it is not in the tree." % value)
            else:
                trace.append((node, 0))
                delete_node(value, tree[node][0], trace, tree_bak, tree_bak2, merge_to)
        elif value > node:
            if not tree[node][1]:
                print("Cannot delete %s because it is not in the tree." % value)
            else:
                trace.append((node, 1))
                delete_node(value, tree[node][1], trace, tree_bak, tree_bak2, merge_to)
    return tree


def print_node(tree):
    """
    打印树中数据
    :param tree:树
    :return:无
    """
    if tree:
        for i in tree:
            print(i)
            if tree[i][0]:
                print_node(tree[i][0])
            if tree[i][1]:
                print_node(tree[i][1])


if __name__ == '__main__':
    a = np.arange(12)
    b = BinarySearchTree(a)
    c = b.insert_node([23, 45, 453, 23])
    print_node(b.tree)