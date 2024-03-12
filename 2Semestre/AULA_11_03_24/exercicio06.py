import methods
##6 - Faça um função que receba uma matriz quadrada e retorna sua transposta.

def transpostaMatriz(matriz):
    for i in range(len(matriz)):
        for j in range(i):
            aux = matriz[i][j]
            matriz[i][j] = matriz[j][i]
            matriz[j][i] = aux
    return matriz

matriz = [[1, 2 ,3 ], [4, 5 , 6], [7 , 8 , 9]]

# transpostaMatriz(matriz)

methods.formatMatriz(matriz)
            
    
