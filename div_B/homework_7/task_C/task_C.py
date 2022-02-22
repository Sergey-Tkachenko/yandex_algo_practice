def find_cover(intervals, m):
    cand = []
    max_right = 0
    max_right_cand = [0, 0]
    intervals = sorted(intervals)
    for i in range(len(intervals)):
        if intervals[i][0] > max_right:
            max_right = max_right_cand[1]
            cand.append(max_right_cand)
        if (intervals[i][0] <= max_right) and (intervals[i][1] > max_right_cand[1]):
            max_right_cand = intervals[i]

    cand.append(max_right_cand)
    if cand[-1][1] < m:
        print("No solution")
    else:
        cnt = 0
        while cand[cnt][1] < m:
            cnt += 1
        print(cnt + 1)

        for i in range(cnt + 1):
            print(*cand[i])


def main():
    with open("input.txt", "r") as f:
        m = int(f.readline())
        lines = f.readlines()

        intervals = [[0, 0]] * (len(lines) - 1)
        for i in range(len(lines) - 1):
            intervals[i] = list(map(int, lines[i].split()))

        find_cover(intervals, m)


if __name__ == '__main__':
    main()




