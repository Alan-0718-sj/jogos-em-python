# Encerrando a interação e o loop
# break sai do bloco do laço abruptamente, continue apenas pula para próxima iteração.
import random

print("*********************************")
print("Bem vindo ao jogo de Adivinhação!")
print("*********************************")

numero_secreto = random.randrange(1,101)
total_de_tentativas = 3

# print("Qual nível de dificuldade?")
# print("(1) Fácil (2) Médio (3) Díficil")

# nivel = int(input("Define o nível: "))

# if(nivel == 1):
#     total_de_tentativas = 20
# elif(nivel == 2):
#     total_de_tentativas = 10
# else:
#     total_de_tentativas = 5

for rodada in  range(1, total_de_tentativas + 1):
  # String interpolation interpolação de strings
  print("Tentativa {} de {}".format(rodada, total_de_tentativas))
  chute_str = input("Digite o seu número entre 1 e 100: ")
  print("Você digitou " , chute_str)
  chute = int(chute_str)

  if(chute < 1 or chute > 100):
      print("Você deve digitar um número entre 1 e 100!")
      continue

  acertou = chute == numero_secreto
  maior = chute > numero_secreto
  menor = chute < numero_secreto

  if(acertou):
      print("Parabéns! Você acertou!")
      break
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
