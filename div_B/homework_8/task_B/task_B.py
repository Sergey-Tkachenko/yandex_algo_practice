def is_ancestor(child, parent, graph: dict):
    if child not in graph.keys():
        return False
    else:
        if graph[child] == parent:
            return True
        else:
            return is_ancestor(graph[child], parent, graph)


def main():
    with open("input.txt", "r") as f:
        n = int(f.readline())
        graph = dict()
        for i in range(n - 1):
            child, parent = f.readline().split()
            graph[child] = parent

        queries = f.readlines()
        for i in range(len(queries)):
            name_1, name_2 = queries[i].split()
            if is_ancestor(name_1, name_2, graph):
                print(2, end=" ")
            elif is_ancestor(name_2, name_1, graph):
                print(1, end=" ")
            else:
                print(0, end=" ")


main()
