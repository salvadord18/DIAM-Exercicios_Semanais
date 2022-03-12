# 1.
lista = [54, 26, 93, 17, 77, 31, 44, 55, 20]
aux = 0
for l in lista:
    if lista[l] > lista[l+1]:
        aux = lista[l]
        lista[l] = lista[l+1]
        lista[l + 1] = aux
print(str(lista))