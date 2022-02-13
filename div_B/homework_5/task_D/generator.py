import itertools


def is_correct_slow(seq):
    lefts = []
    for i in range(len(seq)):
        if seq[i] == "(":
            lefts.append([i, False])
        else:
            flag = True
            for j in range(len(lefts) - 1, -1, -1):
                if (not lefts[j][1]) and (lefts[j][0] < i):
                    lefts[j][1] = True
                    flag = False
                    break

            if flag:
                return "NO"

    for i in range(len(lefts)):
        if not lefts[i][1]:
            return "NO"

    return "YES"


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


# with open("input_9.txt", "r") as f:
#     in_seq = f.readline()
#     print(is_correct_slow(in_seq))

def random_seq_gen(l=2):
    grid = [[0, 1]] * l
    for seq in itertools.product(*grid):
        s = "".join(["(" if seq[i] == 0 else ")" for i in range(len(seq))])
        yield s


for i in range(20):
    for seq in random_seq_gen(i):
        # print(seq)
        ans_slow = is_correct_slow(seq)
        ans = is_correct_seq(seq)

        if not ans_slow == ans:
            print("Bad seq:", seq)
            print("Slow answer:", ans_slow)
            print("Ans:", ans)


