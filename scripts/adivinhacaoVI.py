# Encerrando a interação e o loop
# break sai do bloco do laço abruptamente, continue apenas pula para próxima iteração.
import random

def jogar():
        
    print("*********************************")
    print("Bem vindo ao jogo de Adivinhação!")
    print("*********************************")

    # Variaveis
    numero_secreto = random.randrange(1,101)
    total_de_tentativas = 0
    pontos = 1000

    print("Qual nível de dificuldade?", numero_secreto)
    print("(1) Fácil (2) Médio (3) Díficil")

    nivel = int(input("Define o nível: "))

    if(nivel == 1):
        total_de_tentativas = 20
    elif(nivel == 2):
        total_de_tentativas = 10
    else:
         total_de_tentativas = 5

        # Laço
    for rodada in  range(1, total_de_tentativas + 1):
            # String interpolation interpolação de strings
            print("Tentativa {} de {}".format(rodada, total_de_tentativas))

            chute_str = input("Digite o seu número entre 1 e 100: ")
            print("Você digitou " , chute_str)
            chute = int(chute_str)

            if(chute < 1 or chute > 100):
                print("Você deve digitar um número entre 1 e 100!")
                continue

            # Condições
            acertou = chute == numero_secreto
            maior = chute > numero_secreto
            menor = chute < numero_secreto

            if(acertou):
                print("Parabéns! Você acertou e fez {} pontos!".format(pontos))
                break
            else:
                if(maior):
                    print("O seu chute foi maior do que o número secreto!")
                elif(menor):
                    print("O seu chute foi menor do que o número secreto!")
            pontos_perdidos = abs(numero_secreto - chute)
            pontos = pontos - pontos_perdidos

    print("Fim do jogo")

if(__name__=="__main__"):
    jogar()



"""  
for rodada in range(1, 10):
    print(rodada)
    # print("\nOK")



for rodada1 in range(1,10,2):
    print(rodada1)


for rodada2 in [1,2,3,4,5,6,7]:
    print(rodada2)
"""
