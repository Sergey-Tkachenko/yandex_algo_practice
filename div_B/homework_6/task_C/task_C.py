def find_borders(coefs):
    abs_sum = 0
    for i in range(len(coefs)):
        abs_sum += abs(coefs[i])

    return -abs_sum - 1, abs_sum + 1


def dihotomy(f, a, b, args, tol):
    l = a
    r = b
    x_prev = (l + r) / 2 + 10 * tol
    x_now = (l + r) / 2

    while abs(x_now - x_prev) > tol:
        x_prev = x_now

        f_now = f(x_now, args)
        if f_now > 0:
            r = x_now
        else:
            l = x_now

        x_now = (l + r) / 2

    return x_now


def polynom(x, coefs):
    n = len(coefs)
    ans = 0
    for i in range(n - 1, -1, -1):
        ans += coefs[n - i - 1] * x ** i

    return ans


def main():
    with open("input.txt", "r") as f:
        coefs = list(map(int, f.readline().split()))

        # normalize coeffs
        if coefs[0] < 0:
            for i in range(4):
                coefs[i] *= -1

        a, b = find_borders(coefs)
        sol = dihotomy(polynom, a, b, coefs, tol=1e-8)
        print(sol)


if __name__ == '__main__':
    main()

