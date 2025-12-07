with open("Jour7/input.txt") as f:
    input = f.read().splitlines()

input_list = [list(line) for line in input]

compteur = 0
for i in range(len(input_list)):
    for j in range(len(input_list[i])):
        if input_list[i][j] == 'S':
            input_list[i+1][j] = "|"
        elif input_list[i][j] == '^' and input_list[i-1][j] == '|':
            input_list[i][j-1] = "|"
            input_list[i][j+1] = "|"
            compteur += 1
        elif input_list[i][j] == '.' and input_list[i-1][j] == '|':
            input_list[i][j] = "|"

print(compteur)