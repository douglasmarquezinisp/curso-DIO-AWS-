import datetime

def obter_ano():
    while True:
        try:
            ano = int(input("Digite o ano de nascimento (1922-2021): "))
            if 1922 <= ano <= 2021:
                return ano
            else:
                print("Ano inválido. Digite um ano entre 1922 e 2021.")
        except ValueError:
            print("Entrada inválida. Digite um valor numérico.")

def calcular_idade(ano_nascimento):
    ano_atual = datetime.datetime.now().year
    idade = ano_atual - ano_nascimento
    return idade

nome_completo = input("Digite seu nome completo: ")
ano_nascimento = obter_ano()

idade = calcular_idade(ano_nascimento)
print(f"Olá, {nome_completo}! Você tem {idade} anos.")
