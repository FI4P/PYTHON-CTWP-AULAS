from methods import methods

#7 -Uma matriz retangular da forma 5xN (5 linhas e N colunas) representa as notas de alunos em 5 provas. Cada linha é a nota de um aluno em uma das provas, enquanto cada coluna representa as 5 notas de um aluno somente. Media ponderada das notas.

pesoMateria = [1, 2, 3, 4, 5]

matrizNotasAlunos = [
    [ 10, 7], 
    [ 9 , 2], 
    [ 5 , 9], 
    [ 3 , 1], 
    [ 10, 0]
]

def mediaPonderada(listaPesos, matrizNotasAlunos):
    somaListaPesos = 0
    mediasPonderadas = []
    #Fazendo a soma dos pesos - Iremos utilizar para calcular a média
    for pesos in range(len(listaPesos)):
        somaListaPesos = somaListaPesos + listaPesos[pesos]
    
    #Percorre as colunas da matriz de notas
    for coluna in range(len(matrizNotasAlunos[0])):
        somaNotaPesos = 0
        # Percorre os elementos da lista de pesos
        for pesos in range(len(listaPesos)):
            somaNotaPesos += listaPesos[pesos] * matrizNotasAlunos[coluna][pesos]
        mediasPonderadas.append(f"Media Aluno {coluna}: {somaNotaPesos/somaListaPesos}")

    return mediasPonderadas

            


mediaPonderadaTotal = mediaPonderada(pesoMateria, matrizNotasAlunos)
print(mediaPonderadaTotal)




