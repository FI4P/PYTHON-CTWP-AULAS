
#1 - Faça uma função que printa uma matriz da maneira convencional,ou seja, uma linha abaixo da outra

def formataMatriz(matriz):
    #Percorre as linhas da minha matriz
    for linha in range(len(matriz)):
        #Printa no console linha a linha da minha matriz
        print(matriz[linha])

## 2- Faça uma função que recebe de parâmetros as dimensões, (linhas e colunas), e retorna uma matriz preenchida de zeros com essas dimensões

def geraMatriz(linhas, colunas, valorElementos = 0):
    matrizGerada = []
    for linha in range(linhas):
        linhaMatriz = []
        for coluna in range(colunas):
            linhaMatriz.append(valorElementos)
        matrizGerada.append(linhaMatriz)
    return matrizGerada

matriz = geraMatriz(3, 3)
    
##3 - Faça uma função que recebe uma matriz quadrada como parâmetro e altera todos os elementos da diagonal

def alteraDiagonal(matrizQuadrada, valorElementos = 0):
    #Percorre todas as linhas da minha matriz
    for linha in range(len(matrizQuadrada)):
        #Altera todos os elementos em que os indices são iguais
        matrizQuadrada[linha][linha] = valorElementos
    return matrizQuadrada


# formataMatriz(alteraDiagonal(matriz,1))

##4 - faça uma função que recebe uma matriz quadrada como parâmetro e altera todos os elementos da ˜contra-diagonal para 1.

def alteraContraDigonal(matrizQuadrada, valorElementos = 0):
    for linha in range(len(matrizQuadrada)):
            comprimento = len(matriz[linha]) - linha
            matriz[linha][comprimento - 1] = valorElementos

    return matrizQuadrada

# formataMatriz(alteraContraDigonal(matriz,1))

##5 - Faça uma função que recebe matriz quadrada e altera todos os elementos acima/abaixo da diagonal para 1.

def alteraElementosAcimaAbaixo(matrizQuadrada, valorElementos = 0):
    for linha in range(len(matrizQuadrada)):
        for coluna in range(linha):
            matrizQuadrada[linha][coluna] = valorElementos
            matrizQuadrada[coluna][linha] = valorElementos
    return matrizQuadrada

# formataMatriz(alteraElementosAcimaAbaixo(matriz,1))

##6 - Faça um função que receba uma matriz quadrada e retorna sua transposta.

def geraMatrizTranposta(matrizQuadrada):
    for linha in range(len(matrizQuadrada)):
        for coluna in range(linha):
            aux = matrizQuadrada[linha][coluna]
            matrizQuadrada[linha][coluna] = matrizQuadrada[coluna][linha]
            matrizQuadrada[coluna][linha] = aux
    return matrizQuadrada


matriz = [[1, 2, 3], [4, 5,6], [7 ,8 ,9]]
formataMatriz(geraMatrizTranposta(matriz))



#7 -Uma matriz retangular da forma 5xN (5 linhas e N colunas) representa as notas de alunos em 5provas. Cada linha é a nota de um aluno em uma das provas, enquanto cada coluna representa as 5 notas de um aluno somente.

def mediaPonderada(listaPesos, notasAlunos):
    mediaPonderada = []
    somaPesos = 0
    #Percorre lista de pesos e faz a soma de todos
    for peso in range(len(listaPesos)):
        somaPesos += listaPesos[peso]
        
    for coluna in range(len(notasAlunos[0])):
        somaNotaPesos = 0
        for linha in range(len(listaPesos)):
            somaNotaPesos += listaPesos[linha] * notasAlunos[linha][coluna]
        mediaPonderada.append(somaNotaPesos/somaPesos)
    return mediaPonderada

pesoMateria = [1 , 2 , 3 , 2 , 1]

matrizNotasAlunos = [
    [ 10, 7], 
    [ 9 , 2], 
    [ 5 , 9], 
    [ 3 , 1], 
    [ 10, 0]
]

print(mediaPonderada(pesoMateria, matrizNotasAlunos))


     
'''''
                          | 10 10 10 10 |
                          | 10 10 10 10 |
 [1 , 2, 3 , 4 , 5]  *    | 10 10 10 10 |
                          | 10 10 10 10 |
'''

#8 Faça um código que transforma uma matriz quadrada 8x8 em um tabuleiro de xadrez.


#9 - Faça um código que recebe uma matriz quadrada e reona uma imagem com padrã de circulo



