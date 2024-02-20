# notas = [8, 9 , 10, 7 , 19 , 20 , 28]

# # Fatiando uma lista

# # Selecionando o item de indice 01
# print(notas[1])

# #Invertendo os indices, puxa o ultimo indice
# print(notas[-1])

# #A partir do primeiro indice até o ultimo
# print(notas[1:])

# #A partir do penultimo elemento até o ultimo
# print(notas[-2:])

# # A partir do penultimo indice até o primeiro
# print(notas[:-2])

# #Copia do array para uma nova varivel

# copiaArray = notas[:]



# #Fatiando uma lista
# print(notas[2:4]) #Parte do indice dois e vai até o 4, sem pegar o ultimo

# print(notas[2:4:2]) #Parte do indice dois e vai até o 4, sem pegar o ultimo de dois em dois


options = ["1", "2", "3"]
fila = []






while (True):  
    userOption = input("Qual opção deseja escolher?")

    while(userOption not in options):
        print("1 - Adicionar demanda")
        print("2 - Executar demanda")
        print("3 - Executar demanda")
        userOption = input("Qual opção deseja escolher?")


    if(userOption == "1"):
        demanda = input("Digite a sua demanda")
        fila.append(demanda)
    
        print(f"Demanda adicionada na pocisão {fila.index(demanda)}")

    if(userOption == "2"):
        fila.pop()
        print(fila)


    if(userOption == "3"):
        break







    











