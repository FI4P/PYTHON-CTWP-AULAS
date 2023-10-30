'''lista = [0,1,2,3,4,5,6,7]
print(lista)
for i in range(len(lista)//2):
    ultimo_indice = len(lista) - 1
    aux = lista[i]
    lista[i] = lista[ultimo_indice - i]
    lista[ultimo_indice - i] = aux
    print(lista)

lista = [0,1,2,3,4,5,6,7]
for i in range(len(lista)):
    for j in range(len(lista)-1-i):
        aux = lista[j]
        lista[j] = lista[j + 1]
        lista[j+1] = aux
        print(lista)
    print()
'''
import numba


def forca_opcao(msg,lista_opcoes):
    resposta = input(msg)
    print(lista_opcoes)
    while not resposta in lista_opcoes:
        resposta = input(msg)
    return resposta
def media(numeros):
    soma = 0
    for elem in lista:
        soma += elem
    soma/=len(lista)
    return soma

'''lista = ['sim','nÃ£o']
resposta = forca_opcao("Diga sim ou nÃ£o : ",['sim','nÃ£o'])
print(resposta)
resposta = forca_opcao("tinto seco ou suave ? ",['tinto','seco','suave'])
print(resposta)

lista = [10,20,30,40,50]
for i in range(len(lista)):
    print(f"lista[{i}] = {lista[i]}")
for elem in lista:
    print(elem)

#faÃ§a uma funÃ§Ã£o que recebe o salario como parÃ¢metro e retorna o desconto em reais
#faÃ§a uma funÃ§Ã£o que recebe uma lista e retorna a quantidade de numeros pares ali dentro
#faÃ§a uma funÃ§Ã£o que recebe uma lista e retorna a quantidade de numeros impares ali dentro
#faÃ§a uma funÃ§Ã£o que recebe uma lista contendo nomes de pessoas,
# pergunte ao usuario quantas pessoas ele quer cadastrar e cadastre-as
#faÃ§a uma funÃ§Ã£o que retorne o maior valor de uma lista

def calcula_desconto(salarios):
    descontos = []
    for salario in salarios:
        if salario<=1903:
            aliquota = 0
        elif salario <=2826:
            aliquota = 0.075
        elif salario <= 3751:
            aliquota = 0.15
        elif salario <= 4664:
            aliquota = 0.225
        else:
            aliquota = 0.275
        descontos.append(aliquota*salario)
    return descontos
valores_salarios = [1000,2000,3000,4000,5000]
valores_descontos = calcula_desconto(valores_salarios)
for i in range(len(valores_salarios)):
    print(f"voce receberÃ¡ R${valores_salarios[i] - valores_descontos[i]}")
'''
#faÃ§a uma funÃ§Ã£o que recebe o salario como parÃ¢metro e retorna o desconto em reais
#faÃ§a uma funÃ§Ã£o que recebe uma lista e retorna a quantidade de numeros pares ali dentro
#faÃ§a uma funÃ§Ã£o que recebe uma lista e retorna a quantidade de numeros impares ali dentro
#faÃ§a uma funÃ§Ã£o que recebe uma lista contendo nomes de pessoas,
# pergunte ao usuario quantas pessoas ele quer cadastrar e cadastre-as
#faÃ§a uma funÃ§Ã£o que retorne o maior valor de uma lista
def conta_impar(lista):
    qtd = 0
    for num in lista:
        if num%2 == 1 :
            qtd+=1
    return qtd
def conta_par(lista):
    qtd = 0
    for num in lista:
        if num%2 ==0 :
            qtd+=1
    return qtd
def cadastra_nome(lista_nomes):
    qtd = checa_numero("Diga a qtd de pessoas a serem cadastradas : ")
    for i in range(qtd):
        nome = input(f"Diga o {i+1}Âº nome : ")
        lista_nomes.append(nome)
    return lista_nomes
def checa_numero(msg):
    num = input(msg)
    while not num.isnumeric():
        print("Deve ser um nÃºmero!")
        num = input(msg)
    return int(num)
nomes = ['danilo','jÃ³','tranquilo','thicas']
nomes = cadastra_nome(['vaporub','strepsirs'])
print(nomes)