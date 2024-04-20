#Resolução dos exercicios com explicação:


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


def dicPrint(index, dic):
    for key in dic.keys():
        print(f"{key}: {dic[key][index]}")
    return ""
        
        
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
# dicPrint(index, cars)


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

# dicPrint(mostExpensiveIndex, cars)
    

#Resolucçao: Para resolver esse exercicio, primeiro defini o index do carro mais caro como 0;
#Fiz um for percorrendo a chave referente ao preço em meu dicionario e verifiquei se o valor do preco na posição atual era maior que a posição do index do carro mais caro, deinido anterioment;
#Caso True, o indice do carro mais caro recebe o indice atual;
#Criei uma function que recebe dois argumentos (index, dic) para printar o objeto corretamente, acessando os valores de acordo com o index recuperado.

'----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------'

#4 - Use o dicionario do item anterior para trazer todas as informações sobre o carro mais barato


cars = {
    "model" : ["celta", "tcross", "onix", "Up"],
    "year"  : [2000 , 2023 , 2022 , 2019],
    "price" : [ 200000,  1600000,  900000, 700000 ],
    "id"    : ["FWN-5542", "XLO-6542", "HWN-3532", "FOU-5782", ]
}

cheapestIndex  = 0

for price in range(len(cars["price"])):
    if(cars["price"][price] < cars["price"][cheapestIndex]):
        cheapestIndex = price

dicPrint(cheapestIndex, cars)


#Resolucçao: Para resolver esse exercicio, primeiro defini o index do carro mais barato como 0;
#Fiz um for percorrendo a chave referente ao preço em meu dicionario e verifiquei se o valor do preco na posição atual era menort que a posição do index do carro mais bararo, deinido anteriomento;
#Caso True, o indice do carro mais barato recebe o indice atual;
#Criei uma function que recebe dois argumentos (index, dic) para printar o objeto corretamente, acessando os valores de acordo com o index recuperado.

'----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------'

#5 - Pergunte ao usuário se ele gostaria de cadastrar um carro e implemente esta funcionalidade

registerCar = {
    "1": "sim",
    "2": "não",
}

userInput = input("Deseja cadastrar um carro em nossa base da dados? [1 - Sim | 2 - Não] ")

while userInput not in registerCar.keys():
    print("Selecione uma das opções: [1 - Sim | 2 - Não]")
    userInput = input("Deseja cadastrar um carro em nossa base da dados?")

while (registerCar[userInput] == "sim"):
    #Restante da logica para cadastrar um carro
    
    
























'----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------'

