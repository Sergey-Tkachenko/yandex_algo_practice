def left_bs(seq, lb):
    l = 0
    r = len(seq) - 1
    while l < r:
        m = l + (r - l) // 2
        if seq[m] >= lb:
            r = m
        else:
            l = m + 1

    return l


def right_bs(seq, rb):
    l = 0
    r = len(seq) - 1
    while l < r:
        m = l + (r - l + 1) // 2
        if seq[m] <= rb:
            l = m
        else:
            r = m - 1

    return l


def find_cnt(l, r, seq):
    l_pt = left_bs(seq, l)
    r_pt = right_bs(seq, r)
    if (seq[l_pt] < l) or (seq[r_pt] > r) or (l_pt > r_pt):
        return 0
    else:
        return r_pt - l_pt + 1


def main():
    f = open("input.txt", "r")
    n = int(f.readline())
    seq = list(map(int, f.readline().split()))
    seq = sorted(seq)
    k = int(f.readline())
    ans = [0] * k
    for i in range(k):
        l, r = list(map(int, f.readline().split()))
        ans[i] = find_cnt(l, r, seq)

    print(" ".join(map(str, ans)))


main()

