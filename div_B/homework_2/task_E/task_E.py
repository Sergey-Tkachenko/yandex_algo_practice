n = int(input())
input_seq = list(map(int, input().split()))


def worst_time(n, seq):
    cnt = 0
    max_vol = 0
    for i in range(n):
        cnt += seq[i]
        if seq[i] > max_vol:
            max_vol = seq[i]

    return cnt - max_vol


print(worst_time(n, input_seq))
