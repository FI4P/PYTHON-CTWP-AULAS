#1 - Faça uma função que printa uma matriz da maneira convencional,ou seja, uma linha abaixo da outra

#Para fazer esse exercicio,iremos precisar percorrer todas as linhas da nossa matriz, printando uma de cada vez.

#Utilizando o for, conseguimos iterar sobre todas as linhas e printar elas especificamente de acordo com o indice do for.

def formataMatriz(matriz):
    for linha in range(len(matriz)):
        print(matriz[linha])

#Explicação: Dessa forma, eu percorro todas as linhas da minha matriz printando apenas a linha atual.


#2- Faça uma função que recebe de parâmetros as dimensões, (linhas e colunas), e retorna uma matriz preenchida de zeros com essas dimensões

#Para resolvermos essa questão, vamos percorrer linhas e as colunas. Nas linhas, iremos adicionar as colunas de acordo com os valores passados.
# E após isso, iremos adicionar as linha em uma matriz vazia.

def geraMatriz(numeroLinhas, numeroColunas, valorElementos = 0):
    matriz = [ ] #Define uma matriz vazia
    for linha in range(numeroLinhas):
        linhaMatriz = []
        for coluna in range(numeroColunas):
            linhaMatriz.append(valorElementos)
        matriz.append(linhaMatriz)
    return matriz
