poema = "Ai que prazer / Nao cumprir um dever, / Ter um livro para ler / E nao fazer! / Ler e macada, / Estudar e nada. / Sol doira / Sem literatura / O rio corre, bem ou mal, / Sem edicao original. / E a brisa, essa, / De tao naturalmente matinal, / Como o tempo nao tem pressa..."

# 1)
print("\n-Alínea 1:")

print(poema.split("/")[4:6])

# 2)
print("\n-Alínea 2:")

poema_formatado = poema.replace(" / ", "\n")
print(poema_formatado)

# 3)
print("\n-Alínea 3:")

fim_do_poema = "\nLivros sao papeis pintados com tinta. \nEstudar e uma coisa em que esta indistinta \nA distincao entre nada e coisa nenhuma."
print(poema_formatado + fim_do_poema)

# 4)
print("\n-Alínea 4:")

poema_completo = poema_formatado + fim_do_poema

print(poema_completo.split("\n")[-2])
print(poema_completo.split("\n")[-1])