#QUESTAO 1

pode_entrar = 0
nao_pode = 0

while True:
    idade = int(input("digite a idade (0 para sair)"))

    if idade == 0:
        break;       
    if idade < 15:
        print("Não permitida a entrada")
        nao_pode += 1
    elif idade < 18 or idade >= 75:
        print("Permitida a entrada com acompanhante")
        pode_entrar += 1
    elif 18 <= idade < 75:
        print("Permitida a entrada")
        pode_entrar += 1

print(f"Quantidade de pessoas que podem entrar: {pode_entrar}")
print(f"Quantidade de pessoas que não podem entrar: {nao_pode}")