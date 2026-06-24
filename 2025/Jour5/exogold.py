with open("Jour5/input.txt") as f:
    input = f.read().splitlines()

plages = []

for elt in input:
    plages.append(elt.split('-'))

print(plages)

tab = []

compteur = 0

j = 0
for elt in plages:
    print(f"Test de la plage {compteur} sur {len(plages)}")
    for i in range(int(elt[1]) - int(elt[0]) + 2):
        if int(elt[0]) + j <= int(elt[1]) and (int(elt[0]) + j) not in tab:
            tab.append(int(elt[0]) + j)
            j += 1
        elif int(elt[0]) + j > int(elt[1]):
            j = 0
            break
        else:
            j += 1

print(len(tab))