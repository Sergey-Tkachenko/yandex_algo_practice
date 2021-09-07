input_seq = list(map(int, input().split()))


def count_max_dist(seq):
    left_flag = False
    left_shop = -1
    left_dist_seq = []

    for i in range(len(seq)):
        if seq[i] == 2:
            left_flag = True
            left_shop = i

        elif seq[i] == 1:
            if left_flag:
                left_dist_seq.append(i - left_shop)
            else:
                left_dist_seq.append(10)  # larger that any possible

    right_flag = False
    right_shop = -1
    right_dist_seq = [] # inverse order

    for i in range(len(seq) - 1, -1, -1):
        if seq[i] == 2:
            right_flag = True
            right_shop = i

        elif seq[i] == 1:
            if right_flag:
                right_dist_seq.append(right_shop - i)
            else:
                right_dist_seq.append(10)

    max_dist = 0
    for i in range(len(left_dist_seq)):
        now = min(left_dist_seq[i], right_dist_seq[len(right_dist_seq) - i - 1])
        if now > max_dist:
            max_dist = now

    return max_dist


print(count_max_dist(input_seq))
