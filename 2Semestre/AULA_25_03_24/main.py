#Aula 25_03_24

# dic = {
#     "nome": "Enzo Rodrigues",
#     "idade": 20,
#     "Profissao": "Dev full-stack",
#     "Hobbie": ["Jogar Video Game"]
# }


# #Exercicios 

# #Declare um dicionario:
# numeros = {}

# #Crie uma chave par e associe a uma lista vazia:
# numeros["par"] = []

# #Crie uma chave impar e associe a uma lista vazia:

# numeros["impar"] = []


# #Preencha cada chave com os numeros pares/impares de 0 a 10

# for numero in range(10):
#     if(numero % 2 == 0): 
#         numero["par"].append(numero)
#     else: 
#         numero["impar"].append(numero)

# print(numero)



#Cria um dicionario com 4 chaves: Nome de carros e seus preços:

# carros  = {
#     "nome": ["Celta", "T-Cross", "Civic", "Fox"],
#     "Valores": [10, 20, 30 , 50]
# }



#Print as chaves e seus conteúdos usando um for

# for key in carros.keys():
#     for indice in carros.keys():
#         print(carros[key])



# paises = {
#     "paises": ["Brasil", "New Zeland", "EUA", "Japão"],
#     "pop": [1000, 500, 5000, 700],
#     "pib": [3, 10, 5 , 8],
# }

# paises2 = {
#     "idh": [1, 2 ,3 , 4],
#     "pop": [1000, 2000, 3000, 54000],
#     "pib": [10, 20 , 20 , 30],
#     "CM": [1, 2 , 3 , 4]
# }


# for key in paises.keys():
#     if(key in paises2.keys()):
#         comum = {}
#         comum["key"] = paises[key]
#     else: 
#         incomum = {}
#         incomum[key] = paises[key]
        
# for key2 in paises2.keys():
#     if(key2 not in paises.keys()):
#         incomum[key2] = paises2[key2]
        


#Crie um objeto com chaves que representam as palavras contidas dentro da string e atribua a quantidade de vezes que ela se repete a cada chave.

# frase = "A aranha arranha a rã. A rã arranha a aranha.Nem a aranha arranha a rã. Nem a rã arranha a aranha."

# frase = frase.replace(".", "")

# frase = frase.lower()

# frase = frase.split(" ")

# print(frase)



# dicFrase = {}

# for palavra in frase:
#     if(palavra in dicFrase.keys()):
#         dicFrase[palavra] += 1
#     else:
#         dicFrase[palavra] = 1
        
# print(dicFrase)


# 1 - Cadastrar novo produto
# 2 - Remover um produto
# 3 - Atualizar infos de um produto
# 4 - Trazer todos as infos sobre um produto

peixes = {
  'Espécies': ['Tilápia', 'Baiacu', 'Tucunaré', 'Lambaqui' , 'Salmão', 'Bacalhau', 'Truta'],
  'Valor': [25, 30, 20, 101, 45, 60, 15],
  'Região': ['Piracicaba', 'Oceania', 'Amazonas', 'Águas Raras', 'Noruega', 'Portugal', 'Zona Leste'],
  'Estoque': [10, 23, 3, 31, 42, 12, 21],
  'Validade': [9, 2, 10, 11, 7, 6, 3]
}

menu = {
  'Códigos': ['1', '2', '3', '4', '0'],
  'Nomes': ['Cadastrar', 'Remover', 'Atualizar', 'Ver Informações', 'Sair']
}

def main():
  print('Bem-vindo a peixaria!')

  menu_id = selecionarMenu()
  while (int(menu_id) != 0):
    menu_id = selecionarMenu()

  print('Obrigado por utilizar nosso sistema!')

  return

def selecionarMenu():
  print('|----- MENU -----|')
  for i in range(len(menu['Códigos'])):
    print(f'{menu['Códigos'][i]} - {menu['Nomes'][i]}')

  return inputComValidacao('', menu['Códigos'])

def inputComValidacao(optionText, possibleOptions):
  option = input(optionText)
  while option not in possibleOptions:
    print('Opção inválida!')
    option = input(optionText)

  return option

main()
    
    

        

    
    
    
        