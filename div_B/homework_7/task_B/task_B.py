def max_load(events):
    ans = 0
    now = 0
    for i in range(len(events)):
        if events[i][1] == 1:
            now += 1
            if now > ans:
                ans = now
        else:
            now -= 1

    return ans


def main():
    with open("input.txt", "r") as f:
        n = int(f.readline())
        events = [0] * (2 * n)
        for i in range(n):
            t_in, l = list(map(int, f.readline().split()))
            events[2 * i] = (t_in, 1)
            events[2 * i + 1] = (t_in + l, -1)

        events = sorted(events)
        print(max_load(events))


if __name__ == '__main__':
    main()
