with open("Jour4/input.txt") as f:
    input = f.readlines()

for j in range(len(input)-1):
    com = 0
    for i in range(len(input[j])-1):
        compteur = 0
        if com == 0:
            if i == 0:
                pass
            elif i == len(input[j])-1:
                pass
            else:
                if input[j][i-1] == '@':
                    compteur += 1
                if input[j][i+1] == '@':
                    compteur += 1
                if input[j+1][i-1] == '@':
                    compteur += 1
                if input[j+1][i] == '@':
                    compteur += 1
                if input[j+1][i+1] == '@':
                    compteur += 1
        elif com == len(input)-1:
            if i == 0:
                pass
            elif i == len(input[j])-1:
                pass
            else:
                if input[j][i-1] == '@':
                    compteur += 1
                if input[j][i+1] == '@':
                    compteur += 1
                if input[j-1][i-1] == '@':
                    compteur += 1
                if input[j-1][i] == '@':
                    compteur += 1
                if input[j-1][i+1] == '@':
                    compteur += 1
        else:
            if i == 0:
                if input[j-1][i] == '@':
                    compteur += 1
                if input[j-1][i+1] == '@':
                    compteur += 1
                if input[j][i+1] == '@':
                    compteur += 1
                if input[j+1][i] == '@':
                    compteur += 1
                if input[j+1][i+1] == '@':
                    compteur += 1
            elif i == len(input[j])-1:
                if input[j-1][i] == '@':
                    compteur += 1
                if input[j-1][i-1] == '@':
                    compteur += 1
                if input[j][i-1] == '@':
                    compteur += 1
                if input[j+1][i] == '@':
                    compteur += 1
                if input[j+1][i-1] == '@':
                    compteur += 1
            else:
                if input[j-1][i] == '@':
                    compteur += 1
                if input[j-1][i-1] == '@':
                    compteur += 1
                if input[j-1][i+1] == '@':
                    compteur += 1
                if input[j][i-1] == '@':
                    compteur += 1
                if input[j][i] == '@':
                    compteur += 1
                if input[j][i+1] == '@':
                    compteur += 1
                if input[j+1][i] == '@':
                    compteur += 1
                if input[j+1][i-1] == '@':
                    compteur += 1
                if input[j+1][i+1] == '@':
                    compteur += 1
    if (compteur > 3):
        input[j][i] = 'x'
    com+=1

print(input)