print("Bem-vindo ao teste de gosto por programação!")
print("Por favor, responda as perguntas abaixo com 'sim' ou 'não'.")

resposta = input("Você gosta de resolver problemas lógicos? ")
if resposta.lower() == "sim":
    resposta = input("Você gosta de trabalhar com números? ")
    if resposta.lower() == "sim":
        resposta = input("Você gosta de trabalhar com dados? ")
        if resposta.lower() == "sim":
            print("Você parece gostar de programação!")
        else:
            print("Você pode não gostar muito de programação.")
    else:
        print("Você pode não gostar muito de programação.")
else:
    print("Você pode não gostar muito de programação.")

