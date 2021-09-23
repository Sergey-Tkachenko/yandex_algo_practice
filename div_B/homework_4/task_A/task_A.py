n = int(input())

input_keys, input_values = [], []
for i in range(n):
    a, d = list(map(int, input().split()))
    input_keys.append(a)
    input_values.append(d)


def count_colors(n, a_seq, d_seq):
    d = {}
    keys = []
    for i in range(n):
        if a_seq[i] not in d.keys():
            d[a_seq[i]] = 0
            keys.append(a_seq[i])

        d[a_seq[i]] += d_seq[i]

    keys = sorted(keys)
    for k in keys:
        print(k, d[k])


count_colors(n, input_keys, input_values)
