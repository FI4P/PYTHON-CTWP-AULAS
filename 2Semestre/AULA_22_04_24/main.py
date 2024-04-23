##Tratamento de erros em python

# lista = [1 , 2 ,3 ,4 ,5 ]

# while True:
#     try:
#         numero = int(input("Digite um número:"))
#         print(lista[numero])
#     #Podemos armazenar a excessão em uma variavel
#     except ValueError:
#         print("Digite um caracter númerico")
#     except IndexError as error:
#         print(f"O index deve ser entre 0 e {len(lista) - 1}")
#     except Exception as error:
#         print(error)
#     else:
#         print("Deu certo!")
#         break



# while True:
#     try:
#         numero1 = int(input("Digite um número:"))
#         numero2 = int(input("Digite um número:"))

#         result = numero1 / numero2
#     #Podemos armazenar a excessão em uma variavel
#     except ValueError:
#         print("Digite um caracter númerico")
#     except ZeroDivisionError:
#         print(f"Não é possivel dividir um número por zero!")
#     except Exception as error:
#         print(error)
#     else:
#         print(result)
#         break




# times = {
#     "são Paulo ": "Lixo",
#     "palmeiras": "Quem tem mais, tem 12!",
#     "santos" : "Lugar de peixe é dentro do aquario!",
#     "cortinas": "157",
# }





# while True:
#     try:
#         userInput = input("Digite o nome maior time do brasil:")
#         time = times[userInput]
#     except:
#         print("Time não encontrado!")
#     else:
#         print(f"Voce é um time: {time} ")
#         break



    