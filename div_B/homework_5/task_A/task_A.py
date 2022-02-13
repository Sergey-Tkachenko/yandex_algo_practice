import time
t_0 = time.time()

with open("input_1.txt", "r") as f:
    n, q = list(map(int, f.readline().split()))
    in_seq = list(map(int, f.readline().split()))

    pr_sum = [0] * (len(in_seq) + 1)
    for i in range(len(in_seq)):
        pr_sum[i + 1] = pr_sum[i] + in_seq[i]

    for _ in range(q):
        l, r = list(map(int, f.readline().split()))
        print(pr_sum[r] - pr_sum[l - 1])

print("Total time = ", time.time() - t_0)