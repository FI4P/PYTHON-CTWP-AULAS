def formatMatriz(matriz):
    for i in range(len(matriz)):
         print(matriz[i])
    return

def generateMatriz(linha, coluna, value):
    matriz = []
    for i in range(linha):
        linha = []
        for j in range(coluna):
            linha.append(value)
        matriz.append(linha)
    return matriz

