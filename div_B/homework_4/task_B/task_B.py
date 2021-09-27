cand = {}
names = set()

with open("input.txt", 'r') as f:
    lines = f.readlines()

for i in range(len(lines)):
    name, cnt = lines[i].split()
    cnt = int(cnt)

    if name not in names:
        names.add(name)
        cand[name] = 0
    cand[name] += cnt
    
for name in sorted(names):
    print(name, cand[name])
