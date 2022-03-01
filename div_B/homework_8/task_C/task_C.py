from sys import setrecursionlimit


def find_root(graph, curr):
    if graph[curr][0] is None:
        return curr
    else:
        return find_root(graph, graph[curr][0])


def set_depth(graph, curr, depth=0):
    graph[curr][-1] = depth
    for i in range(len(graph[curr][1])):
        set_depth(graph, graph[curr][1][i], depth + 1)


def find_lca(graph, p_1, p_2):
    while graph[p_1][-1] > graph[p_2][-1]:
        p_1 = graph[p_1][0]

    while graph[p_1][-1] < graph[p_2][-1]:
        p_2 = graph[p_2][0]

    if p_1 == p_2:
        return p_1
    else:
        return find_lca(graph, graph[p_1][0], graph[p_2][0])


def main():
    with open("012", "r") as f:
        n = int(f.readline())
        d = dict()
        for i in range(n - 1):
            child, parent = f.readline().split()

            if parent in d.keys():
                d[parent][1].append(child)
            else:
                d[parent] = [None, [child], -1]

            if child in d.keys():
                d[child][0] = parent
            else:
                d[child] = [parent, [], -1]

        root = find_root(d, list(d.keys())[0])
        set_depth(d, root, 0)

        queries = f.readlines()
        for i in range(len(queries)):
            name_1, name_2 = queries[i].split()
            print(find_lca(d, name_1, name_2))


setrecursionlimit(10 ** 9)
# threading.stack_size(2 ** 26)
# thread = threading.Thread(target=main)
# thread.start()
main()