n = int(input())
candidates = set(map(str, range(1, n + 1)))

inp = input()

while inp != "HELP":
    seq = inp.split()
    inp = input()
    if inp == "YES":
        seq = set(seq)
        candidates = candidates.intersection(seq)
    else:
        for i in range(len(seq)):
            if seq[i] in candidates:
                candidates.remove(seq[i])
    inp = input()

print(" ".join(sorted(candidates)))
