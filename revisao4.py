# Exibe o cardápio;
# Cliente pode fazer pedido;
# Ao finalizar compras, mostrar opção de pagamento com 
# resumo da compra e valor a ser pago;
# Finaliza o programa.

print("Bem vindo ao restaurante Bons Bocados")

class Pratos:
    def __init__(self,nome,preco):
        self.nome = nome
        self.preco = preco
    def __str__(self):
        return f"nome do prato: {self.nome} & preço R$ {self.preco}"

listapratos = [
    Pratos("Macarronada",19.50),
    Pratos("Lasanha",29.30),
    Pratos("Focaccia", 15.00)
]

for prato in listapratos:
    print(prato)

pedido = int(input("Quantos itens deseja levar?"))

listacompras = []
valortotal = 0

for i in range(pedido):
    nomedoprato = input("Qual o nome do prato? ")
    for prato in listapratos:
        if nomedoprato.lower() == prato.nome.lower():
            valortotal += prato.preco

    
print(f"\nValor total a ser pago: R$ {valortotal:.2f}")


print("As formas de pagamento são débito ou crédito, qual você deseja? DIGITE 1 OU 2")
formpagamento = int(input("Digite 1 ou 2 "))

if formpagamento == 1:
    print(f"O valor a ser pago é R$ {valortotal:.2f} sem juros")
elif formpagamento == 2:
    print(f"O pagamento é crédito e fica R$ {valortotal:.2f} + uma taxa de R$ 5 ")
else:
    print("Nenhuma informação fornecida. Compra cancelada.")
