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

    a = delete_node(35, a, merge_to="left")
    print(a)
    print_node(a)
    # a = delete_node(87, a, merge_to="left")
    # print(a)
    # print_node(a)
    # a = delete_node(35, a, merge_to="left")
    # print(a)
    # print_node(a)
