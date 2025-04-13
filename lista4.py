# LISTA 04

# Q1. Faça um algoritmo que lê dois números, 
# e verifica se os dois números são iguais. Se forem iguais, 
# escrever "São iguais", se não, escrever "Não são iguais".
num1 = int(input("digite um primeiro valor"))
num2 = int(input("digite um segundo valor"))
if(num1 == num2):
    print("são iguais.")
else:
    print("são diferentes.")
# Q2. Faça um algoritmo que lê dois números, e verifica
# se o primeiro número é maior ou igual ao segundo número. 
# Se for, escrever "O número {valor do número 1} é maior ou igual ao número 
#     {valor do número 2}". Se não, escrever "O número {valor do número 1} 
# é menor ou igual ao número {valor do número 2}".
valor1 = int(input("digite um primeiro valor para comparar"))
valor2 = int(input("digite um segundo valor para comparar"))
if (valor1 >= valor2):
    print(f"o {valor1} é maior ou igual a {valor2} ")
else:
    print(f"o {valor1} é menor ou igual a {valor2}")
# Q3. Faça um algoritmo que lê dois números, e verifica
# se o primeiro número é menor ou igual ao segundo número.
# Se for, escrever "O número {valor do número 1} é menor ou igual 
#     ao número {valor do número 2}". Se não, escrever "O número
# {valor do número 1} é maior ou igual ao número {valor do número 2}".
numero1 = int(input("insira o 1º numero "))
numero2 = int(input("insira o 2º valor"))
if(numero1 <= numero2):
    print(f"O {numero1} é menor ou igual a {numero2}")
else:
    print(f"O {numero1} é maior que {numero2}")
# Q4. Faça um algoritmo que lê dois números, e verifica se o primeiro
# número é igual ao segundo número. Se forem iguais, escrever 
# "Números iguais". Se não, escrever "Números diferentes".
numm1 = int(input("digite um primeiro valor"))
numm2 = int(input("digite um segundo valor"))
if(numm1 == numm2):
    print("numeros são iguais.")
else:
    print("números são diferentes.")
# Q5. Faça um algoritmo que irá fazer o cadastro de usuário. 
# Para isso, solicita o nome do usuário, e a senha. Depois, pede que 
# o usuário confirme novamente a senha. O sistema deverá verificar se 
# as senhas digitadas são iguais. Se forem iguais, informar que o cadastro 
# está correto. Se não forem iguais, informar que o cadastro 
# não foi realizado porque as senhas não conferem.
nomeusuario = input("Digite o seu nome")
senhausuario = input("Digite sua senha")
confirmarsenha = input("Digite a senha novamente para realizar o cadastro.")

if(senhausuario == confirmarsenha):
    print(f"olá {nomeusuario}, o cadastro está correto")
else:
    print(f"olá {nomeusuario}, o cadastro não foi realizado porque as senhas não conferem")

# Q6. Elabore um algoritmo para representar um sistema de 
# compra de produtos agrícolas de uma feira, mas que só permite compras à vista.
print("Bem-vindo(a) a nossa loja de produtos agrícolas!")
print("O sistema só permite comprar uma unidade de cada produto e a única forma de pagamento é à vista.")
print("PRODUTOS DISPONÍVEIS NO SISTEMA: ")

class Produto:
    def __init__(self, id, nome, preco, quantidade):
        self.id = id
        self.nome = nome
        self.preco = preco
        self.quantidade = quantidade
    
    def __str__(self):
        return f"ID: {self.id}, Produto: {self.nome}, Preço: R$ {self.preco}, Quantidade: {self.quantidade}"


produtos = [
    Produto(1, "laranja", 20, 1),
    Produto(2, "Cacau", 30, 1),
    Produto(3, "feijão", 8, 1),
    Produto(4, "beterraba", 7, 1),
    Produto(5, "café", 30, 1),
    Produto(6, "cereal", 15, 1),
    Produto(7, "milho", 10, 1),
    Produto(8, "batata inglesa", 8, 1),
    Produto(9, "batata doce", 5, 1),
    Produto(10, "soja", 20, 1)
]

for produto in produtos:
    print(produto)

print("Faça o login no sistema para realizar seu pedido")
usuarionome = input("Digite o seu nome: ")
usuariosenha = input("Digite a senha: ")
confirmarsenha = input("Confirmar senha: ")
quantidadeitens = int(input("Quantidade de itens que deseja levar (até 10 itens, 1 unidade de cada): "))

if quantidadeitens > 10:
    print("Você pode levar no máximo 10 itens.")
else:
    listacompras = []
    valorTotal = 0
    
    for _ in range(quantidadeitens):
        pedido = input("Digite o nome ou o ID do produto: ")
        
        produto_encontrado = None
        if pedido.isdigit():
            produto_encontrado = next((produto for produto in produtos if produto.id == int(pedido)), None)
        else:
            produto_encontrado = next((produto for produto in produtos if produto.nome.lower() == pedido.lower()), None)
        
        if produto_encontrado:
            listacompras.append(produto_encontrado.id)
            valorTotal += produto_encontrado.preco
        else:
            print("Produto inválido. Tente novamente.")
    
    print(f"RESUMO DO SEU PEDIDO: ")
    for id_produto in listacompras:
        produto_selecionado = next(produto for produto in produtos if produto.id == id_produto)
        print(f"{produto_selecionado}")

    print(f"O VALOR DA SUA COMPRA É: R$ {valorTotal:.2f}")
    
    formapagamento = input("Como deseja pagar? (Digite 'à vista' para confirmar): ")
    if formapagamento.lower() == "à vista":
        print(f"Obrigado, {usuarionome}, compra feita com sucesso!")
    else:
        print(f"Sinto muito, {usuarionome}, sua compra não pode ser feita e seus dados serão descartados pelo sistema.")


# Q7. Elabore um algoritmo para representar um sistema de compra
# de produtos agrícolas de uma feira, mas que só permite realizar
# a compra, se a pessoa tiver dinheiro para pagar à vista e se estiver
# com a anuidade de associação de produtor rural em dia. 
print("Bem-vindo(a) a nossa loja de produtos agrícolas!")
print("O sistema só permite comprar uma unidade de cada produto e a única forma de pagamento é à vista.")
print("PRODUTOS DISPONÍVEIS NO SISTEMA:")

class Produto:
    def __init__(self, id, nome, preco):
        self.id = id
        self.nome = nome
        self.preco = preco
    
    def __str__(self):
        return f"ID: {self.id}, Produto: {self.nome}, Preço: R$ {self.preco}"

produtos = [
    Produto(1, "laranja", 20),
    Produto(2, "Cacau", 30),
    Produto(3, "feijão", 8),
    Produto(4, "beterraba", 7),
    Produto(5, "café", 30),
    Produto(6, "cereal", 15),
    Produto(7, "milho", 10),
    Produto(8, "batata inglesa", 8),
    Produto(9, "batata doce", 5),
    Produto(10, "soja", 20)
]

for produto in produtos:
    print(produto)

nome_usuario = input("Digite o seu nome: ")
quantidadeitens = int(input("Quantos itens deseja levar? (até 10 itens): "))

if quantidadeitens > 10:
    print("Você pode levar no máximo 10 itens.")
else:
    listacompras = []
    valorTotal = 0


    for i in range(quantidadeitens):
        pedido = int(input("Digite o ID do produto: "))
        for produto in produtos:
            if produto.id == pedido:
                listacompras.append(produto)
                valorTotal += produto.preco
                break

    print("\nRESUMO DO SEU PEDIDO:")
    for produto in listacompras:
        print(produto)

    print(f"Valor total da compra: R$ {valorTotal}")

    pagamento = input("Pagamento à vista? (Digite 'sim' para confirmar): ").lower()
    if pagamento == "sim":
        print(f"Obrigado pela compra, {nome_usuario}!")
    else:
        print("Compra não pode ser realizada. Somente pagamento à vista.")


# Q8. Elabore um algoritmo que solicita duas informações do usuário. 
# A primeira, pergunta se possui bolsa família (S ou N), e a segunda, 
# se possui mais de três filhos (S ou N). Se for contemplado pelo bolsa 
# família e possuir mais de três filhos, deverá retornar Verdadeiro, 
# significando que pode acessar à vaga de cotista.
bolsaf = input("possui bolsa família? (sim: S ou não: N) ")
filhos = input("possui mais de três filhos? (sim: S ou não: N) ")

if bolsaf == "s" and filhos == "s":
    print(True)

# Q9. Elabore um algoritmo para que só possa autorizar a 
# entrada na loja, àqueles que estão com a anuidade de associação 
# em dia ou pagar o valor de 25 reais na entrada.

anuidade = input("Você está com a anuidade em dia? (sim ou não): ")

if anuidade == "sim":
    print("Entrada permitida!")
else:
    pagaranuidade = input("Deseja pagar a entrada agora? (sim ou não): ")
    if pagaranuidade == "sim":
        pagamento = int(input("Insira o valor: "))
        if pagamento >= 25:
            print("Entrada permitida!")
        else:
            print("Valor insuficiente. Entrada negada!")
    else:
        print("Entrada negada!")

