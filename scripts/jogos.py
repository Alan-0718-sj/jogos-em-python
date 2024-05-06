# Encerrando a interação e o loop
# break sai do bloco do laço abruptamente, continue apenas pula para próxima iteração.
import forca
import adivinhacaoVI

def escolha_jogo():

    print("*********************************")
    print("******Escolha o seu jogo!********")
    print("*********************************")


    print("(1) Forca (2) Adivinhação")

    jogo = int(input("Qual jogo? "))

    if(jogo == 1):
        print("jogando forca")
        forca.jogar()
    elif(jogo == 2):
        print("Jogando adivinhação")
        adivinhacaoVI.jogar()

if(__name__=="__main__"):
    escolha_jogo()


