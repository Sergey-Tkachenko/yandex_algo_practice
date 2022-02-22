def count_painted(events):
    len_painted = 0
    balance = -1
    last_beg = events[0][0]
    for i in range(len(events) - 1):
        if events[i + 1][1] == -1:
            if balance == 0:
                last_beg = events[i + 1][0]
            balance -= 1
        else:
            balance += 1
            if balance == 0:
                len_painted += events[i + 1][0] - last_beg

    return len_painted


def main():
    with open("input_13.txt", "r") as f:
        n = int(f.readline())
        events = [0] * (2 * n)
        for i in range(n):
            beg, end = list(map(int, f.readline().split()))
            events[2 * i] = (beg, -1)
            events[2 * i + 1] = (end, 1)

        events = sorted(events)
        print(count_painted(events))


if __name__ == '__main__':
    main()