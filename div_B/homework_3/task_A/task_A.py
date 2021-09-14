input_seq_1 = list(map(int, input().split()))
input_seq_2 = list(map(int, input().split()))


def count_intersection(seq_1, seq_2):
    set_1 = set(seq_1)

    return len(set_1.intersection(seq_2))


print(count_intersection(input_seq_1, input_seq_2))