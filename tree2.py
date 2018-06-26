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
                if not tree[node][0]:
                    tree[node][0] = {value: [{}, {}]}
                else:
                    insert_node(value, tree[node][0])
            elif value > node:
                if not tree[node][1]:
                    tree[node][1] = {value: [{}, {}]}
                else:
                    insert_node(value, tree[node][1])
    else:
        tree[value] = [{}, {}]

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
    level = 0
    if level == 0:
        tree_bak = tree
    for node in tree:
        if value == node:
            print("Find %s in the tree." % value)
            if not tree[node][0] and not tree[node][1]:
                print('=================')
                print(tree)
                tree_bak = {}
            elif not tree[node][0] and tree[node][1]:
                tree_bak = tree[node][1]
            elif tree[node][0] and not tree[node][1]:
                tree = tree[node][0]
            elif tree[node][0] and tree[node][1]:
                print('========2=========')

                def restructure(temp_tree):
                    tree_list = temp_tree[[i for i in tree.keys()][0]]
                    flag = 0
                    for i in range(len(tree_list)):
                        sub_tree = tree_list[i]
                        for sub_node in sub_tree:
                            if not sub_tree[sub_node][1-i]:     # 解释：以a表示被删除节点，b、c分别表示a的左右两个子节点。当选择左边的子节点b替换被删除节点a时，子节点b的右子节点需为空，以将子节点c插在b的右子节点位置上；选择右边亦同理。所以用1-i来进行交叉判断。
                                sub_tree[sub_node][1 - i] = tree_list[1 - i]
                            else:
                                flag += 1
                                if flag >= 2:
                                    flag = 0
                                    restructure(sub_tree)
                    return tree
                restructure(tree)
        elif value < node:
            if not tree[node][0]:
                print("Cannot delete %s because it is not in the tree." % value)
            else:
                delete_node(value, tree[node][0])
        elif value > node:
            if not tree[node][1]:
                print("Cannot delete %s because it is not in the tree." % value)
            else:
                delete_node(value, tree[node][1])
    return tree_bak


def delete_node2(value, tree, trace=[]):
    """
    删除节点
    :param value: 
    :param tree: 
    :return: 
    """
    for node in tree:
        if value == node:
            print("Find %s in the tree." % value)
            if not tree[node][0] and not tree[node][1]:
                print('=================')
                tree = {}
                print(tree)
            elif not tree[node][0] and tree[node][1]:
                tree = tree[node][1]
            elif tree[node][0] and not tree[node][1]:
                tree = tree[node][0]
            elif tree[node][0] and tree[node][1]:

                def restructure(temp_tree):
                    tree_list = temp_tree[[i for i in tree.keys()][0]]
                    flag = 0
                    for i in range(len(tree_list)):
                        sub_tree = tree_list[i]
                        for sub_node in sub_tree:
                            if not sub_tree[sub_node][1-i]:     # 解释：以a表示被删除节点，b、c分别表示a的左右两个子节点。当选择左边的子节点b替换被删除节点a时，子节点b的右子节点需为空，以将子节点c插在b的右子节点位置上；选择右边亦同理。所以用1-i来进行交叉判断。
                                sub_tree[sub_node][1 - i] = tree_list[1 - i]
                            else:
                                flag += 1
                                if flag >= 2:
                                    flag = 0
                                    restructure(sub_tree)
                    return tree
                restructure(tree)
        elif value < node:
            if not tree[node][0]:
                print("Cannot delete %s because it is not in the tree." % value)
            else:
                trace.append((node, 0))
                delete_node2(value, tree[node][0], trace)
        elif value > node:
            if not tree[node][1]:
                print("Cannot delete %s because it is not in the tree." % value)
            else:
                trace.append((node, 1))
                delete_node2(value, tree[node][1], trace)
    print('+++++++++++++++++')
    print(trace)
    print(type(trace))
    print('+++++++++++++++++')
    print(tree)
    return tree


def delete_node3(value, tree):
    tree_bak = tree
    for node in tree:
        while not value == node:
            if value < node:
                if not tree_bak[node][0]:
                    print("Cannot delete %s because it is not in the tree!" % value)
                    return 0
                else:
                    node = [i for i in tree_bak[node][0].keys()][0]
            elif value > node:
                if not tree[node][1]:
                    print("Cannot delete %s because it is not in the tree!" % value)
                    break
        return {}


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

a = delete_node2(87, a)
print(a)
print_node(a)
