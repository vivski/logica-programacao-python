# Escreva um programa que simule um jogo 
# de adivinhação. O programa deve gerar um número
# aleatório entre 1 e 40 e permitir que
# o usuário tente adivinhar o número com o máximo de 5 chutes.
import random;
sorteio = random.randint(1,40)
tentativas = 5

for tentativa in range(1, tentativas+1) :
    chute = int(input("insira seu chute:  "))
    if chute < 1 or chute > 40:
        print("por favor insira um numero entre 1 e 40")
        continue
    if chute == sorteio:
        print(f"está certo! : {sorteio} em {tentativa}")
    elif chute < sorteio:
        print("o numero é menor")
    else:
        print("o numero é maior")

if chute != sorteio:
    print("ops vc errou!")