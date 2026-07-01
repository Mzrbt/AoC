with open("input.txt") as f:
    input = f.readlines()

res=0

for elt in input:
    ind = 0
    ind_prec = 0
    nb = ''
    for i in range(12):
        print(f'ind: {ind}')
        maxi = elt[ind]
        print(list(elt[ind:len(elt)-11+i]))
        print(f'indice: {ind}, fin: {len(elt)-12+i}')
        for index, digit in enumerate(list(elt[ind:len(elt)-12+i])):
            if nb != '':
                if len(elt[ind:]) == 12 - int(nb):
                    nb += digit
                    break
            if digit > maxi:
                maxi = digit
                ind = index + ind_prec
        ind += 1
        ind_prec = ind
        nb += maxi
    res += int(nb)
print(res)