poema = "Ai que prazer / Nao cumprir um dever, / Ter um livro para ler / E nao fazer! / Ler e macada, / Estudar e nada. / Sol doira / Sem literatura / O rio corre, bem ou mal, / Sem edicao original. / E a brisa, essa, / De tao naturalmente matinal, / Como o tempo nao tem pressa..."

# 1
print("\n-Alínea 1:")

# conta o número de vogais existentes no texto;
vowel = "aeiou"
count ={'a':0, 'e':0,'i':0,'o':0,'u':0}
for i in poema :
    if i in vowel :
        if (count[i] != 0) :
            count[i] +=1
        else:
            count[i] = 1
print(count)

# imprime na consola as ocorrências da cada vogal;
for i in count:
    s = str(count[i])
    print(i + " : " + s)

#  identifica a vogal mais utilizada;
vogal_mais_usada = 0
for i in count:
    if count[i] > vogal_mais_usada:
        vogal_mais_usada = count[i]

# imprime na consola a vogal mais utilizada;
for i in count:
    if count[i] == vogal_mais_usada:
        print("vogal mais utilizada: " + i)

# várias vogais empatadas com o maior número de ocorrências
num_ocorrencias = 0
for i in count:
    if count[i] == vogal_mais_usada:
        num_ocorrencias += 1
if num_ocorrencias > 1:
    print("Há vários vencedores.")
else:
    print("Há apenas um vencedor.")


