from sys import setrecursionlimit


def max_dist(graph, leaves, dists):
    new_leafs = set()
    for leaf in leaves:
        for node in graph[leaf]:
            graph[node].remove(leaf)

            cnt = len(graph[node])
            if cnt == 0:
                return dists[leaf] + dists[node]
            elif cnt == 1:
                new_leafs.add(node)

            dists[node] = max(dists[node], dists[leaf] + 1)

    return max_dist(graph, new_leafs, dists)


def main():
    with open("input_8.txt", 'r') as f:
        n = int(f.readline())
        if n == 1:
            return 0

        dists = [0] * n

        graph = [set()] * n
        for i in range(n):
            graph[i] = set()

        for i in range(n - 1):
            n_1, n_2 = list(map(int, f.readline().split()))
            n_1 -= 1
            n_2 -= 1
            graph[n_1].add(n_2)
            graph[n_2].add(n_1)

        init_leafs= set()
        for i in range(n):
            if len(graph[i]) == 1:
                init_leafs.add(i)
                dists[i] = 1
        return max_dist(graph, init_leafs, dists)


setrecursionlimit(10 ** 9)
print(main())
