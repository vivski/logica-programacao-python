# Q2

import random

num_participantes = int(input("digite o numero de participantes"))
pontuacoes = [random.randint(1,80) for _ in range(num_participantes)]

print("\nPontuações dos participantes:")

for i, pontuacao in enumerate(pontuacoes, start=1):
    print(f" Participante {i}: {pontuacao}")

maior_pontuacao = max(pontuacoes)
menor_pontuacao = min(pontuacoes)

maiores = pontuacoes.count(maior_pontuacao)
menores = pontuacoes.count(menor_pontuacao)

print(f"\nMaior pontuação: {maior_pontuacao} (empate: {maiores >1})")
print(f"\nMenor pontuação: {menor_pontuacao} (empate: {menores > 1})")
