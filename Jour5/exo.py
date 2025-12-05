with open("Jour5/input.txt") as f, open("Jour5/inputval.txt") as v:
    input = f.read().splitlines()
    val = v.read().splitlines()

plages = []

for elt in input:
    plages.append(elt.split('-'))

c=0
for v in val:
    for i in range(len(plages)):
        if int(plages[i][0]) <= int(v) <= int(plages[i][1]):
            c += 1
            break

print(c)