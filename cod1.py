class Pessoa:
    def __init__(self,nome,cpf,idade,email,senha):
        self.nome = nome
        self.cpf = cpf
        self.idade = idade
        self.email = email
        self.senha = senha

        def __str__(self):
            return f"nome: {self.nome}, cpf: {self.cpf}, idade: {self.idade}, email: {self.email}, senha: {self.senha}"

Pessoas= []

def cadastro():
    nomecadastro = input("Digite o nome de cadastro.")
    cpfcadastro = int(input("Seu CPF sem caracteres especiais, apenas números."))
    idadecadastro = int(input("Digite sua idade "))
    emailcadastro = input("Digite o email de cadastro.")
    senhacadastro = input("Digite a senha de cadastro.")
    novo_cadastro = Pessoa(nomecadastro,cpfcadastro,idadecadastro,emailcadastro,senhacadastro)
    Pessoas.append(novo_cadastro)

def login():
    print("Para login use o email e a senha criados no momento do cadastro.")
    email_login = input("Digite seu email")
    senha_login = input("Digite sua senha")
    for Pessoa in Pessoas:
        if email_login == Pessoa.email and Pessoa.senha == senha_login:
            print("Parabéns, login feito com sucesso")
        else:
            print("Senha ou email incorretos, por favor crie uma conta")

while True:
    print("Bem Vindo ao Sistema do Governo - SisGov.com.br ")
    print("Digite a opcao que deseja")
    print("1 - cadastro")
    print("2 - login")
    print("3 - logout/sair")
    opcao = int(input("Digite a opção escolhida"))
    match opcao:
        case 1:
            print("Bem vindo a pagina de cadastro")
            cadastro()
        case 2:
            print("Bem vindo a pagina de login")
            login()
        case 3:
            print("Logout...saiindo..")
            break
        case _:
            print("Opção inválida")