arraySort = [7 , 5 , 4 , 1 , 3 , 2 ,6]

arraySorted = []

while arraySort:
    menor_indice = 0
    for number in range(len(arraySort)):
       if(arraySort[number] < arraySort[menor_indice]):
           menor_indice = number
    numberMenor = arraySort.pop(menor_indice)
    arraySorted.append(numberMenor)

print(arraySorted)

