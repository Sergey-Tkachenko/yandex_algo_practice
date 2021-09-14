in_m = int(input())
in_lookers_sets = []
for i in range(in_m):
    in_lookers_sets.append(set(input()))

in_n = int(input())
in_suspects = []
for i in range(in_n):
    in_suspects.append(input())


def find_most_wanted(m, lookers, n, suspects):
    most_wanted = []
    max_freq = -1
    susp_sets = list(map(set, suspects))

    for i in range(n):
        now = 0
        for j in range(m):
            if lookers[j].issubset(susp_sets[i]):
                now += 1

        if now > max_freq:
            max_freq = now
            most_wanted = [i]
        elif now == max_freq:
            most_wanted.append(i)

    return most_wanted


ans = find_most_wanted(in_m, in_lookers_sets, in_n, in_suspects)
for i in range(len(ans)):
    print(in_suspects[ans[i]])
