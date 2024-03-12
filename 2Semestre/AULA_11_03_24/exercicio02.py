# 2- Faça uma função que recebe de parâmetros as dimensões, (linhas e colunas), e retorna uma matriz preenchida de zeros com essas dimensões
import exercicio01

def generateMatriz(linha, coluna, value):
    matriz = []
    for i in range(linha):
        linha = []
        for j in range(coluna):
            linha.append(value)
        matriz.append(linha)
    return matriz

matriz = generateMatriz(4, 4, 1)

exercicio01.formatMatriz(matriz)


