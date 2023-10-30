'''1-	FaÃ§a um programa que peÃ§a uma nota, entre zero e dez. Mostre uma mensagem
 caso o valor seja invÃ¡lido e continue pedindo atÃ© que o usuÃ¡rio informe um valor vÃ¡lido.'''

#1
'''
nota = int(input("Diga sua nota : "))
while nota<0 or nota>10:# not (nota>0 and nota<10)
    print("Tem que ser entre 0 e 10!")
    nota = int(input("Diga sua nota : "))
print("Parabens")

nota = int(input("Diga sua nota : "))
while not (nota>0 and nota<10):
    print("Tem que ser entre 0 e 10!")
    nota = int(input("Diga sua nota : "))
print("Parabens")
'''
#2
'''
2-	FaÃ§a um programa que leia e valide as seguintes informaÃ§Ãµes:
a.	Nome: maior que 3 caracteres;
b.	Idade: entre 0 e 150;
c.	SalÃ¡rio: maior que zero;
d.	Sexo: 'f' ou 'm';
e.	Estado Civil: 's', 'c', 'v', 'd';

nome = input("Diga seu nome : ")
while len(nome)<3:
    print("Tem que ter no mÃ­nimo 3 caracteres!")
    nome = input("Diga seu nome : ")

idade = int(input("Diga sua idade : "))
while idade<0 or idade>150:
    print("A idade deve ser entre 0 e 150!")
    idade = int(input("Diga sua idade : "))

salario = int(input("Diga seu salario : "))
while salario<0:
    print("Voce Ã© pobre mas nem tanto")
    salario = int(input("Diga seu salario : "))

sexo = input("Diga seu sexo : ")
while not (sexo == 'f' or sexo == 'm'):#sexo !='f' and sexo != 'm'
    print("f ou m")
    sexo = input("Diga seu sexo : ")


es = input("Diga seu estado civil : ")
while not (es == 's' or es == 'c' or es == 'v' or es == 'd'):#sexo !='f' and sexo != 'm'
    print("s c v ou d")
    es = input("Diga seu estado civil : ")

import matplotlib.pyplot as plt

a = 80000
pop_a = [a]
b = 200000
pop_b = [b]
t=0
tempo = [t]
while a<b:
    a*=1.03
    b*=1.015
    t+=1
    pop_b.append(b)
    pop_a.append(a)
    tempo.append(t)
plt.plot(tempo,pop_a,label='A')
plt.legend()
plt.plot(tempo,pop_b,label = 'B')
plt.grid()
plt.show()
print(t)


i=0
soma = 0
while i<5:
    num = float(input(f"Diga o {i+1}Âº nÃºmero : "))
    soma += num
    i+=1
print(f"A soma dos numeros que vc digitou Ã© {soma} e a mÃ©dia Ã© {soma/i}")
'''

#5
'''5-	FaÃ§a um programa que receba dois nÃºmeros inteiros e gere os nÃºmeros 
inteiros que estÃ£o no intervalo compreendido por eles.

a = input("Diga um nÃºmero : ")
while not a.isnumeric():
    print("Tem que ser um int!")
    a = input("Diga um nÃºmero : ")
a = int(a)
b = input("Diga um nÃºmero : ")
while not b.isnumeric():
    print("Tem que ser um int!")
    b = input("Diga um nÃºmero : ")
b = int(b)

while a<b:
    print(a)
    a+=1

while b<a:
    print(b)
    b+=1


6-	FaÃ§a um programa que leia um nome de usuÃ¡rio e a sua senha e nÃ£o aceite a senha 
igual ao nome do usuÃ¡rio, mostrando uma mensagem de erro e voltando a pedir as informaÃ§Ãµes.

nome = input("Diga seu nome : ")
senha = input("Diga sua senha : ")
while nome == senha:
    nome = input("Diga seu nome : ")
    senha = input("Diga sua senha : ")

#tabuada
num = 1
while num <= 10:
    print(f"A tabuada do {num} Ã© :")
    i=1
    while i<=10:
        print(f"{num} * {i} = {num*i}")
        i+=1
        -
    if num == 5:
        break
    num += 1

8-	A sÃ©rie de Fibonacci Ã© formada pela sequÃªncia 1,1,2,3,5,8,13,21,34,55,...
FaÃ§a um programa capaz de gerar a sÃ©rie atÃ© o nâˆ’Ã©simo termo.

a = 1
b = 1
i = 0
n = int(input("Qts fibos vc quer ???"))
print(a)
print(b)
while i < n:
    c = a+b
    a = b
    b = c
    print(c)
    print(c/a)
    #1.61803398875
    i+=1

fat = 1
i = 1
n = int(input("Diga um numero : "))
print(f"O fatorial de {n} Ã© : ")
sentenca = ''
while i<=n:
    fat*=i
    if i<n:
        sentenca+=str(n-i+1)+'*'
    else:
        sentenca+=str(n-i+1)
    i+=1
print(f"{sentenca} = {fat}")

a = 1
b = 1
qtd = 0
n = int(input("Qts fibos vc quer ???"))
print(a)
print(b)
while qtd < n:
    c = a+b
    a = b
    b = c
    qtd+=1
    i = 2
    num = c
    while True:
        if num==2:
            print("ta bom vai o dois Ã© primo")
            break
        if num % i == 0:
            print(f"{num} nÃ£o Ã© primo!")
            break
        elif i>num**0.5:
            print(f"{num} Ã© primo!")
            break
        i+=1

salario = 1000
ano = 1996
porcentagem_inicial = 1.5/100
i = 0
while ano + i <2002:
    porcentagem = 2**i * porcentagem_inicial
    print(f"No ano de {ano+i} o aumento percentual Ã© de {porcentagem}")
    salario*=1+porcentagem
    i+=1
print(salario)

primeiro = 0
segundo = 0
terceiro = 0
quarto = 0
while True:
    num = input("Diga um numero : ")
    while not num.isnumeric():
        num = input("Diga um numero : ")
    if num>0 and num < 25:
        primeiro +=1
    elif num>25 and num < 50:
        segundo +=1
    elif num>50 and num < 75:
        terceiro +=1
    elif num>75 and num < 100:
        quarto +=1
    elif num<0:
        break
'''

primeiro = 0
segundo = 0
terceiro = 0
quarto = 0
nulo = 0
branco = 0
total = 0
while True:
    num = input("Diga seu voto - 1,2,3,4. Para sair, 0 e nulo/branco 5 e 6 respectivamente : ")
    while not (num == '0' or num == '1' or num == '2' or num == '3'or num =='4' or num == '5'
               or num == '6'):
        num = input("Diga seu voto - 1,2,3,4. Para sair, 0 e nulo/branco 5 e 6 respectivamente : ")
    if num == '1':
        primeiro +=1
    elif num == '2':
        segundo +=1
    elif num == '3':
        terceiro +=1
    elif num == '4':
        quarto +=1
    elif num == '5':
        nulo +=1
    elif num == '6':
        branco +=1
    else:
        break
    total += 1

print(f"O total de votos foi de {total}")
print(f"O primeiro recebeu {primeiro}")
print(f"O segundo recebeu {segundo}")
print(f"O terceiro recebeu {terceiro}")
print(f"O quarto recebeu {quarto}")
print(f"O numero de nulos foi {nulo}")
print(f"O numero de votos em branco foi {branco}")
print(f"A porcentagem de nulos foi de {nulo*100/total:.2f}%")
print(f"A porcentagem de brancos foi de {branco*100/total:.2f}%")