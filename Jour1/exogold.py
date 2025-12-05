#NON FINI !

with open("Jour1/input.txt", 'r') as f:
    lignes = f.readlines()

dial = 50
c = 0
max = 0

for ligne in lignes:
    if len(ligne) > max:
        max = len(ligne)
    print(ligne)
    if ligne[0] == "L":
        if len(ligne) == 2:
            if (dial - ligne[1]) < 0:
                c += 1
            dial = (dial - int(str(0)+str(ligne[1])))%100
            if dial == 0:
                c += 1
        elif len(ligne) == 3:
            if (dial - int(str(ligne[1])+str(ligne[2]))) < 0:
                c += 1
            dial = (dial - int(str(ligne[1])+str(ligne[2])))%100
            if dial == 0:
                c += 1
        elif len(ligne) == 4:
            print(int(str(ligne[1])+str(ligne[2])+str(ligne[3])) - dial)
            print("bladjefjiejgrejgrjig")
            if (int(str(ligne[1])+str(ligne[2])+str(ligne[3])) - dial) >= 100:
                nvD = int(str(ligne[1])+str(ligne[2])+str(ligne[3])) - dial
                print(f"nvd = {nvD}")
                c += nvD[0]
            elif dial != 0:
                c+=1
            dial = (dial - int(str(ligne[1])+str(ligne[2])+str(ligne[3])))%100
            if dial == 0:
                c += 1
        else:
            if (int(str(ligne[1])+str(ligne[2])+str(ligne[3])+str(ligne[4])) - dial) >= 1000:
                nvD = int(str(ligne[1])+str(ligne[2])+str(ligne[3])+str(ligne[4])) - dial
                c += nvD[0]
            dial = (dial - int(str(ligne[1])+str(ligne[2])+str(ligne[3])+str(ligne[4])))%100
            if dial == 0:
                c += 1
    else:
        if len(ligne) == 2:
            if dial + ligne[1] > 100:
                c += 1
            dial = (dial + int(str(0)+str(ligne[1])))%100
            if dial == 0:
                c += 1
        elif len(ligne) == 3:
            if (dial + int(str(ligne[1])+str(ligne[2]))) > 100:
                c += 1
            dial = (dial + int(str(ligne[1])+str(ligne[2])))%100
            if dial == 0:
                c += 1
        elif len(ligne) == 4:
            dial = (dial + int(str(ligne[1])+str(ligne[2])+str(ligne[3])))%100
            if dial == 0:
                c += 1
        else:
            dial = (dial + int(str(ligne[1])+str(ligne[2])+str(ligne[3])+str(ligne[4])))%100
            if dial == 0:
                c += 1
    print(dial)

print(f"C = {c}")
print(f"Max = {max}")

print(len("L537"))