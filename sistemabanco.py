saldo = 0

def exibir_saldo():
    print(f"Saldo = R${saldo}")


while True:
    print("1 - Saldo")
    print("2 - Depositar")
    print("3 - Sacar")
    print("4 - Sair")
    opcao = int(input("Digite uma das opções:"))


    match opcao:
      case 1:
        print("* Saldo na Conta *")
        exibir_saldo()
      case 2:
        print("* Depositar *")
        valor_deposito = float(input("Qual o valor a depositar? "))
        saldo += valor_deposito
        exibir_saldo()
      case 3:
        print("* Sacar *")
        valor_saque = float(input("Qual o valor a sacar? "))
        saldo -= valor_saque
        exibir_saldo()
      case 4:
        print("Opção válida")
        break
      case _:
          print("Opção inválida")
