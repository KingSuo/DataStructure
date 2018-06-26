def insert_node(value, tree={}):
    """
    向树中插入数据
    :param value:
    :param tree:
    :return:
    """
    if tree:
        for node in tree:
            if value < node:
                if tree[node][0] is None:
                    tree[node][0] = {value: [None, None]}
                else:
                    insert_node(value, tree[node][0])
            elif value > node:
                if tree[node][1] is None:
                    tree[node][1] = {value: [None, None]}
                else:
                    insert_node(value, tree[node][1])
    else:
        tree[value] = [None, None]

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


def delete_node(value, tree):
    """
    删除节点
    :param value: 
    :param tree: 
    :return: 
    """
    pass


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


a = insert_node(35)
insert_node(17, a)
insert_node(39, a)
insert_node(16, a)
insert_node(56, a)
insert_node(87, a)
insert_node(28, a)
print(a)
print_node(a)
t1 = find_node(35, a)
t2 = find_node(56, a)
t3 = find_node(39, a)
t4 = find_node(16, a)
t5 = find_node(87, a)
t6 = find_node(28, a)
t7 = find_node(8, a)
t8 = find_node(80, a)
print(t1, t2, t3, t4, t5, t6, t7, t8)