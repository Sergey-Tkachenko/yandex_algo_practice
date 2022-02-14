def count_intervals(l, seq):
    rb = seq[0] - 1
    cnt = 0

    for i in range(len(seq)):
        if seq[i] > rb:
            rb = seq[i] + l
            cnt += 1

    return cnt


def left_bs(k, l_0, r_0, f, args):
    l = l_0
    r = r_0

    while l < r:
        m = l + (r - l) // 2
        if f(m, *args) <= k:
            r = m
        else:
            l = m + 1

    return l


def main():
    with open("input_10.txt", "r") as f:
        n, k = list(map(int, f.readline().split()))
        seq = list(map(int, f.readline().split()))
        seq = sorted(seq)

        print(left_bs(k, 0, seq[n-1] - seq[0], count_intervals, [seq]))


if __name__ == '__main__':
    main()
