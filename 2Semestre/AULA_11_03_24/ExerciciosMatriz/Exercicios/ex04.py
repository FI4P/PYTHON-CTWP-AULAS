from methods import methods

#4 - faça uma função que recebe uma matriz quadrada como parâmetro e altera todos os elementos da contra-diagonal para 1.

def alteraContraDiagonal(matrizQuadrada, valorElementos = 0):
    #Percorre as linhas da matriz
    for linha in range(len(matrizQuadrada)):
    #Percorre os elementos da linha atual
        for coluna in range(len(matrizQuadrada[linha])):
            #Comprimento da matriz
            comprimentoMatriz = len(matrizQuadrada) - 1
            #Verifica se a soma dos indices do elemento atual são iguais ao comprimento da matriz
            if(linha + coluna == comprimentoMatriz):
                matrizQuadrada[linha][coluna] = valorElementos
    return matrizQuadrada

def alteraContraDiagonalRefatorada(matrizQuadrada, valorElementos = 0):
    for linha in range(len(matrizQuadrada)):
        comprimentoMatriz = len(matrizQuadrada) - linha
        matrizQuadrada[linha][comprimentoMatriz - 1] = valorElementos
    return matrizQuadrada


matrizQuadrada = methods.geraMatriz(3 , 3)
methods.formataMatriz(alteraContraDiagonalRefatorada(matrizQuadrada, 1))


#Para resolver esse exercicio utilizamos duas estruturas de repetição for, uma para percorrer as linhas da matriz e a segunda os elementos que compoem essa linha. 

# Uma contra diagonal é definida quando a soma dos indices dos elementos são iguais ao comprimento da matriz, então bastou apenas verificar se o indice do elemento atual é igual ao comprimento da matriz.

#Podemos também resolver esse exercicio utilizando apenas um for. Primeiro calculamos o comprimento da nossa matriz, depois iremos subtrair o indice que indica a linha atual do comprimento e o resultado disso subtrair por 1. 

#Tendo uma matriz 3 x 3 como exemplo, quando o indice da linha for 0, o elemento que será alterado irá ser: elemento[linha][comprimento - linha -1]

# Resultado (Linha = 0, comprimento = 3 | coluna = (comprimento - linha) - 1 = 2) - Soma dos indices do elemento é igual ao comprimento  - elemento[0][2]
# Resultado (Linha = 1, comprimento = 3 | coluna = (comprimento - linha) - 1 = 1) - Soma dos indices do elemento é igual ao comprimento  - elemento[1][1]
# Resultado (Linha = 2, comprimento = 3 | coluna = (comprimento - linha) - 1 = 0) - Soma dos indices do elemento é igual ao comprimento  - elemento[0][2]





                
