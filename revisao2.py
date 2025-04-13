# 2. Sistema de registro de alunos Crie um sistema onde o usuário pode registrar até 5 alunos , 
# informando o nome, a idade e a turma. 
# O sistema deve armazenar as informações em uma lista de objetos 
# e, ao final, exibir todos os alunos cadastrados.

print("Sistema de registro de alunos")
print("O sistema só permite registrar até 5 alunos")

class Aluno: 
    def __init__(self, nome, idade, turma):
        self.nome = nome
        self.idade = idade
        self.turma = turma
    def __str__(self):
        return f"Nome: {self.nome}, Idade: {self.idade}, Turma: {self.turma}"

# Lista para armazenar os alunos
alunos = []

# Loop para cadastrar até 5 alunos
for i in range(5):
    nome = input(f"Digite o nome do aluno {i+1}: ")
    idade = int(input("Digite a idade: "))
    turma = input("Digite a turma do aluno (1, 2 ou 3): ")
    
    aluno = Aluno(nome, idade, turma)
    alunos.append(aluno)  # Adicionar o objeto aluno na lista

# Exibir todos os alunos cadastrados
print("\nAlunos cadastrados:")
for aluno in alunos:
    print(aluno)  # Chama o método __str__ e exibe os dados
