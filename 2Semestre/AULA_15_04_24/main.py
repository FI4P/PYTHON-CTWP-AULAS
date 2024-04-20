#Resolução dos exercicios com explicação:

def dicPrintByIndex(index, dic):
    for key in dic.keys():
        print(f"{key}: {dic[key][index]}")
    return ""

def dicFormatedPrint(dic):
    for key in dic.keys():
        print(f"{key}: {dic[key]}")
    return ""

# 1- Modifique o seguinte código para eliminar o uso de condicionais
'''
    resp = input("Diga oi ou tchau")
    if(resp == "oi"):
        print("olá")
    else:
        print("falou")
        
'''

# answers = {
#     "oi": "Olá, tudo bem?",
#     "tchau": "Até mais!"
# }

# options = {
#     "1" : "Sair",
#     "2" : "Continuar"
# }



# while True:
#     userInput = input("Digite uma das opções possíveis: [ Oi | Tchau ]")
#     userInput = userInput.lower()
#     while userInput not in answers.keys():
#         userInput = input("Digite uma das opções possíveis: [ Oi | Tchau ]")
#         userInput = userInput.lower()
#     print(answers[userInput])
#     logout = input("Deseja continuar ou sair do sistema: [1 - Sair | 2 - Continuar]")
#     while logout not in options.keys():
#         logout = input("Deseja continuar ou sair do sistema: [1 - Sair | 2 - Continuar]")
#     if(options[logout].lower() == "sair"):
#         print(options[logout])
#         break
    
#Resolução: Utilizei dicionarios com chaves que represetavm as opções possiveis e seus respectivos valores. 
#Assim, adicionei uma estrutura de repetição while que verifica se o que o usuário inputou está ou não presente no dicionario
#Dessa forma, evitei a utilização das  verificações if and else.

'----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------'

# 2 - Traga ao usuário todas as inforamções sobre um carro de sua escolha. Defina um dicionário com carros e algumas informações e mande o usuário selecionar um carro.
    
# cars = {
#     "model" : ["celta", "tcross", "onix", "Up"],
#     "year"  : [2000 , 2023 , 2022 , 2019],
#     "price" : ["R$: 20.0000", "R$: 160.0000", "R$: 90.0000", "R$: 70.0000"],
#     "id"    : ["FWN-5542", "XLO-6542", "HWN-3532", "FOU-5782", ]
# }

# userInput = input("Selecione um do carros diponiveis:")
# userInput = userInput.lower()

# while userInput not in cars["model"]:
#     print("O carro digitado não foi encontrado!")
#     userInput = input("Selecione um do carros diponiveis:")
#     userInput = userInput.lower()

# index = 0
# for car in range (len(cars["model"])):
#     if(userInput == cars["model"][car]):
#         index = car
#         break
# dicPrintByIndex(index, cars)


#Resolucçao: Para resolver esse exercicio, primeiro verifiquei se o carro que o usuário digitou existia em nosso dicionario.
#Caso true, percorria o dicionario na posição de modelos até encontrar o carro digitado, salvando o index em uma variavel aux.
#Criei uma function que recebe dois argumentos (index, dic) para printar o objeto corretamente, acessando os valores de acordo com o index recuperado.

'----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------'

#3 - Use o dicionario do item anterior para trazer todas as informações sobre o carro mais caro

# cars = {
#     "model" : ["celta", "tcross", "onix", "Up"],
#     "year"  : [2000 , 2023 , 2022 , 2019],
#     "price" : [ 200000,  1600000,  900000, 700000 ],
#     "id"    : ["FWN-5542", "XLO-6542", "HWN-3532", "FOU-5782", ]
# }

# mostExpensiveIndex = 0

# for price in range(len(cars["price"])):
#     if(cars["price"][price] > cars["price"][mostExpensiveIndex]):
#          mostExpensiveIndex = price

# dicPrintByIndex(mostExpensiveIndex, cars)
    

#Resolucçao: Para resolver esse exercicio, primeiro defini o index do carro mais caro como 0;
#Fiz um for percorrendo a chave referente ao preço em meu dicionario e verifiquei se o valor do preco na posição atual era maior que a posição do index do carro mais caro, deinido anterioment;
#Caso True, o indice do carro mais caro recebe o indice atual;
#Criei uma function que recebe dois argumentos (index, dic) para printar o objeto corretamente, acessando os valores de acordo com o index recuperado.

'----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------'

#4 - Use o dicionario do item anterior para trazer todas as informações sobre o carro mais barato


# cars = {
#     "model" : ["celta", "tcross", "onix", "Up"],
#     "year"  : [2000 , 2023 , 2022 , 2019],
#     "price" : [ 200000,  1600000,  900000, 700000 ],
#     "id"    : ["FWN-5542", "XLO-6542", "HWN-3532", "FOU-5782", ]
# }

# cheapestIndex  = 0

# for price in range(len(cars["price"])):
#     if(cars["price"][price] < cars["price"][cheapestIndex]):
#         cheapestIndex = price

# dicPrintByIndex(cheapestIndex, cars)


#Resolucçao: Para resolver esse exercicio, primeiro defini o index do carro mais barato como 0;
#Fiz um for percorrendo a chave referente ao preço em meu dicionario e verifiquei se o valor do preco na posição atual era menort que a posição do index do carro mais bararo, deinido anteriomento;
#Caso True, o indice do carro mais barato recebe o indice atual;
#Criei uma function que recebe dois argumentos (index, dic) para printar o objeto corretamente, acessando os valores de acordo com o index recuperado.

'----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------'

#5 - Pergunte ao usuário se ele gostaria de cadastrar um carro e implemente esta funcionalidade

# registerCar = {
#     "1": "sim",
#     "2": "não",
# }
# while True:
#     userInput = input("Deseja cadastrar um carro em nossa base da dados? [1 - Sim | 2 - Não] ")

#     while userInput not in registerCar.keys():
#         userInput = input("Deseja cadastrar um carro em nossa base da dados?  [1 - Sim | 2 - Não]")


#     if (registerCar[userInput] == "sim"):
#         #Restante da logica para cadastrar um carro
#         for key in cars.keys():
#             userInput = input(f"Qual o {key}")
#             cars[key].append(userInput)
#     else:
#         print("Obrigado por utilizar nosso sistema!")
#         break
    
# dicFormatedPrint(cars)


#Resolucçao: Para cadastrar um carro em nosso dicionario, criei um looping com while True e nele peguntei se o usuer gostaria ou não cadastrar.
#Fiz mais um while para verificar se o que o usuário digitou como resposta existe como uma resposta válida.
#Caso exista, se a resposta for sim ele percorre as chaves do dicionario, adicionando em cada uma o valor correspondente.
#Criei uma function que recebe um argumento ( dic) para printar o objeto corretamente, acessando os valores de acordo com o index recuperado.

'----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------'

#6 - Pergunte ao usuário se ele gostaria de remover um carro e implemente esta funcionalidade

# deleteCar = {
#     "1" : "sim",
#     "2" : "não",
# }

# cars = {
#     "model" : ["celta", "tcross", "onix", "Up"],
#     "year"  : [2000 , 2023 , 2022 , 2019],
#     "price" : [ 200000,  1600000,  900000, 700000 ],
#     "id"    : ["FWN-5542", "XLO-6542", "HWN-3532", "FOU-5782", ]
# }

# while True:
#     userInput = input("Deseja remover um carro em nossa base da dados? [1 - Sim | 2 - Não] ")

#     while userInput not in deleteCar.keys():
#         userInput = input("Deseja remover um carro da nossa base da dados?  [1 - Sim | 2 - Não]")

#     if(deleteCar[userInput] == "sim"):
#         index = 0
#         inputCar = input("Qual carro gostaria de deletar?")
       
#         while inputCar not in cars["model"]:
#             print("Carro inexistente em  nossa base de dados!")
#             inputCar = input("Qual carro gostaria de deletar?")
#         for car in range(len(cars["model"])):
#             if(cars["model"][car] == inputCar.lower()):
#                 index = car
#         for key in cars.keys():
#             cars[key].pop(index)
#         print("Carro removido com sucesso!")
#         dicFormatedPrint(cars)
#     else:
#         print("Obrigado por utilizar nosso sistema")
#         break

#Resolucçao: Para remover um carro em nosso dicionario, criei um looping com while True e nele peguntei se o usuer gostaria ou não remover.
#Fiz mais um while para verificar se o que o usuário digitou como resposta existe como uma resposta válida.
#Caso exista, se a resposta for sim ele percorre a chave que contém o nome dos carros existentes e caso seja igual ao input dado, recupera o index.
#Utilizo o metodo pop() para remover o item com base no index.
#Criei uma function que recebe um argumento ( dic) para printar o objeto corretamente, acessando os valores de acordo com o index recuperado.
'----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------'
#7 - Escreva um codigo capaz e contar a quantidade de vezes que uma palavra aparece numa frase, por exemplo:
# def countPrhase(word):
#     count = 0
#     prhase = "A aranha arranha a rã. A rã arranha a aranha. Nem a aranha arranha a rã. Nem a rã arranha a aranha."
#     prhase = prhase.replace(".", "").lower()
#     print(prhase)

#     arrayPrhase = prhase.split(" ")

#     if(not (word not in arrayPrhase)):
#         for iWord in range(len(arrayPrhase)):
#             if(arrayPrhase[iWord] == word):
#                 count = count + 1
#     else:
#         print("A palavra não aparece nenhuma vez!")
#     print(f"Contador: {count}")
        
# countPrhase("a")

#Resolucçao: Criei uma função que recebe como argumento a palavra que gostariamos de procurar.
#Apos isso, utilizo o método replace para remover os pontos por espaços em brancos. além de utilizar o lower() para melhor tratamento de erros.
#Utilizo o método split() para transformar a string em um array, onde cada posição representa uma palavra.
#Faço uma verificação para ver se a palavra passada como parâmetro está na frase. 
#Caso a palavra esteja, percorro o array e verifico se a palavra atual é igual a palavra passada como parâmetro. Caso true, adiciono ao contador.


'----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------'

#8 - Escreva um código capaz de alterar números por extenso numa frase pelos caracteres correspondentes: Ex: Eu tenho aula na sala cinco , zero , dois -> eu tenho aula na sala 5 , 0 , 2 

# numbers = {
#     "um": "1",
#     "dois": "2",
#     "três": "3",
#     "quatro": "4",
#     "cinco": "5",
#     "seis": "6",
#     "sete": "7",
#     "oito": "8",
#     "nove": "9",
#     "dez": "10"
# }

# symbols = [".", ","]
# prhase = "Eu tenho aula na sala um, dois, três, quatro, cinco, seis, sete, oito, nove, dez."
# for symbol in symbols:
#     prhase = prhase.replace(symbol, "")

# arrayPhrase =  prhase.split(" ")

# for index in range(len(arrayPhrase)):
#     if(arrayPhrase[index] in numbers.keys()):
#         arrayPhrase[index] = numbers[arrayPhrase[index]]
# newPrhase =  " ".join(arrayPhrase)
# print(newPrhase)


#Resolucçao: Criei um dicionario com chaves equivalentes a numeros por extenso e nelas, armazenei o valor corresponde.
#Removi todos os pontos existentes em nossa frase, para facilitar a manipulação.
#Criei uma variavel que recebeu um array com todas as palavras da string.
#Após isso, fiz um looping para percorrer todos os itens do array e verifiquei se o elemento atual exisita como uma chave em meu dicionario.
#Caso true, o elemento atual recebe o valor do dicionario na chave. Para acessar a chave, usei o elemento atual do array.

'----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------'

#9 - Dados dois dicionarios, retorne uma lista com todas as chaves presentes em ambos

dicionario1 = {
    "chave1": "valor1",
    "chave2": "valor2",
    "chave3": "valor3",
    "chave4": "valor4",
    "chave6": "valorD"
}

dicionario2 = {
    "chave2": "valorA",
    "chave3": "valorB",
    "chave5": "valorC",
    "chave6": "valorD"
}

# Inicializando listas para armazenar as chaves comuns e não comuns
commumKeys = []
uncommunKeys = []

# Verificando chaves comuns
for key in dicionario1.keys():
    if key in dicionario2:
        commumKeys.append(key)
    else:
        uncommunKeys.append(key)

# Verificando chaves exclusivas do segundo dicionário
for key2 in dicionario2.keys():
    if key2 not in dicionario1:
        uncommunKeys.append(key2)

print("Chaves comuns:", commumKeys)
print("Chaves não comuns:", uncommunKeys)

    
'----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------'
    
# 10 - Dados dois dicicionarios,  retorne uma lista com as chaves que não são comuns aos dois.

dicionario1 = {
    "chave1": "valor1",
    "chave2": "valor2",
    "chave3": "valor3",
    "chave4": "valor4",
    "chave6": "valorD"
}

dicionario2 = {
    "chave2": "valorA",
    "chave3": "valorB",
    "chave5": "valorC",
    "chave6": "valorD"
}

# Inicializando listas para armazenar as chaves comuns e não comuns
commumKeys = []
uncommunKeys = []

# Verificando chaves comuns
for key in dicionario1.keys():
    if key in dicionario2:
        commumKeys.append(key)
    else:
        uncommunKeys.append(key)

# Verificando chaves exclusivas do segundo dicionário
for key2 in dicionario2.keys():
    if key2 not in dicionario1:
        uncommunKeys.append(key2)

print("Chaves comuns:", commumKeys)
print("Chaves não comuns:", uncommunKeys)



















