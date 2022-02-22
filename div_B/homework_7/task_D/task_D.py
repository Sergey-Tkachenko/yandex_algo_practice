def count_pussies(intervals, pussies):
    n = len(pussies)
    m = len(intervals)

    pussies = sorted(pussies)
    events = [[0, 0]] * (2 * m)
    for i in range(m):
        events[2 * i] = [intervals[i][0], -1]
        events[2 * i + 1] = [intervals[i][1], 1]
    events = sorted(events)

    ptr = 0
    begs, ends = dict(), dict()
    for i in range(len(events)):
        while (ptr < n)  and ((pussies[ptr] < events[i][0]) or ((pussies[ptr] == events[i][0]) and (events[i][1] == 1))):
            ptr += 1
        if events[i][1] == -1:
            begs[events[i][0]] = ptr
        else:
            ends[events[i][0]] = ptr

    for i in range(len(intervals)):
        print(ends[intervals[i][1]] - begs[intervals[i][0]])


def main():
    with open("input.txt", "r") as f:
        n, m = list(map(int, f.readline().split()))
        pussies = list(map(int, f.readline().split()))
        intervals = [[0, 0]] * m
        for i in range(m):
            intervals[i] = list(map(int, f.readline().split()))

        count_pussies(intervals, pussies)


if __name__ == '__main__':
    main()
