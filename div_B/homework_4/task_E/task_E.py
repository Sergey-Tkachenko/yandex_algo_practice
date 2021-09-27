def count_node(g, node):
    if node not in g.keys():
        return 0

    ans = len(g[node])
    for now in g[node]:
        ans += count_node(g, now)

    return ans


def find_most_popular(n):
    topics = {}
    g = {}

    for i in range(n):
        idx = int(input())
        if idx == 0:
            topic = input()
            topics[topic] = i + 1
        else:
            if idx not in g.keys():
                g[idx] = []
            g[idx].append(i + 1)
        input()

    max_cnt = 0
    ans = None
    for topic in topics:
        cnt = count_node(g, topics[topic]) + 1
        if cnt > max_cnt:
            max_cnt = cnt
            ans = topic

    return ans


print(find_most_popular(int(input())))
