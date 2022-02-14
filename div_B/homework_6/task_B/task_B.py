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


def find_pos(num, seq):
    l_pt = left_bs(seq, num)
    r_pt = right_bs(seq, num)

    if (seq[l_pt] < num) or (seq[r_pt] > num) or (l_pt > r_pt):
        return "0 0"
    else:
        return f"{l_pt + 1} {r_pt + 1}"


def main():
    with open("input.txt", "r") as f:
        n = f.readline()
        seq = list(map(int, f.readline().split()))
        k = int(f.readline())
        queries = list(map(int, f.readline().split()))
        ans = [""] * k
        for i in range(k):
            ans[i] = find_pos(queries[i], seq)

        for i in range(k):
            print(ans[i])


if __name__ == '__main__':
    main()
