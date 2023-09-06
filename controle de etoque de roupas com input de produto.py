estoque = {'calça': 30, 'blusa': 30, 'camiseta': 30}

def registrar_saida():
    item = input('Digite o item que deseja retirar do estoque (calça, blusa ou camiseta): ')
    quantidade = int(input('Digite a quantidade que deseja retirar: '))
    if item in estoque:
        if estoque[item] >= quantidade:
            estoque[item] -= quantidade
            print(f'Saída registrada. Quantidade restante de {item}s: {estoque[item]}')
        else:
            print(f'Quantidade insuficiente em estoque. Quantidade restante de {item}s: {estoque[item]}')
    else:
        print('Item não encontrado no estoque.')

def mostrar_estoque():
    print('Estoque atual:')
    for item, quantidade in estoque.items():
        print(f'{item}: {quantidade}')

# Exemplo de uso
mostrar_estoque()
registrar_saida()
mostrar_estoque()
