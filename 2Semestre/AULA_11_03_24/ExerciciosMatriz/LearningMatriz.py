# Matriz em PY nada mais é do que uma lista PAI que contém sublistas FILHO

#Cada sublista dentro de uma Lista PAI representa uma linha da matriz

#Cada elemento da sublista irá representar a coluna da matriz.

# Representando uma matriz: [  [ col-00 , col-01 , col-02 ], [ col-10 , col-11 , col-12 ] , [ col-20 , col-21 , col22 ] ]

#Observando, vemos que as linhas são o conjunto todo da sublista e as colunas são representadas pelos elementos da sublista.

#É importante observar que os índices das colunas sempre começam em zero em uma matriz. Portanto, o índice final das colunas será sempre tamanhoTotalMatriz - 1.

#Montando uma matriz em py:

# matriz = [ [ "col 0,0", "col 0,1", "col 0,2"] , ["col 1,0", "col 1,2", "col 1,2"] , ["col 2,0", "col 2,1", "col 2,2"] ]

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


matriz = [ [ 0 , 0 , 0 ] , [ 0 , 0 , 0] , [0 , 0 , 0] ]

for linha in range(len(matriz)):
    resultado =  "Não Quadrada" if len(matriz[linha]) !=  len(matriz) else "Quadrada"    

#==========================================================================================================================#

#A diagonal principal de uma matriz é definida pelo indice da coluna ser igual ao indice da coluna

#Podemos descobrir a diagonal de uma matriz utilizando um for ou dois com uma verificação.

#Exemplo: Printando os elementos da diagonal de uma matriz
termo = False 
for linha in range(len(matriz)):
    if(termo): 
        print(matriz[linhaAnteriror]) 
        termo = False
    
    for coluna in range(len(matriz[linha])):    
        # Se indice linha == indice coluna (elemento diagonal)
        if(linha == coluna):
         matriz[linha][coluna] = 1
         linhaAnteriror = linha
         termo = True







            
            

        


    










