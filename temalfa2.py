f = open("input", "r")

nr_noduri = int(f.readline())

noduri = []

for i in f.readline().split():
    noduri.append(i)
print("noduri ")
print(noduri)
valori = []
for i in f.readline().split():
    valori.append(i)
print("valori ")
print(valori)

nod_initial = f.readline()

noduri_nefinale = []
for i in f.readline().split():
    noduri_nefinale.append(i)

nod_final = []
for i in f.readline().split():
    nod_final.append(i)
print('noduri nefinale')
print(noduri_nefinale)
print('noduri finale')
print(nod_final)
print('\n')
automat = dict()
for i in noduri:
    automat.update({i: []})
for i in f.readlines():
    i = i.split()
    automat.setdefault(i[0], []).append((i[1], i[2]))
print('automat')

print(automat)

equivalence = []
old_equivalence = []
equivalence.append(noduri_nefinale)
equivalence.append(nod_final)
print('lista de echivalenta initiala')
print(equivalence)


def testare(a, b):
    global old_equivalence
    ok = 0
    if a == b:
        return 1
    for i in old_equivalence:
        if a in i and b in i:
            ok = 1
            break
    return ok


while equivalence != old_equivalence:
    old_equivalence = equivalence.copy()
    equivalence.clear()
    for i in old_equivalence:
        equivalence.append([i[0]])
        for j in range(1, len(i)):
            ok = 0
            y = 0
            for y in range(len(equivalence)):
                p = 0
                while p < len(automat[i[j]]):
                    ok = 0
                    if testare(automat[i[j]][p][0], automat[equivalence[y][0]][p][0]) == 1:
                        ok = 1
                    else:
                        ok = 0
                        break
                    p += 1
                if ok == 1:
                    equivalence[y].append(i[j])
                    break
            if ok == 0:
                equivalence.append([i[j]])

    print(equivalence)

print('lista de echivalenta finala')
print(old_equivalence)
automat_minimal = dict()
for i in old_equivalence:
    for j in automat[i[0]]:
        p = 0
        while p < (len(old_equivalence)):
            if j[0] in old_equivalence[p]:
                automat_minimal.setdefault(','.join(i), []).append((old_equivalence[p], j[1]))
                p = len(old_equivalence)
            else:
                p += 1
print(automat_minimal)
