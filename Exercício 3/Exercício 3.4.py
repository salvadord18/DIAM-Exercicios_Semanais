# 1)
def functionname(string1, string2) :
    arr1 = list(string1)
    arr2 = list(string2)
    for i in arr1:
        for j in arr2:
            if i == j:
                arr2 = s.replace(j, "None")
    for a in arr2:
        if a != "None"7:
            print("As palavras não são transponíveis")


functionname("olá", "adeus")

# 2)
def sortString(string1, string2):
    string1 = sorted(string1)
    string2 = sorted(string2)
    if string1 == string2:
        print("As palavras são transponíveis")

sortString("olá", "olá")

#3)

# 4)
def (string1, string2):
    vowel = "aeiou"
    count1 = {'a': 0, 'e': 0, 'i': 0, 'o': 0, 'u': 0}
    count2 = {'a': 0, 'e': 0, 'i': 0, 'o': 0, 'u': 0}
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


