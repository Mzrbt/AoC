with open("Jour1/input.txt", 'r') as f:
    lignes = f.read().splitlines()

dial = 50
c = 0

for ligne in lignes:    
    dir = ligne[0]
    dist = int(ligne[1:])
    
    if dir == "L":
        if dist >= dial:
            nb = 1 + (dist - dial) // 100
        else:
            nb = 0
        dial = (dial - dist) % 100
    else:  # R
        nb = (dial + dist) // 100
        dial = (dial + dist) % 100
    
    c += nb

print(f"C = {c}")