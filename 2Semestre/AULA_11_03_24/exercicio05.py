import methods
##5 - Faça uma função que recebe matriz quadrada e altera todos os elementos acima/abaixo da diagonal para 1.

def changeDiagonalAboveElements(matriz, value):
    for i in range(len(matriz)):
        print(i)
        for j in range(i):
            matriz[i][j] = value
    return matriz

def changeDiagonalElements(matriz, value):
    for i in range(len(matriz)):
        print(i)
        for j in range(i):
            matriz[j][i] = value
    return matriz



matriz = methods.generateMatriz(3,3, 0)

changeDiagonalAboveElements(matriz, 1)
changeDiagonalElements(matriz, 1)


methods.formatMatriz(matriz)
            
                
            
    
