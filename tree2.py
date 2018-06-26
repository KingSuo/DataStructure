def insert_node(value, tree={}):
    """
    向树中插入数据
    :param value:
    :param tree:
    :return:
    """
    if tree:
        for key in tree:
            if value < key:
                if tree[key][0] is None:
                    tree[key][0] = {value: [None, None]}
                else:
                    insert_node3(value, tree[key][0])
            elif value > key:
                if tree[key][1] is None:
                    tree[key][1] = {value: [None, None]}
                else:
                    insert_node3(value, tree[key][1])
    else:
        tree[value] = [None, None]

    return tree


def print_node(tree):
    """
    打印树中数据
    :param tree:
    :return:
    """
    if tree:
        for i in tree:
            print(i)
            if tree[i][0]:
                print_node(tree[i][0])
            if tree[i][1]:
                print_node(tree[i][1])