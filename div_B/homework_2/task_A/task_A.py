input_seq = []
now = int(input())
while now != 0:
    input_seq.append(now)
    now = int(input())


def count_max(seq):
    if len(seq) == 0:
        return 0

    seq_max = seq[0]
    cnt = 1
    for i in range(1, len(seq)):
        if seq[i] > seq_max:
            seq_max = seq[i]
            cnt = 1
        elif seq[i] == seq_max:
            cnt += 1

    return cnt


print(count_max(input_seq))
