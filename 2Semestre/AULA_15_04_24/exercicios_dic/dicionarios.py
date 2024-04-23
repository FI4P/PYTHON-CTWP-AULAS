def printDicByIndex (dic , index):
    for key in dic.keys():
        print(dic[key][index])
    return ""


# 1- Modifique o seguinte código para eliminar o uso de condicionais
'''
    resp = input("Diga oi ou tchau")
    if(resp == "oi"):
        print("olá")
    else:
        print("falou")
        
'''

# options = {
#     "oi": "Seja bem-vindo!",
#     "tchau": "Volte sempre!"
# }

# userInput = input("Digite uma das opções:[Oi | Tchau]")

# while userInput.lower() not in options.keys():
#     print("Opção inexistente!")
#     userInput = input("Digite uma das opções:[Oi | Tchau]")

# print(options[userInput.lower()])
    


# 2 - Traga ao usuário todas as inforamções sobre um carro de sua escolha

carros = {
    'nomes': ['celta', 'up', 'tcross'],
    'portas': [4 , 2 , 4],
    'preco': [1000, 2000, 3000],
}

# userInput = input("Digite o nome do carro:")

# while userInput.lower() not in carros['nomes']:
#     print("Carro não encontrado!")
#     userInput = input("Digite o nome do carro:")

# idCarro = 0
# for index in range(len(carros['nomes'])):
#     if(userInput == carros['nomes'][index]):
#         idCarro = index

# printDicByIndex(carros, idCarro)



#3 - Use o dicionario do item anterior para trazer todas as informações sobre o carro mais caro


# mostExpensive = 0
# for price in range(len(carros['preco'])):
#     if(carros['preco'][price] > mostExpensive):
#         mostExpensive = price

# printDicByIndex(carros, mostExpensive)



#4 - Use o dicionario do item anterior para trazer todas as informações sobre o carro mais barato

sheapestCar = 0

for index in range(len(carros['preco'])):
    if( sheapestCar < len(carros['preco'][index])):
        sheapestCar = index

printDicByIndex(carros, sheapestCar)


#5 - Pergunte ao usuário se ele gostaria de cadastrar um carro e implemente esta funcionalidade

options = {
   "sim": "1",
   "não": "2",
}


while True:
    userInput = input("Deseja cadastrar um carro em nossa base dados?").lower()

    while userInput not in options.keys():
        print("Opção inválida")
        userInput = input("Deseja cadastrar um carro em nossa base dados?").lower()

    if(options['sim'] == "1"):
        for key in carros.keys():
            









#6 - Pergunte ao usuário se ele gostaria de remover um carro e implemente esta funcionalidade


#7 - Escreva um codigo capaz e contar a quantidade de vezes que uma palavra aparece numa frase, por exemplo:


#8 - Escreva um código capaz de alterar números por extenso numa frase pelos caracteres correspondentes: Ex: Eu tenho aula na sala cinco , zero , dois -> eu tenho aula na sala 5 , 0 , 2 

#9 - Dados dois dicionarios, retorne uma lista com todas as chaves presentes em ambos

# 10 - Dados dois dicicionarios,  retorne uma lista com as chaves que não são comuns aos dois.


