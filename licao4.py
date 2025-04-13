# LISTA 03 - Condicional simples

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
numero1 = int(input("digite um primeiro valor"))
numero2 = int(input("digite um segundo valor"))
if(num1 <= num2):
    print(f"o {numero1} é menor ou igual a {numero2}")
else:
    print(f"o {numero2} é maior ou igual a {numero1}")
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

# Q7. Elabore um algoritmo para representar um sistema de compra
# de produtos agrícolas de uma feira, mas que só permite realizar
# a compra, se a pessoa tiver dinheiro para pagar à vista e se estiver
# com a anuidade de associação de produtor rural em dia. 

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

