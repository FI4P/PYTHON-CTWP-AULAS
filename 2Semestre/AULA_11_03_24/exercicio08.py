import methods

#8 Faça um código que transforma uma matriz quadrada 8x8 em um tabuleiro de xadrez.

def generateXadrez(matriz):
    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            if(i % 2 == 0 and j % 2 == 0) or (i % 2 != 0 and j % 2 != 0):
                matriz[i][j] = 0
            else:
                matriz[i][j] = 1
                
matriz = methods.generateMatriz(8 , 8 , 0)

generateXadrez(matriz)


methods.formatMatriz(matriz)