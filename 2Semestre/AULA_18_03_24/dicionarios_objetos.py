#Um dicionario em python basicamente é um objeto em outras lingaugens. É construído da mesma forma, chave: valor

#Declarando um objeto em python
dicionario = {
    "chave": "valor"
}

#Acessando valores de um objeto em py

pessoa ={
    "nome" : "Enzo",
    "idade": 20,
    "Profissao": "DEV"
}

#Para acessar, basta colocar o objeto["chave".
nomePessoa = pessoa["nome"]

#Criand uma chave que não existe para esse objeto

pessoa["novaChave"] = "Minha nova chave"



#Desafio 01

# poligonos = {
#     "3":"TRI",
#     "4":"QUA",
#     "5":"PEN",
#     "6":"HEX"
# }


# resposta = input("Digita a quantidade de lados:")

# print(poligonos[resposta])


#Desafio 02

# objeto = {
    
# }

# objeto["pares"] = []
# objeto["impares"] = []

# for count in range(101):
#     if(count % 2== 0): objeto["pares"].append(count)
#     else:objeto["impares"].append(count)


# print(objeto)

# #Desafio 03


numeros = {
    "zero": 0,
    "um": 1,
    "dois": 2,
    "dois": 2,
    "tres": 3,
    "quatro": 4,
    "cinco": 5,
    "seis": 6,
    "sete": 7,
    "oito": 8,
    "nove": 9,
    

}

frase = "Meu numero é um dois tres quatro cinco seis sete oito nove"

frase.lower()
frase = frase.split(" ")

for elemento in range(len(frase)):
    if(frase[elemento] in numeros.keys()):
        frase[elemento] = str(numeros[frase[elemento]])

frase = " ".join(frase)
print(frase)

