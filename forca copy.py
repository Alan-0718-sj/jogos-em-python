# Encerrando a interação e o loop
# break sai do bloco do laço abruptamente, continue apenas pula para próxima iteração.
# open("palavras.txt", "w") Escreve arquivo
# open("palavras.txt", "r") Leitura de arquivo
# open("palavras.txt", "a") Adicionar conteúdo
import random

def jogar():
    print("*********************************")
    print("Bem vindo ao jogo de Forca******!")
    print("*********************************")


    arquivo = open("palavras.txt", "r")
    palavras = []

    for linha in arquivo:
        linha = linha.strip()
        palavras.append(linha)

    arquivo.close()

    numero = random.randrange(0,len(palavras))
    palavra_secreta = palavras[numero]

    palavra_secreta = "maça".upper() # .upper() - Para deixar todas asletras maiusculas
    letras_acertadas = ["_" for letra in palavra_secreta]

    enforcou = False
    acertou = False
    erros = 0 # Para limitar as tentativas

    print(letras_acertadas)

    # Enquanto(True)
    while(not enforcou and not acertou):

        chute = input("Qual letra? ")
        chute = chute.strip().upper() # .strip() - Para retirar espaços

        if(chute in palavra_secreta): # Para limitar as tentativas
            index = 0
            for letra in palavra_secreta:
                if(chute == letra):
                    letras_acertadas[index] = letra
                index += 1
        else: # Para limitar as tentativas
            erros += 1 # Para limitar as tentativas

        enforcou = erros == 6 # Para limitar as tentativas
        acertou = "_" not in letras_acertadas # Quando acerta todas as letras finaliza o jogo.
        print(letras_acertadas)


    if(acertou):
        print("Você ganhou!!!")
    else:
        print("Você perdeu!!!")
    print("Fim do jogo")

if(__name__=="__main__"):
    jogar()

