chaine = '69810572-69955342,3434061167-3434167492,76756725-76781020,49-147,296131-386620,910523-946587,34308309-34358652,64542-127485,640436-659023,25-45,35313993-35393518,753722181-753795479,1544-9792,256-647,444628-483065,5863911-6054673,6969623908-6969778569,658-1220,12631-63767,670238-830345,1-18,214165106-214245544,3309229-3355697'

pl = chaine.split(",")

plsplit = []

res = 0
l_res = []

for elt in pl:
    plsplit.append(elt.split("-"))

i = 0

for elt in plsplit:

    for i in range(int(elt[0]), int(elt[1])): 
        ch = str(i)
        for i in range(1, len(ch) // 2 + 1):
            if ch in l_res:
                break
            if len(ch) % i == 0:
                n = len(ch) // i
                if i == 1:
                    n = 1
                parts = [ch[i:i+n] for i in range(0, len(ch), n)]
                flag = True
                for elt in parts:
                    if elt != parts[0]:
                        flag = False
                if flag and len(parts) != 0:
                    res += int(ch)
                    l_res.append(ch)
i += 1

print(res)
