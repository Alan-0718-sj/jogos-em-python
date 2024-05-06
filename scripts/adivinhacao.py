"""
print(*args, sep=' ', end='\n', file=None, flush=False)
    Prints the values to a stream, or to sys.stdout by default.

    sep
      string inserted between values, default a space.
    end
      string appended after the last value, default a newline.
    file
      a file-like object (stream); defaults to the current sys.stdout.
    flush
      whether to forcibly flush the stream.

"""


# print("*********************************")
# print("Bem vindo no jogo de Adivinhação!")
# print("*********************************")

# numero_secreto = 42

# chute_str = input("Digite o seu número: ")

# print("Você digitou", chute_str)

# chute = int(chute_str)

# acertou = chute == numero_secreto
# maior =   chute > numero_secreto
# menor =   chute < numero_secreto

# if (acertou):
#     print("Você acertou")
# else:
#     if(maior):
#         print("Você errou!! O seu chute foi maior do que o número secreto.")
#     elif(menor):
#         print("Você errou!! O seu chute foi menor do que o número secreto.")

# print("Fim do jogo")


print("*********************************")
print("Bem vindo ao jogo de Adivinhação!")
print("*********************************")

numero_secreto = 42
total_de_tentativas = 3
rodada = 1

while(rodada <= total_de_tentativas > 0):
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

  rodada = rodada + 1

print("Fim do jogo")

