# 1)
lista = [54, 26, 93, 17, 77, 31, 44, 55, 20]
for i in range(len(lista)-1,0,-1):
    for l in range(i):
        if lista[l] > lista[l+1]:
            aux = lista[l]
            lista[l] = lista[l+1]
            lista[l + 1] = aux
print(lista)