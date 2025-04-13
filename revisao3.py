# Recebe o número de quantas pessoas deseja calcular o IMC;
# Recebe o sexo, idade e altura de cada pessoa;
# Calcula o IMC de cada pessoa;
# Retorna a quantidade de pessoas em cada classificação e a lista de IMCs calculados.

print("Quantas pessoas querem calcular o IMC?")
# print("Digite o sexo feminino OU masculino")
# print("Digite a altura")
quantidade = int(input("Digite a quantidade de pessoas que desejam calcular o IMC."))

for _ in range(quantidade):
  sexopessoa = input("Qual o sexo?") 
  idadepessoa = input("quantos anos?")
  alturapessoa = float(input("digite a altura"))
  pesopessoa = float(input("qual o seu peso"))
  if sexopessoa == "feminino":
    imc = (pesopessoa/ (alturapessoa * alturapessoa))
    print(f"seu IMC é {imc:.2f}")
  else:
    imc = (pesopessoa/ (alturapessoa * alturapessoa))
    print(f"seu IMC é {imc:.2f}")
