def is_correct_seq(seq):
    cnt = 0
    for i in range(len(seq)):
        if seq[i] == '(':
            cnt += 1
        else:
            cnt -= 1

        if cnt < 0:
            return "NO"

    return "YES" if cnt == 0 else "NO"


with open("input.txt", "r") as f:
    in_seq = f.readline().strip()
    print(is_correct_seq(in_seq))
