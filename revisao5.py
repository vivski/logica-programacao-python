# Receber as notas de 10 alunos
notas = []
for i in range(10):
    nota = float(input(f"Digite a nota do aluno {i+1}: "))
    notas.append(nota)

while True:
    print("\nMenu:")
    print("1 - Informar a maior e menor nota da turma")
    print("2 - Informar a média geral da turma")
    print("3 - Encerrar o programa")
    
    opcao = int(input("Escolha uma opção: "))
    
    if opcao == 1:
        print(f"Maior nota: {max(notas)}, Menor nota: {min(notas)}")
    elif opcao == 2:
        print(f"Média geral: {sum(notas) / len(notas):.2f}")
    elif opcao == 3:
        print("Programa encerrado.")
        break
    else:
        print("Opção inválida!")