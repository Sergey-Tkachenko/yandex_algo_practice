from operator import itemgetter

with open("input.txt", "r") as f:
    N, M = list(map(int, f.readline().split()))
    X_s = list(map(int, f.readline().split()))
    Y_s = list(map(int, f.readline().split()))

    X_to_id = []
    for i in range(N):
        X_to_id.append((X_s[i], i))

    Y_to_id = []
    for i in range(M):
        Y_to_id.append((Y_s[i], i + 1))

    X_to_id = sorted(X_to_id, key=itemgetter(0))
    Y_to_id = sorted(Y_to_id, key=itemgetter(0))

    room_ptr = 0
    ans = [0] * N
    cnt = 0

    for i in range(N):
        start = room_ptr
        for j in range(start, M):
            room_ptr += 1
            if X_to_id[i][0] + 1 <= Y_to_id[j][0]:
                ans[X_to_id[i][1]] = Y_to_id[j][1]
                cnt += 1
                break

    print(cnt)
    for i in range(N):
        print(ans[i])
