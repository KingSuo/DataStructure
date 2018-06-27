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


def delete_node2(value, tree, trace=[], tree_bak=None, tree_bak2=None):
    """
    删除节点
    :param value:
    :param tree:
    :param trace:
    :param tree_bak:
    :return:
    """
    if not trace:
        tree_bak = tree     # 利用浅拷贝“顶层复制”性质保存内部节点数据
        tree_bak2 = tree
    for node in tree:
        if value == node:
            print("Find %s in the tree." % value)
            if not tree[node][0] and not tree[node][1]:
                print(trace)
                for i in range(len(trace) -1):
                    trace_node, j = trace[i]
                    tree_bak = tree_bak[trace_node][j]
                trace_node, j = trace[-1]
                tree_bak[trace_node][j] = {}
            elif not tree[node][0] and tree[node][1]:
                print(trace)
                for i in range(len(trace) - 1):
                    trace_node, j = trace[i]
                    tree_bak = tree_bak[trace_node][j]
                trace_node, j = trace[-1]
                tree_bak[trace_node][j] = tree[node][1]
                # tree = tree[node][1]
            elif tree[node][0] and not tree[node][1]:
                print("trace:", trace)
                for i in range(len(trace) - 1):
                    trace_node, j = trace[i]
                    tree_bak = tree_bak[trace_node][j]
                trace_node, j = trace[-1]
                tree_bak[trace_node][j] = tree[node][0]
                # tree = tree[node][0]
            elif tree[node][0] and tree[node][1]:
                print("trace:", trace)
                sub_trace = [[], []]        # 存放被删除节点的子节点信息
                for i in range(2):
                    print("tree:", tree)
                    tree_bak3 = tree
                    sub_trace[i].append((node, i))
                    tree_bak3 = tree_bak3[node][i]
                    sub_node = [temp for temp in tree_bak3.keys()][0]
                    sub_trace[i].append((sub_node, 1 - i))
                    while tree_bak3[sub_node][1 - i]:
                        tree_bak3 = tree_bak3[sub_node][1 - i]
                        sub_node = [temp for temp in tree_bak3.keys()][0]
                        sub_trace[i].append((sub_node, 1 - i))
                print('sub_trace: ', sub_trace)

                # for t in range(len(sub_trace)):
                for t in range(1):
                    total_trace = trace + sub_trace[t]
                    for i in range(len(total_trace) - 1):
                        trace_node, j = total_trace[i]
                        tree_bak = tree_bak[trace_node][j]
                    for i in range(len(trace) -1):
                        trace_node, j = trace[i]
                        tree_bak2 = tree_bak2[trace_node][j]
                    trace_node, j = total_trace[-1]
                    tree_bak[trace_node][j] = tree[node][1]
                    print("tree_bak2: ", tree_bak2)
                    trace_node3, j3 = trace[-1]
                    tree_bak2[trace_node3][j3] = tree_bak
                    print(trace_node, j)
                print("tree: ", tree)
                print("tree_bak: ", tree_bak)
                print("tree_bak2: ", tree_bak2)
        elif value < node:
            if not tree[node][0]:
                print("Cannot delete %s because it is not in the tree." % value)
            else:
                trace.append((node, 0))
                delete_node2(value, tree[node][0], trace, tree_bak, tree_bak2)
        elif value > node:
            if not tree[node][1]:
                print("Cannot delete %s because it is not in the tree." % value)
            else:
                trace.append((node, 1))
                delete_node2(value, tree[node][1], trace, tree_bak, tree_bak2)
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
insert_node(36, a)
insert_node(40, a)
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

a = delete_node2(17, a)
print(a)
print_node(a)
# print(a[35][1][39][1][56][1])