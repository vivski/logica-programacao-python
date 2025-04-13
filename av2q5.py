# Q5 (4.0 pontos). Elabore um programa para simular um gerenciamento de
# acesso ao sistema. O programa deve conter apresentar um menu que só
# encerra se escolhida a opção 3. (...)

import re

usuarios = []

def validar_nome_usuario(nome):
    if len(nome) < 5 or "@" not in nome or "." not in nome:
        raise ValueError("nome de usuario invalido. deve conter pelo menos 5 caracteres um @ e um .")
    if any(usuario['nome'] == nome for usuario in usuarios):
        raise ValueError("Nome não encontrado na lista de usuarios")
    
def validar_senha(senha):
    if not (6 <= len(senha) <= 8):
        raise ValueError("senha invalida. deve ter de 6 a oito digitos")
    if len(re.findall(r'[0-9]', senha)) < 2:
        raise ValueError("senha invalida. minimo 2 numeros.")
    if len(re.findall(r'[a-zA-Z]', senha)) < 2:
        raise ValueError("senha invalida. minimo 2 letras")
    if len(re.findall(r'[!@#$%^^&*()]', senha)) < 2:
        raise ValueError("senha invalida. minimo 2 caracteres especiais")

#ex email: vivian@gmail.com
#ex senha: ab12#$as

def criar_usuario():
    try:
        nome = input("digite seu nome").strip()
        if not nome:
            raise ValueError("obrigatorio fornecer um nome para acessar o sistema")
        validar_nome_usuario(nome)
  
        senha = input("crie sua senha / forneça uma senha").strip()
        if not senha:
            raise ValueError("obrigatorio ter uma senha para acessar o sistema")
        validar_senha(senha)

        usuarios.append({'nome': nome, 'senha': senha})
        print("cadastro concluido! bem-vinde")
    except ValueError as e:       
        print(f"Erro: {e}")

def acessar_sistema():
    try:
        nome = input("digite o nome")
        if not nome:
            raise ValueError("nome de usuario é obrigatorio.")
        senha = input("digite sua senha")
        if not senha:
            raise ValueError("forneça uma senha, é obrigatorio")

        usuario = next((u for u in usuarios if u['nome'] == nome and u['senha'] == senha), None)
        if usuario:
            print("acesso liberado")
        else:
            print(":( acesso negado! :( ")
    except ValueError as e:
        print(f"Erro: {e}")

def menu():
    while True:
        print("\n--- Menu ---------")    
        print("1. CADASTRO")    
        print("2. ENTRAR NO SISTEMA")  
        print("3. SAIR")  
        try:
            opcao = int(input("digite a opcao"))
            match opcao:
                case 1:
                    criar_usuario()
                case 2:
                    acessar_sistema()
                case 3:
                    print("Saiindoo...")
                    break
                case _:
                    print("invalido.")           
        except ValueError:
            print("entrada invalida")  
menu()