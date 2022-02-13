def find_pr_sum(seq):
    pr_sum = [0] * (len(seq) + 1)
    for i in range(len(seq)):
        pr_sum[i + 1] = pr_sum[i] + seq[i]

    return pr_sum


with open("input.txt", "r") as f:
    n = int(f.readline())
    in_seq = list(map(int, f.readline().split()))
    pr_sum = find_pr_sum(in_seq)
    min_now = 0
    for i in range(n):
        t = pr_sum[i + 1]
        pr_sum[i + 1] -= min_now
        if min_now > t:
            min_now = t

    print(max(pr_sum[1:]))
