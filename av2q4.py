# Q4 (3.0 pontos) Elabore um programa que analisa os nomes completos
# fornecidos pelos usuários. O programa deve:
# 1. Criar uma função chamada analisar_nome que receba uma string
# representando o nome completo do usuário e retorne três valores
# dentro de uma tupla:
# ○ O primeiro nome.
# ○ O último nome (ou "Não encontrado" se não houver).
# ○ O número total de caracteres do nome (desconsiderando
# espaços).

# 2. No programa principal:
# ○ Solicitar ao usuário que insira um nome completo.
# ○ Chamar a função analisar_nome com o nome fornecido.
# ○ Imprimir os resultados no formato adequado.

def analisar_nome(nome_completo):
    partes = nome_completo.split()
    primeiro_nome = partes[0]
    ultimo_nome = partes[-1] if len(partes) > 1 else "não encontrado"
    total_caracteres = len("". join(partes))
    return primeiro_nome, ultimo_nome, total_caracteres

nome_completo = input("digite seu nome completo").strip()
primeiro, ultimo, total = analisar_nome(nome_completo)

print(f"primeiro nome: {primeiro}")
print(f"Último nome: {ultimo}")
print(f"Número total de caracteres (sem espaços): {total}")