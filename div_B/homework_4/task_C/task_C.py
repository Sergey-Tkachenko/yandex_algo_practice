from operator import itemgetter, attrgetter

with open("input.txt", "r") as f:
    lines = f.readlines()


d = {}

for line in lines:
    words = line.split()
    for i in range(len(words)):
        if words[i] not in d.keys():
            d[words[i]] = 0
        d[words[i]] += 1

items = list(d.items())

items = sorted(items, key=itemgetter(0))
items = sorted(items, key=itemgetter(1), reverse=True)

for name, _ in items:
    print(name)



