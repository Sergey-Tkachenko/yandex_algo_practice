from operator import itemgetter

K = 450
with open("input.txt", "r") as f:
    seq = f.readlines()

in_parties = {}
in_sigma = 0

for s in seq:
    split = s.split()
    name = ' '.join(split[:-1])
    cnt = int(split[-1])

    if name not in in_parties.keys():
        in_parties[name] = 0

    in_parties[name] += cnt
    in_sigma += cnt


def fill_missing(mods, res, sigma_places):
    mods = sorted(mods, key=itemgetter(1), reverse=True)
    mods = sorted(mods, key=itemgetter(2), reverse=True)

    for i in range(K - sigma_places):
        res[mods[i][0]] += 1

    return res


def count_places(parties, sigma):
    res = {}
    mods = []
    sigma_places = 0

    for name in parties.keys():
        res[name] = parties[name] * K // sigma
        sigma_places += res[name]
        mods.append((name, parties[name], parties[name] * K % sigma))

    return fill_missing(mods, res, sigma_places)


for k, v in count_places(in_parties, in_sigma).items():
    print(k, v)
