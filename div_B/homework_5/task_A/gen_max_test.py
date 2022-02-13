n = q = 3 * 10 ** 5

with open("input_5.txt", "w") as f:
    f.write(f"{n} {q}\n")
    max_arr = [1000000000] * n
    f.write(" ".join(map(str, max_arr)))
    f.write("\n")

    for i in range(q):
        f.write(f"1 {n}\n")

    f.write("\n")


