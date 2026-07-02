with open("input.txt") as f:
    input = f.readlines()

input[-1] += '.'
c1 = ''
for i in range(len(input[0])):
    c1 += '.'

input.insert(0, c1)
input.insert(len(input), c1)

for i in range(len(input)):
    input[i] += '.'
    input[i] = '.' + input[i]

rres = 0
res = 1
while(res > 0):
    res = 0
    for i in range(len(input)-2):
        for j in range(len(input[0])-3):
            if input[i+1][j+1] == '@':
                nb = 0
                if input[i][j] == '@' or input[i][j] == 'x': nb += 1
                if input[i][j+1] == '@' or input[i][j+1] == 'x': nb += 1
                if input[i][j+2] == '@' or input[i][j+2] == 'x': nb += 1
                if input[i+1][j] == '@' or input[i+1][j] == 'x': nb += 1
                if input[i+1][j+2] == '@' or input[i+1][j+2] == 'x': nb += 1
                if input[i+2][j] == '@' or input[i+2][j] == 'x': nb += 1
                if input[i+2][j+1] == '@' or input[i+2][j+1] == 'x': nb += 1
                if input[i+2][j+2] == '@' or input[i+2][j+2] == 'x': nb += 1
                if nb < 4:
                    res += 1
                    input[i+1] = input[i+1][:j+1] + 'x' + input[i+1][j+2:]
    input = [line.replace('x', '.') for line in input]
    rres += res
print(rres)
