from methods import methods 
 

##3 - Faça uma função que recebe uma matriz quadrada como parâmetro e altera todos os elementos da diagonal

def alteraDiagonal(matrizQuadrada, valorElementos =0):
    # Percorre o numero de linhas da matriz
    for linha in range(len(matrizQuadrada)):
        #Percorre os elementos da linha atual
        for coluna in range(len(matrizQuadrada[linha])):
            if(linha == coluna): matrizQuadrada[linha][coluna] = valorElementos
    return matrizQuadrada

def alteradiagonalRefatorado(matrizQuadrada, valorElementos = 0):
    for linha in range(len(matrizQuadrada)):
        #Coluna recebe o mesmo indice que a linha atual
        coluna = linha
        #Altera o elemento onde linha e coluna são iguais
        matrizQuadrada[linha][coluna] = valorElementos
    return matrizQuadrada


matrizQuadrada = methods.geraMatriz(3,3, 0)
methods.formataMatriz(alteradiagonalRefatorado(matrizQuadrada, 1))


#Explicando: Para resolver esse exercicio é necessário entender que os elementos da diagonal principal de uma matriz tem seus indices de coluna, linha iguais. 
 
#Uma vez que sabemos isso, precisamos apenas percorrer a matriz e verificar se o indice da linha atual é igual ao indice da coluna atual, caso seja verdade, subsitua o valor do elemento atual elemento[linha][coluna]

#Podemos resolver apenas com um for também, uma vez que queremos trocar os elementos com indices iguais. elemento[linha][linha]
           
