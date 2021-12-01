xNome = input("Digite o nome do Aluno: ")
i = 1
xSoma = 0
while (i <= 3):
  xNota = float(input("Digite a nota {0} do(a) aluno(a): ".format(i)))
  xSoma = xSoma + xNota
  i = i + 1
pass 
xMedia = xSoma/3
if (xMedia >= 10):
  print("Média das notas do aluno {0} é {1}. Aluno(a) aprovado(a)!".format(xNome, xMedia))
else: 
  print("Média das notas do aluno {0} é {1}. Aluno(a) reprovado(a)!".format(xNome, xMedia))


 
