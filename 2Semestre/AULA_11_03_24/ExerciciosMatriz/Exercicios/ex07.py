from methods import methods

#7 -Uma matriz retangular da forma 5xN (5 linhas e N colunas) representa as notas de alunos em 5 provas. Cada linha é a nota de um aluno em uma das provas, enquanto cada coluna representa as 5 notas de um aluno somente. Media ponderada das notas.

pesoMateria = [1 , 2 , 3 , 2 , 1]

matrizNotasAlunos = [
    [ 10, 7], 
    [ 9 , 2], 
    [ 5 , 9], 
    [ 3 , 1], 
    [ 10, 0]
]

def mediaPonderada(listaPesos, matrizNotasAlunos):
  #Percorre os itens da lista de pesos e faz a soma
  somaPesos = 0
  for pesos in range(len(listaPesos)):
    somaPesos += listaPesos[pesos]
  
  mediaPonderadaAlunos = []
  #For para percorrer as colunas da matriz de Notas
  for coluna in range(len(matrizNotasAlunos[0])):
    somaNotaPeso = 0
    for linha in range(len(listaPesos)):
      somaNotaPeso += listaPesos[linha] * matrizNotasAlunos[linha][coluna]
    mediaPonderadaAlunos.append(somaNotaPeso/somaPesos)

  return mediaPonderadaAlunos

listaMedias = mediaPonderada(pesoMateria, matrizNotasAlunos)   
print(listaMedias)        




