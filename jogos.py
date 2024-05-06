# Encerrando a interação e o loop
# break sai do bloco do laço abruptamente, continue apenas pula para próxima iteração.
import forca
import adivinhacaoVI
import speech_recognition as sr
import datetime

def greet():
    hour = datetime.datetime.now().hour
    if hour >= 0 and hour < 12:
        return "Bom dia!"
    elif hour >= 12 and hour < 18:
        return "Boa tarde!"
    else:
        return "Boa noite!"

# print(greet())
voz = (greet())

 # para obter o dia da semana atual em português
from datetime import datetime
import pyttsx3

dias = {0: "Segunda-feira", 1: "Terça-feira", 2: "Quarta-feira", 3: "Quinta-feira", 4: "Sexta-feira", 5: "Sábado", 6: "Domingo"}

dia_semana = datetime.now().weekday()

    
# Ler os dados e repoduz


    

def ler_data_hora():
    agora = datetime.now()
    dia_da_semana = agora.strftime("%A")
    data = agora.strftime("%d/%m/%Y")
    hora = agora.strftime("%H:%M:%S")
    mensagem = f"Olá!!! Meu nome é Tatá. {voz}. Estimo que esteja tudo bem contigo, e a sua família. Hoje é {dias[dia_semana]}, {data}, e são {hora} horas. Irei exibir o menu para escolher o jogo."
    engine = pyttsx3.init()
    engine.say(mensagem)
    engine.runAndWait()
    
ler_data_hora()

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


