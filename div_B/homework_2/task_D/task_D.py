l, k = list(map(int, input().split()))
input_seq = list(map(int, input().split()))


def find_base(l, k, seq):
    max_left = -1
    min_right = l

    for i in range(k):
        if(seq[i] > max_left) and (seq[i] <= l // 2 - 1 + l % 2):
            max_left = seq[i]

        if (seq[i] < min_right) and (seq[i] >= l // 2):
            min_right = seq[i]

    if min_right == max_left:
        return min_right
    else:
        return max_left, min_right


ans = find_base(l, k, input_seq)

if type(ans) is tuple:
    print(*ans)
else:
    print(ans)
