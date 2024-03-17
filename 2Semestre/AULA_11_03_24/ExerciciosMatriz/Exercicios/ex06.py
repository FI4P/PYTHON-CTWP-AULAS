from methods import methods

def matrizTransposta(matrizQuadrada):
    #Percorre as linhas da matriz
    for linha in range(len(matrizQuadrada)):
    #Percorre os itens da linha, tirando os itens que compoem a diagonal
        for coluna in range(linha):
            aux = matrizQuadrada[linha][coluna]
            matrizQuadrada[linha][coluna] = matrizQuadrada[coluna][linha]
            matrizQuadrada[coluna][linha] = aux
    return matrizQuadrada


matrizQuadrada = [ [ 1 , 2 , 3 ] , 
           [ 4 , 5 , 6 ] , 
           [ 7 , 8 , 9 ] ]

methods.formataMatriz(matrizTransposta(matrizQuadrada))