# conversao de temperatura

def celsiusparakelvin(numero):
    k = numero + 273.15
    print(f" celsius para kelvin {k}")

def kelvinparacelsius(numero):
    c = numero + 273.15
    print(f" celsius para kelvin {c}")


while True:

        print("TERMINAL DE CONVERSÃO")
        print("DIGITE: 1 | CELSIUS PARA KELVIN")
        print("DIGITE: 2 | KELVIN PARA CELSIUS")
        print("DIGITE 3 | PARA SAIR")
        opcao = int(input("Digite a função desejada"))
        match opcao:
          case 1:
           numero = int(input("digite o valor q deseja converter para kelvin em celsius"))
           celsiusparakelvin(numero)
          case 2:
              numero = int(input("digite o valor q deseja converter em krlvin psra celsius"))
              kelvinparacelsius(numero)
          case 3:
              print("Saiiiindoo...")
              break

           




