with open("input.txt", 'r') as f:
    lignes = f.read().splitlines()

dial = 50
c = 0

for ligne in lignes:    
    dir = ligne[0]
    dist = int(ligne[1:])
    if dir == "L":
        if dial == 0:
            nb = dist // 100
        elif dist >= dial:
            nb = 1 + (dist - dial) // 100
        else:
            nb = 0
        dial = (dial - dist) % 100
    else:
        if dial + dist >= 100:
            nb = 1 + (dial + dist - 100) // 100
        else:
            nb = 0
        dial = (dial + dist) % 100
    print(ligne + ' ' + str(nb))
    print('dial ' + str(dial))
    c += nb

print(f"C = {c}")