#OLacoComFor
print("*********************************")
print("Bem vindo ao jogo de Adivinhação!")
print("*********************************")

numero_secreto = 42
total_de_tentativas = 3


for rodada in  range(1, total_de_tentativas + 1):
  # String interpolation interpolação de strings
  print("Tentativa {} de {}".format(rodada, "de", total_de_tentativas))
  chute_str = input("Digite o seu número: ")
  print("Você digitou " , chute_str)
  chute = int(chute_str)

  acertou = chute == numero_secreto
  maior = chute > numero_secreto
  menor = chute < numero_secreto

  if(acertou):
      print("Parabéns! Você acertou!")
  else:
      if(maior):
          print("O seu chute foi maior do que o número secreto!")
      elif(menor):
          print("O seu chute foi menor do que o número secreto!")

print("Fim do jogo")



"""  
for rodada in range(1, 10):
    print(rodada)
    # print("\nOK")



for rodada1 in range(1,10,2):
    print(rodada1)


for rodada2 in [1,2,3,4,5,6,7]:
    print(rodada2)
"""
