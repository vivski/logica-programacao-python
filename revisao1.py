# 1. Sistema de controle de estoque de livraria Crie um sistema simples
#  onde o usuário pode visualizar livros disponíveis para venda e comprar
#   apenas um exemplar por vez. O sistema 
# deve permitir que o usuário escolha um livro por ID ou nome e, 
# ao final, exiba o resumo da compra e o valor total.

print("Bem-vindo(a) a nossa livraria")
print("O sistema só permite comprar uma unidade ")
print("PRODUTOS DISPONÍVEIS NO SISTEMA: ")

class Livro: 
    def __init__(self, id,nome,preco,quantidade):
        self.id = id
        self.nome = nome
        self.preco = preco
        self.quantidade = quantidade
    def __str__(self):
        return f"id: {self.id}, nome: {self.nome}, preço: {self.preco}, quantidade: {self.quantidade}"

livros = [
    Livro(1,"harry potter",60,1),
    Livro(2,"Alice",65,1),
    Livro(3,"Inglês Infantil",25,1),
    Livro(4,"Livro para colorir",15,1),
]

for livro in livros:
    print(livro)


quantidadelivro = int(input("digite a quantidade de livros que voce quer levar"))

if quantidadelivro > 1:
    print("você não pode levar mais de um item")
else:
    listacompras = []
    valortotal = 0
    for _ in range(quantidadelivro):
     pedido = input("Digite o id do livro que você quer levar.")
     livro_encontrado = None;
     if pedido.isdigit():
        livro_encontrado = next((livro for livro in livros if livro.id == int(pedido)), None)
     if livro_encontrado:
        listacompras.append(livro_encontrado.id)
        valortotal += livro_encontrado.preco
     else:
        print("produto inválido. Tente novamente.")

print("Resumo do seu pedido.")
for id_livro in listacompras:
    livro_escolhido = next((livro for livro in livros if livro.id == id_livro), None)
    print(f"{livro_escolhido}")

print(f"O VALOR DA SUA COMPRA É: R$ {valortotal:.2f}")
