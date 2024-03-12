import methods

##4 - faça uma função que recebe uma matriz quadrada como parâmetro e altera todos os elementos da ˜contra-diagonal para 1.

def counterDiagonalChange(matriz, value):
    for i in range(len(matriz)):
        matriz[i][len(matriz)- i - 1] = value
    return matriz
    
    

matriz = methods.generateMatriz(3,3, 0)

counterDiagonalChange(matriz, 1)

methods.formatMatriz(matriz)




