#entrada de variáveis e dados
nota1 = float(input("Informe a sua 1ª nota: "))
nota2 = float(input("Informe a sua 2ª nota: "))
nota3 = float(input("Informe a sua 3ª nota: "))
              
 #processamento de dados
media = (nota1 + nota2 + nota3) / 3

#saída de dados
print("A média das suas notas é de ", media) 

if media >= 7:
  print("Aluno aprovado!")
else:
  print("Aluno reprovado!")
