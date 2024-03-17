# Matriz em PY nada mais é do que uma lista PAI que contém sublistas FILHO

#Cada sublista dentro de uma Lista PAI representa uma linha da matriz

#Cada elemento da sublista irá representar a coluna da matriz.

# Representando uma matriz: [  [ col-00 , col-01 , col-02 ], [ col-10 , col-11 , col-12 ] , [ col-20 , col-21 , col22 ] ]

#Observando, vemos que as linhas são o conjunto todo da sublista e as colunas são representadas pelos elementos da sublista.

#É importante observar que os índices das colunas sempre começam em zero em uma matriz. Portanto, o índice final das colunas será sempre tamanhoTotalMatriz - 1.

#Montando uma matriz em py:

# matriz = [ [ "col 0,0", "col 0,1", "col 0,2"] , ["col 1,0", "col 1,1", "col 1,2"] , ["col 2,0", "col 2,1", "col 2,2"] ]

#Para acessarmos um determinado elemento da nossa matriz precisamos especificar qual linha que ele está e em qual coluna.

#Exemplo: Acessando o elemento "col 1,2" da nossa matriz

# col12 = matriz[1][1]


#Lembrando que o primeiro indice é referente a lista de linhas, e o segundo referente a posição do elemento dentro dessa sublista de linha, colunas.

#===================================================================================================================================================#

#Podemos percorrer uma matriz e seus elementos utilizando o for. O primeiro for representa as linhas da matriz e o segundo as colunas.

# Exemplo Exibir todas as linhas da matriz, uma abaixo da outra.

# for linha in range(len(matriz)):
#     if(linha == 0) : termo = "Primeira"
#     if(linha == 1) : termo = "Segunda"
#     if(linha == 2) : termo = "Terceira"
#     print(f"{termo} linha")
#     print(matriz[linha])

#Nesse caso, iteramos sobre len(Matriz) pois isso representa a quantidade de linhas da matriz.

#No primeiro momento, linha começa como 0 e representa a primeira linha da nossa matriz e assim que termina, vira um e assim por diante.

#Caso queiramos verificar elementos especificos da nossa matriz, podemos utilizar o segundo for que representa as colunas


# for linha in range(len(matriz)):
#     for coluna in range(len(matriz[linha])):
#         print(matriz[linha][coluna])

#O segundo for é len(matriz[linha]) pois precisamos percorrer todos os elementos presentes na linha especifica.
        
#Nessa caso, printamos todos os elementos da nossa matriz. O primeiro for só ira mudar, assim que o segundo for finalizado.


#===========================================================================================================================#

#Uma matriz quadrada é uma matriz em que o número de colunas e o mesmo que o número de linhas.

#Podemos representar essa matriz da seguinte forma: [ [ 1 , 1 , 1] , [ 2 , 2 , 2] , [3 , 3 , 3] ]


matriz = [ [ 1 , 2 , 3 ] , 
           [ 4 , 5 , 6 ] , 
           [ 7 , 8 , 9 ] ]

for linha in range(len(matriz)):
    resultado =  "Não Quadrada" if len(matriz[linha]) != len(matriz) else "Quadrada"    

#==========================================================================================================================#

#A diagonal principal de uma matriz é definida pelo indice da coluna ser igual ao indice da coluna

#Podemos descobrir a diagonal de uma matriz utilizando um for ou dois com uma verificação.

#Exemplo: Printando os elementos da diagonal de uma matriz

# for linha in range(len(matriz)):
#     for coluna in range(len(matriz[linha])):    
#         # Se indice linha == indice coluna (elemento diagonal)
#         if(linha == coluna):
#             print(matriz[linha][coluna])

#======================================================================================================================================#

# A contra diagonal de umatriz é definida pelos elementos em que a soma dos indices linha e coluna são igual ao comprimento dela (tamanhoTotalmatriz -1)

#Podemos definir o tamanho de uma matriz pegando o número de colunas e subtraindo 1. Isso ocorre pois o indice de uma matriz começa em zero.


# for linha in range(len(matriz)):
#     for coluna in range(len(matriz[linha])):
#         comprimento = len(matriz[linha]) - 1
#         if(linha + coluna == comprimento):
#             print(matriz[linha][coluna])

#Podemos printar os elementos da contra diagonal da nossa matriz utilizando apenas um for. Sabendo que a contra diagonal é definida quando a soma dos indices do nosso elemento é igual ao comprimento da nossa matriz, podemos subtrair o comprimento total da nossa matriz pela linha atual - 1, descobrindo o elemento que satisfaz essa condição.

# for linha in range(len(matriz)):
#     #Elemento em que a soma dos indices é igual ao comprimento
#     comprimento = len(matriz) - linha 
#     print(matriz[linha][comprimento - 1])


#========================================================================================================================================================#


#Os elementos acima da diagonal principal de uma matriz podem ser definidos quando o indice que representa a coluna do elemento é maior que a linha em que ele se encontra. Seguindo a mesma lógica, os elementos que se encontram abaixo da diagonal principal podem ser definidos quando o indice da linha é maior que o indice que representa a coluna em que ele se encontra.

#Exemplo: Printando os elementos acima da diagonal da matriz

# for linha in range(len(matriz)):
#     for coluna in range(len(matriz[linha])):
#         if(coluna > linha):
#             print(matriz[linha][coluna])
            
#Exemplo: Printando os elementos abaixo da diagonal da matriz

# for linha in range(len(matriz)):
#     for coluna in range(len(matriz[linha])):
#         if(linha > coluna):
#             print(matriz[linha][coluna])

#É possivel trocar todos os elementos da nossa matriz sem utilizarmos uma verificação if. Com duas estruturas de repetição, uma para percorrer a quantidade de linhas e a outra para percorrer o indice da linha atual.

#Fazendo com que o elemento da matriz na posição elemento[coluna][linha] que sempre será os acimas da diagonal recebam o valor novo. Fazendo o contrário, colocando elemento[linha][coluna], estamos fazendo com que os elementos abaixo da diagonal sejam alterados.


# Exemplo - Printando elemento abaixo da diagonal: Tendo uma raiz 3 x 3 como exemplo, quando a linha for 0, nosso segundo for não será executado. Tendo linha como 1, nosso segundo for será executado uma vez e coluna terá como posição 0, logo elemento[linha][coluna] vale respectivamente elemento[1][0].

# Simulando tudo: 

#1- (Linha = 0, coluna = 0 - Não percorre o nosso segundo for)
#2- (Linha = 1, coluna = [0] - irá percorrer o nosso for uma vez - elemento[linha][coluna] - elemento[1][0]
#3- (Linha = 2, coluna = [0, 1] - irá percorrer o nosso for duas vezes - elemento[linha][coluna] - elemento[2][0] & elemento[2,1]

# for linha in range(len(matriz)):
#     for coluna in range(linha):
#      elemento = matriz[linha][coluna]
#      print(elemento)

# Exemplo - printando elemento acima da diagonal: Tendo uma raiz 3 x 3 como exemplo, quando a linha for 0, nosso segundo for não será executado. Tendo linha como 1, nosso segundo for será executado uma vez e coluna terá como posição 0, logo elemento[coluna][linha] vale respectivamente elemento[0][1].

#Simulando tudo:
#1- (Linha = 0, coluna = 0 - Não percorre o nosso segundo for)
#2- (Linha = 1, coluna = [0] - irá percorrer o nosso for uma vez - elemento[coluna][linha] - elemento[0][1]
#3- (Linha = 2, coluna = [0 , 1] - irá percorrer o nosso for duas vezes - elemento[coluna][linha] - elemento[1][2]

# for linha in range(len(matriz)):
#     for coluna in range(linha):
#         elemento = matriz[coluna][linha] 
#         print(elemento)

#=========================================================================================================================================================#

#Uma matriz composta de uma matriz quadrada é basicamente a mesma matriz com as colunas nos lugares das linhas.

#Exemplo: | 1 , 2 , 3 |                  | 1 , 4 , 7 |
#         | 4 , 5 , 6 |        ===       | 2 , 5 , 8 |
#         | 7 , 8 , 9 |                  | 3 , 6 , 9 |


#Podemos simular a transposição de uma matriz quadrada fazendo a utilização de duas estruturas de repetição. A primeira para percorrer todas as linhas da nossa matriz e a segunda para percorrer o range da linha atual. Além disso, precisamos criar uma variavel auxiliar para que possamos armazenar os valores correspodentes as linhas, uma vez que elas receberão os valores das colunas e vice-versa.

# for linha in range(len(matriz)):
#     for coluna in range(linha):
#        #aux - Elemento atual da coluna
#        aux = matriz[linha][coluna]
#        #Elemento atual da coluna recebe Elemento atual da linha
#        matriz[linha][coluna] = matriz[coluna][linha]
#        #Elemento atual da linha
#        matriz[coluna][linha] = aux
#        print(matriz[linha])
#        print("=================")

#Dessa forma, utilizando range da linha atual no segundo for, trocamos apenas os elementos que precisam ser trocados. Os elementos da diagonal não precisam ser trocados e com essa forma, nosso algoritmo fica melhor


#=====================================================================================================================================================#


       
        
       
        








            
            

        


    










