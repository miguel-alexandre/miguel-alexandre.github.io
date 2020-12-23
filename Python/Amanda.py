import os
#coding utf-8
#Projeto de inteligência artifícial de combate à depressão.
#Desenvolvido em 2020 por Miguel Alexandre.
#versão 1.0.0
os.system("cvlc Welcome.mp3 --play-and-exit")
os.system("clear")
print ("Amanda IA 1.0.0 Project")
print ("Olá, Miguel, Bem vindo. O que deseja?")
comando = str(input("Insira o comando: "))

if comando=='Conversar':
     os.system("python3 chat.py")
elif comando=='Musica':
    print("Qual música deseja escutar? ")
    musica = str(input("Insira o nome da música: "))
    if musica=='Bad Apple':
        os.system("cvlc Maca_ruim.mp3 --play-and-exit")
    if musica=='Voracity':
         os.system("cvlc Voracity.mp3 --play-and-exit")
elif comando=='Filme':
    print("Qual filme gostaria de assistir? ")
    filme = str(input("Insira o nome do filme: "))