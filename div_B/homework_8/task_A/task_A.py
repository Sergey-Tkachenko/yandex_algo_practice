def add(node, value):
    if node[0] > value:
        if node[1] is None:
            node[1] = [value, None, None]
            print("DONE")
        else:
            add(node[1], value)
    elif node[0] < value:
        if node[2] is None:
            node[2] = [value, None, None]
            print("DONE")
        else:
            add(node[2], value)
    else:
        print("ALREADY")


def search(node, value):
    if node is None:
        print("NO")
    elif node[0] > value:
        search(node[1], value)
    elif node[0] < value:
        search(node[2], value)
    else:
        print("YES")


def printtree(node, depth=0):
    if node is not None:
        printtree(node[1], depth + 1)
        print("." * depth + str(node[0]))
        printtree(node[2], depth + 1)


def main():
    with open("input_5.txt", "r") as f:
        queries = f.readlines()
        ptr = 0
        while (ptr < len(queries)) and (queries[ptr].split()[0] == "SEARCH"):
            print("NO")
            ptr += 1

        # First ADD query
        if ptr < len(queries):
            tree = [int(queries[ptr].split()[-1]), None, None]
            print("DONE")
            ptr += 1

        # Main loop
        for i in range(ptr, len(queries)):
            if queries[i].strip() == 'PRINTTREE':
                printtree(tree)
            else:
                command, value = queries[i].split()
                value = int(value)
                if command == "ADD":
                    add(tree, value)
                else:
                    search(tree, value)


main()