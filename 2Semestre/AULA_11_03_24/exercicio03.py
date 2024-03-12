##3 - Faça uma função que recebe uma matriz quadrada como parâmetro e altera todos os elementos da diagonal
import methods


def diagonalChange(matriz, value):
    for i in range(len(matriz)):
        matriz[i][i] = value
    return matriz

matriz = methods.generateMatriz(3 , 3 , 0)

diagonalChange(matriz, 1)
methods.formatMatriz(matriz)








