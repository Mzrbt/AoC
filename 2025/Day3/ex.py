with open("input.txt") as f:
    input = f.readlines()

res=0
for elt in input:
    imax1 = 0
    max1 = 0
    max2 = 0
    for i in range(len(elt)-1):
        if int(elt[i]) > max1 and i < (len(elt)-2):
            max1 = int(elt[i])
            imax1 = i
    for j in range(len(elt)-1):
        if int(elt[j]) > max2 and j != imax1 and j > imax1:
            max2 = int(elt[j])
    res += int(''.join([str(max1),str(max2)]))
print(res)