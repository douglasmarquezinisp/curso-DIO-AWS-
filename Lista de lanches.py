listaDelanches = ['misto', 'xsalada', 'xburguer', 'salada', 'xegg']

novo_lanche = input("Digite o nome do lanche que deseja comer: ")

def acharElemento(array, elemento):
    elementoEncontrato = False
    posicao = False

    for i in range(len(array)) :
      if (array[i] == elemento):
          elementoEncontrato = True
          posicao = i
          break

    if(elementoEncontrato == True):
     print('Encontrei o lanche', posicao)
    else:
     print("Não encontrei o lanche")

acharElemento(listaDelanches,novo_lanche)