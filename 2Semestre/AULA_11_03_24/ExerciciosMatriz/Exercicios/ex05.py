from methods import methods

##5 - Faça uma função que recebe matriz quadrada e altera todos os elementos acima/abaixo da diagonal para 1.

def alteraElementosAcimaAbaixo(matrizQuadrada, valorElemento = 0):
    #Percorre as linhas da matriz
    for linha in range(len(matrizQuadrada)):
    #Percorre os elementos da linha atual
        for coluna in range(len(matrizQuadrada[linha])):
            if(linha != coluna):
                matrizQuadrada[linha][coluna] = valorElemento
    return matrizQuadrada

def alteraElementosAcimaAbaixoRefatorada(matrizQuadrada, valorElemento = 0):
    for linha in range(len(matrizQuadrada)):
        for coluna in range(linha):
            matrizQuadrada[linha][coluna] = valorElemento
            matrizQuadrada[coluna][linha] = valorElemento
    return matrizQuadrada

matrizQuadrada = methods.geraMatriz(3, 3)

methods.formataMatriz(alteraElementosAcimaAbaixoRefatorada(matrizQuadrada, 1))

#Explicando: Como vimos, os elementos acima da diagonal são caracterizados por possuir o indice de coluna maior que o indice da linha e os elementos abaixo o contrário. 
 
#Nesse exercicio, verificamos se o indice da linha e coluna do elemento atual são divergentes, caso verdadeiro, mudamos o elemento respectivo dessa posição. Fizemos dessa forma pois sabemos que os elementos da diagonal principal tem seus indices de coluna e linha iguais.

#Podemos resolver esse exercicio sem utilizar a verificação if. Para que isso seja possivel, o nosso segundo for precisa ser iteradoma em relação ao range da linha. Isso facilita pois assim, evitamos de fazer uma verificação a mais em nosso algoritimo.

