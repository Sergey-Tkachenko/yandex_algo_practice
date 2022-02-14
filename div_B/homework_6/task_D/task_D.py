def count_trees(n, a, b, k, m):
    return n * (a + b) - n // k * a - n // m * b


def left_bs(x, l_0, r_0, f, args):
    l = l_0
    r = r_0
    while l < r:
        m = l + (r - l) // 2
        if f(m, *args) >= x:
            r = m
        else:
            l = m + 1

    return l


def main():
    with open("input.txt", "r") as f:
        a, k, b, m, x = list(map(int, f.readline().split()))
        out = left_bs(x, 1, 2 * x, count_trees, [a, b, k, m])
        print(out)


main()
