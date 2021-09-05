x, y, z = list(map(int, input().split()))

if (x > 12) or (y > 12):
    print(1)
else:
    if x == y:
        print(1)
    else:
        print(0)