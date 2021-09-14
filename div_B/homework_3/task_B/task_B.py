input_seq = list(map(int, input().split()))


def isinseq(seq):
    my_set = set()
    for item in seq:
        if item in my_set:
            print("YES")
        else:
            print("NO")
            my_set.add(item)


isinseq(input_seq)