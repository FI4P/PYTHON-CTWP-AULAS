'''lista = [4,2,5,7,5,6,1]
carros = ['uno','up','kombi','celta','mobi','kwid','gol']
indice_maior = 0
maior = lista[indice_maior]
for i in range(1,len(lista)):
    candidato = lista[i]
    print(f"Vou testar se {candidato} > {maior}")
    if candidato > maior:
        print(f"Vou trocar {maior} por {candidato}")
        maior = candidato
        indice_maior = i
print(f"O carro mais caro Ã© o {carros[indice_maior]} e vale R${lista[indice_maior]},00")


precos = [4000,2000,5000,7000,5000,6000,1000]
carros = ['uno','up','kombi','celta','mobi','kwid','gol']
potencia = [100,200,300,40,700,350,50]
ano = [2012,2010,2020,2021,2022,2023,2011]
sentenca = 'Nossos carros sÃ£o : '
for i in range(len(carros)):
    if i<len(carros)-1:
        sentenca+=f'{carros[i]}, '
    else:
        sentenca +=f'{carros[i]}.'
print(sentenca)
opcao = input("Qual carro vc deseja ver ? ")
while opcao not in carros:
    print("Deve er uma opÃ§Ã£o cadastrada!")
    opcao = input("Qual carro vc deseja ver ? ")
for i in range(len(carros)):
    print(f"estou testando se {carros[i]} == {opcao}")
    if carros[i] == opcao:
        indice = i
        break
print(i)
print(f"O carro {carros[indice]} custa {precos[indice]}, tem potencia {potencia[indice]}"
      f" e foi fabricado em {ano[indice]}")

'''
for i in range(10):
    i=0
import sys
print(sys.getsizeof([i for i in range(10000000)]))
print(sys.getsizeof(range(10000000)))