N, i, j = list(map(int, input().split()))

print(min(abs(i - j), N - abs(i - j)) - 1)