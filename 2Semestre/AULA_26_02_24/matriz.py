

def formatMatriz(matriz):
    for i in range (len(matriz)):
        print(matriz[i])
    return

matriz = [[1, 2, 3, 4], [4, 5,6, 4], [7 ,8 ,9, 4],  [7 ,8 ,9, 4]]



# Zerando todos os itens da nossa matrizs

# for i in range(len(matriz)):   
#     for j in range(len(matriz[i])):
#         matriz[i][j] = 0;


# for i in range(len(matriz)):
#     for j in range(len(matriz[i])):
#         if(i == j):
#             matriz[i][j] = 1
#         else:
#             matriz[i][j]= 0



# for i in range(len(matriz)):
#     for j in range(len(matriz[i])):
#         if(i == j):
#             matriz[i][j] = 1
#         else:
#             matriz[i][j]= 0
        



for i in range (len(matriz)):
   for j in range(len(matriz[i])):
      if((i % 2 == 0 and j % 2 == 0) or (i % 2 != 0 and j % 2 != 0)):
        matriz[i][j] = 1 
      else:
         matriz[i][j] = 0

formatMatriz(matriz)
    



       