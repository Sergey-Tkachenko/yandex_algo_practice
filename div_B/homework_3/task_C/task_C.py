input_seq =list(input().split())


def unique_elem(seq):
    unique = set()
    whole = set()
    for i in range(len(seq)):
        if seq[i] in whole:
            if seq[i] in unique:
                unique.remove(seq[i])
        else:
            whole.add(seq[i])
            unique.add(seq[i])
    ans = []
    for i in range(len(seq)):
        if seq[i] in unique:
            ans.append(seq[i])

    print(" ".join(ans))


unique_elem(input_seq)

