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

res = 0
for i in range(len(input)-2):
    for j in range(len(input[0])-3):
        if input[i+1][j+1] == '@':
            nb = 0
            if input[i][j] == '@': nb += 1
            if input[i][j+1] == '@': nb += 1
            if input[i][j+2] == '@': nb += 1
            if input[i+1][j] == '@': nb += 1
            if input[i+1][j+2] == '@': nb += 1
            if input[i+2][j] == '@': nb += 1
            if input[i+2][j+1] == '@': nb += 1
            if input[i+2][j+2] == '@': nb += 1
            if nb < 4:
                res += 1
print(res)
