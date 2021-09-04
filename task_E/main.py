d = int(input())
x, y = list(map(int, input().split()))

if (0 <= x <= d) and (0 <= y <= d) and (y <= d - x):
    print(0)
else:
    d_A = x ** 2 + y ** 2
    d_B = (x - d) ** 2 + y ** 2
    d_C = x ** 2 + (y - d) ** 2

    if (d_A <= d_B) and (d_A <= d_C):
        print(1)
    elif (d_B <= d_A) and (d_B <= d_C):
        print(2)
    else:
        print(3)