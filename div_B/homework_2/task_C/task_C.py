input_seq = input()


def countassym(seq):
    n = len(seq)
    if n == 0:
        return 0
    else:
        cnt = 0
        for i in range(n // 2):
            if seq[i] != seq[n - 1 - i]:
                cnt += 1

        return cnt


print(countassym(input_seq))
