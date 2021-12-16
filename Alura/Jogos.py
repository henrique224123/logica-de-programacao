import forca
import adivinhacao

print("======================================")
print("==========Escolha o seu jogo==========")
print("======================================")

print("(1) Forca (2) Adivinhação")

jogo = int(input("Faça sua escolha: "))

if(jogo == 1):
    print("Jogo Escolhiido: Forca")
    forca.Jogo2()
elif(jogo == 2):
    print("Jogo Escolhido: Adivinhação")
    adivinhacao.Jogo1()