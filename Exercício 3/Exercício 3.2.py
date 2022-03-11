poema = "Ai que prazer / Nao cumprir um dever, / Ter um livro para ler / E nao fazer! / Ler e macada, / Estudar e nada. / Sol doira / Sem literatura / O rio corre, bem ou mal, / Sem edicao original. / E a brisa, essa, / De tao naturalmente matinal, / Como o tempo nao tem pressa..."

# 1
print("\n-Alínea 1:")

vowel = "aeiou"
count ={'a':0, 'e':0,'i':0,'o':0,'u':0}
for i in poema :
    if i in vowel :
        if (count[i] != 0) :
            count[i] +=1
        else:
            count[i] = 1
print(count)
#ocorrencias da cada vogal;
for i in count :
    s = str(count[i])
    print(i + " : " + s)