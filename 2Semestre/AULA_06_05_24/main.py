
##Worst way
arraySort = [7 , 5 , 4 , 1 , 3 , 2 ,6]

# arraySorted = []

# while arraySort:
#     menor_indice = 0
#     for number in range(len(arraySort)):
#        if(arraySort[number] < arraySort[menor_indice]):
#            menor_indice = number
#     numberMenor = arraySort.pop(menor_indice)
#     arraySorted.append(numberMenor)

# print(arraySorted)

def findMenor(lista):
    menor_indice = 0
    for number in range(len(lista)):
       if(lista[number] < lista[menor_indice]):
           menor_indice = number
    return menor_indice
    


# bad way

def selectionSort(lista):
    for i in range(len(lista)):
        delayIndex = findMenor(lista[i:])
        realIndex  = delayIndex + i
        aux = lista[realIndex]
        lista[realIndex] = lista[i]
        lista[i] = aux
    return lista

newLista = selectionSort(arraySort)
print(newLista)


# 