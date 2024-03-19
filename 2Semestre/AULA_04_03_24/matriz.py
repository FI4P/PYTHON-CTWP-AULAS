import matplotlib.pyplot as plt

def formatMatriz(matriz):
    for i in range (len(matriz)):
        print(matriz[i])
    return


def geraMatriz(linhas, colunas , num = 0):
    matriz =[]

    for i in range(linhas):
        linha = []
        for j in range(colunas):
            linha.append(num)
        matriz.append(linha)
    print()
    return matriz


matriz = geraMatriz(8   ,8 , 1)



# for i in range (len(matriz)):
#    for j in range(len(matriz[i])):
#       if((i % 2 == 0 and j % 2 == 0) or (i % 2 != 0 and j % 2 != 0)):
#         matriz[i][j] = 1 
#       else:
#          matriz[i][j] = 0

# for i in range(len(matriz)):
#     for j in range (len(matriz[i])):
#      if (i + j) % 2  == 0:
#          matriz[i][j] = 1


# for i in range (len(matriz)):
#     matriz[i][i] = 0


# for i in range(len(matriz)):
#     for j in range (len(matriz[i])):
#      if (i + j)  ==  len(matriz) - 1:
#          matriz[i][j] = 0

# for i in range(len(matriz)):
#     matriz[i][i] = 0
#     matriz[i][len(matriz) - 1 -i] = 0 


# for i in range(len(matriz)):
#     for j in range (i):
#         matriz[j][i] = 0


# for i in range(len(matriz)):
#     for j in range(len(matriz)):
#         matriz[i][j] = i


# formatMatriz(matriz)

# plt.imshow(matriz, cmap="hot")
# plt.figure()    

# for i in range(len(matriz)):
#     for j in range(i):
#         aux = matriz[i][j]
#         matriz[i][j] = matriz[j][i]
#         matriz[j][i] = aux




# formatMatriz(matriz)



# pesos = [1 , 2 , 3 , 2 , 1]
# somaPesos = 0
# for i in range (len(pesos)):
#     somaPesos = somaPesos + pesos[i]

# notas = [[10, 7], [9,2], [5,9], [3, 1], [10, 0]]

# media = []

# for j in range(len(notas[0])):
#     soma = 0
#     for i in range(len(pesos)):
#         soma += pesos[i] * notas[i][j]
#     media.append(soma/somaPesos)

# print(media)


# circulo = geraMatriz(1000, 1000)
# for i in range(len(circulo)):
#     for j in range(len(circulo)):
#         if((i-len(circulo)//2)**2 + (j-len(circulo)//2)**2 < (len(circulo)//2)**2):
#             circulo[i][j] = i+j



# plt.imshow(circulo)
# plt.show()



