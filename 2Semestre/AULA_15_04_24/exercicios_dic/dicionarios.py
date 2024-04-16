# 1- Modifique o seguinte código para eliminar o uso de condicionais
'''
    resp = input("Diga oi ou tchau")
    if(resp == "oi"):
        print("olá")
    else:
        print("falou")
        
'''
resposta = {
    "oi": "olá",
    "tchau": "Falou"
}

userInput = input("Digite oi ou tchau") 

while userInput not in resposta.keys():
    userInput = input("Digite oi ou tchau") 

print(resposta[userInput])
    


# 2 - Traga ao usuário todas as inforamções sobre um carro de sua escolha>

carros = {
    'nomes': ['Celta', 'Up', 'T-cross'],
    'portas': [4 , 2 , 4],
    'preco': [1000, 2000, 3000],
}

#3 - Use o dicionario do item anterior para trazer todas as informações sobre o carro mais caro


#4 - Use o dicionario do item anterior para trazer todas as informações sobre o carro mais barato

#5 - Pergunte ao usuário se ele gostaria de cadastrar um carro e implemente esta funcionalidade


#6 - Pergunte ao usuário se ele gostaria de remover um carro e implemente esta funcionalidade


#7 - Escreva um codigo capaz e contar a quantidade de vezes que uma palavra aparece numa frase, por exemplo:


#8 - Escreva um código capaz de alterar números por extenso numa frase pelos caracteres correspondentes: Ex: Eu tenho aula na sala cinco , zero , dois -> eu tenho aula na sala 5 , 0 , 2 

#9 - Dados dois dicionarios, retorne uma lista com todas as chaves presentes em ambos

# 10 - Dados dois dicicionarios,  retorne uma lista com as chaves que não são comuns aos dois.


