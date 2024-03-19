from methods import methods

#8 Faça um código que transforma uma matriz quadrada 8x8 em um tabuleiro de xadrez.

def geraTabuleiroXadrez(matrizQuadrada):
    #Percorre as linhas da minha matriz
    for linha in range(len(matrizQuadrada)):
        #Percorre os itens da minha linha atual
        for coluna in range(len(matrizQuadrada[linha])):
             if(linha % 2 == 0 and coluna % 2 == 0) or (linha % 2 != 0 and coluna % 2 != 0):
                matrizQuadrada[linha][coluna] = 1
    return matrizQuadrada


matrizQuadrada = methods.geraMatriz(8,8, 0)

methods.formataMatriz(geraTabuleiroXadrez(matrizQuadrada))