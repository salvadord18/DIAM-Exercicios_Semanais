# 1)
def functionname(string1, string2) :
    b = False
    for i in string1:
        for j in string2:
            if i == j:
                string2 = string2.replace(j, None)
    for a in string2:
        if a != None:
            print("Não é possível")

# 2)
def sortString(string1, string2):
    string1 = sorted(string1)
    string2 = sorted(string2)
    if string1 == string2:
        print("É possível")

#3)
