# Encerrando a interação e o loop
# break sai do bloco do laço abruptamente, continue apenas pula para próxima iteração.
# open("palavras.txt", "w") Escreve arquivo
# open("palavras.txt", "r") Leitura de arquivo
# open("palavras.txt", "a") Adicionar conteúdo
# lowerCamelCase - a primeira palavra é escrita com todas as letras minúsculas, as palavras restantes com a primeira letra maiúscula e unidas sem espaço.
# snake_case, isto é, cada palavra é iniciada com letras minúsculas e separadas por um underscore (_).
import random

def jogar():

    imprimi_mensagem_abertura()
    palavra_secreta = carrega_palavra_secreta()
    
    letras_acertadas = inicializa_letras_acertadas(palavra_secreta)
    print(letras_acertadas)
    # letras_acertadas = ["_" for letra in palavra_secreta]

    enforcou = False
    acertou = False
    erros = 0 # Para limitar as tentativas

   

    # Enquanto(True)
    while(not enforcou and not acertou):

        chute = pode_chute()

        if(chute in palavra_secreta): # Para limitar as tentativas
            marca_chute_correto(chute, letras_acertadas, palavra_secreta)
        else: # Para limitar as tentativas
            erros += 1 # Para limitar as tentativas
            desenha_forca(erros)

        enforcou = erros == 7 # Para limitar as tentativas
        acertou = "_" not in letras_acertadas # Quando acerta todas as letras finaliza o jogo.
        print(letras_acertadas)


    if(acertou):
        imprime_mensagem_vencedor()
    else:
        imprime_mensagem_perdedor(palavra_secreta)
        

def desenha_forca(erros):
    print("  _______     ")
    print(" |/      |    ")

    if(erros == 1):
        print(" |      (_)   ")
        print(" |            ")
        print(" |            ")
        print(" |            ")

    if(erros == 2):
        print(" |      (_)   ")
        print(" |      \     ")
        print(" |            ")
        print(" |            ")

    if(erros == 3):
        print(" |      (_)   ")
        print(" |      \|    ")
        print(" |            ")
        print(" |            ")

    if(erros == 4):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |            ")
        print(" |            ")

    if(erros == 5):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |            ")

    if(erros == 6):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |      /     ")

    if (erros == 7):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |      / \   ")

    print(" |            ")
    print("_|___         ")
    print()


def imprime_mensagem_vencedor():
    print("Parabéns, você ganhou!")
    print("       ___________      ")
    print("      '._==_==_=_.'     ")
    print("      .-\\:      /-.    ")
    print("     | (|:.     |) |    ")
    print("      '-|:.     |-'     ")
    print("        \\::.    /      ")
    print("         '::. .'        ")
    print("           ) (          ")
    print("         _.' '._        ")
    print("        '-------'       ")

def imprime_mensagem_perdedor(palavra_secreta):
    print("GAME OVER!")
    print("A palavra era {}".format(palavra_secreta))
    print("    _______________         ")
    print("   /               \       ")
    print("  /                 \      ")
    print("/\/                  \/\  ")
    print("\ |  XXXX     XXXX   | /   ")
    print(" \|  XXXX     XXXX   |/     ")
    print("  |  XXX       XXX   |      ")
    print("  |                  |      ")
    print("  \__     XXX      _/     ")
    print("   |\     XXX     /|       ")
    print("   | |           | |        ")
    print("   | I I I I I I I |        ")
    print("   |  I I I I I I  |        ")
    print("   \_             _/       ")
    print("     \_         _/         ")
    print("       \_______/           ")


def marca_chute_correto(chute, letras_acertadas, palavra_secreta):
    index = 0
    for letra in palavra_secreta:
            if(chute == letra):
                letras_acertadas[index] = letra
            index += 1


def pode_chute():
    chute = input("Qual letra? ")
    chute = chute.strip().upper() # .strip() - Para retirar espaços
    return chute


def inicializa_letras_acertadas(palavra):
    return ["_" for letra in palavra]


def imprimi_mensagem_abertura():
    print("*********************************")
    print("Bem vindo ao jogo de Forca!")
    print("*********************************")


def carrega_palavra_secreta():
    arquivo = open("palavras.txt", "r")
    palavras = []

    for linha in arquivo:
        linha = linha.strip()
        palavras.append(linha)

    arquivo.close()

    numero = random.randrange(0,len(palavras))
    palavra_secreta = palavras[numero].upper()
    return palavra_secreta


if(__name__=="__main__"):
    jogar()
