from itertools import combinations_with_replacement
# 1)
def functionname(string1, string2) :
    arr1 = list(string1)
    arr2 = list(string2)
    for i in arr1:
        for j in arr2:
            if i == j:
                arr2 = s.replace(j, None)
    for a in arr2:
        if a != None:
            print("As palavras não são transponíveis")


functionname("olá", "adeus")

# 2)
def sortString(string1, string2):
    string1 = sorted(string1)
    string2 = sorted(string2)
    if string1 == string2:
        print("As palavras são transponíveis")

sortString("olá", "olá")

# 3)
def testAllPoss(string1, string2, x):
    max_length = x
    for r in range(max_length, max_length+1):
        for combo in combinations_with_replacement(string1, r=r):
            lista_combinacoes = [''.join(combo)]
            print(lista_combinacoes)

    if string2 in lista_combinacoes:
        print("A segunda string encontra-se na lista")
    else:
        print("A segunda string não se encontra na lista")

# 4)
def countletters(string1, string2):
    vowel = "abcdefghijklmnaopqrstuvwsyz"
    count1 = {'a': 0, 'b': 0, 'c': 0, 'd': 0, 'e': 0, 'f': 0, 'g': 0, 'h': 0, 'i': 0, 'j': 0, 'k': 0, 'l': 0, 'm': 0, 'n': 0, 'o': 0, 'p': 0, 'q': 0, 'r': 0, 's': 0, 't': 0, 'u': 0, 'v': 0, 'w': 0, 'x': 0, 'y': 0, 'z': 0}
    count2 = {'a': 0, 'b': 0, 'c': 0, 'd': 0, 'e': 0, 'f': 0, 'g': 0, 'h': 0, 'i': 0, 'j': 0, 'k': 0, 'l': 0, 'm': 0, 'n': 0, 'o': 0, 'p': 0, 'q': 0, 'r': 0, 's': 0, 't': 0, 'u': 0, 'v': 0, 'w': 0, 'x': 0, 'y': 0, 'z': 0}
    for i in string1:
        if i in vowel:
            if (count1[i] != 0):
                count1[i] += 1
            else:
                count1[i] = 1
    for i in string2:
        if i in vowel:
            if (count2[i] != 0):
                count2[i] += 1
            else:
                count2[i] = 1
    for l in count1:
        for f in count2:
            if count1[l] != count2[f]:
                print("As palavras não são transponíveis")


