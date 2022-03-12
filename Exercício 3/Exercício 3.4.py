# 1)
def functionname(string1, string2) :
    arr1 = list(string1)
    arr2 = list(string2)
    for i in arr1:
        for j in arr2:
            if i == j:
                arr2 = s.replace(j, "None")
    for a in arr2:
        if a != "None":
            print("Não é possível")

functionname("olá","adeus")

# 2)
def sortString(string1, string2):
    string1 = sorted(string1)
    string2 = sorted(string2)
    if string1 == string2:
        print("É possível")

sortString("olá","olá")

#3)
