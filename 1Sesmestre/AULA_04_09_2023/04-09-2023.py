'''
salario = int(input("Diga seu salÃ¡rio : "))
if salario <= 1903.98:
    aliquota = 0
elif salario <= 2826.65:
    aliquota = 7.5/100
elif salario <= 3751.05:
    aliquota = 15/100
elif salario <= 4664.68:
    aliquota = 22.5/100
else:
    aliquota = 27.5/100
desconto = aliquota*salario
print(f"Seu salario final Ã© de R${salario - desconto}")

letra = input("Diga uma letra : ")
if letra == 'a' or letra == 'e' or letra == 'i' or letra == 'o' or letra == 'u':
    print(f'{letra} Ã© uma vogal')
else:
    print(f'{letra} Ã© uma consoante')

letra = input("Diga uma letra : ")
vogal = 'vogal'
vogal_ou_consoante = 'consoante'
if letra == 'a':
    vogal_ou_consoante = vogal
elif letra == 'e':
    vogal_ou_consoante = vogal
elif letra == 'i':
    vogal_ou_consoante = vogal
elif letra == 'o':
    vogal_ou_consoante = vogal
elif letra == 'u':
    vogal_ou_consoante = vogal
print(f"{letra} Ã© {vogal_ou_consoante}")

num1 = float(input('Diga um valor : '))
num2 = float(input('Diga outro valor : '))
if num1>num2:
    print(f"{num1} > {num2}")
else:
    print(f"{num2} > {num1}")

ano = int(input('Diga seu ano de nascimento : '))
if ano <= 2007:
    print("Pode votar!!")
else:
    print("nÃ£o pode votar!")

senha = 1234
tentativa = int(input("Diga sua senha : "))
if senha == tentativa:
    print('ACESSO PERMITIDO')
else:
    print('ACESSO NEGADO')

qtd = int(input("Qts maÃ§Ã£s vc vai comprar ? "))
preco = 0.25
if qtd < 12:
    preco = 0.3
valor_total = preco*qtd
print(f"Sua compra custou R${valor_total} ")

altura = float(input("Diga sua altura : "))
sx = input("Diga seu sexo (f/m): ")
if sx == 'f':
    peso = 62.1*altura - 44.7
else:
    peso = 72.7*altura - 58
print(f"Seu peso ideal Ã© {peso:.2f}")

lados = int(input("Qts lados vc tem : "))
if lados == 3:
    print('Triangulo')
elif lados == 4:
    print('Quadrado')
elif lados == 5:
    print("PentÃ¡gono")

lados = int(input("Qts lados vc tem : "))
if lados < 3:
    print('NÃ£o Ã© um polÃ­gono')
elif lados > 5:
    print("PolÃ­gono nÃ£o identificado")
else:
    print('Ã‰ um polÃ­gono')


num1 = int(input("Diga um nÃºmero : "))
num2 = int(input("Diga um nÃºmero : "))
num3 = int(input("Diga um nÃºmero : "))

if num1 > num2 and num1 > num3:
    maior = num1
elif num2 > num3:
    maior = num2
else:
    maior = num3

if num1 > num2 and num1>num3:#aqui o num1 serÃ¡ o Ãºltimo no print
    if num2 > num3:#aqui o num2 serÃ¡ o segundo
        print(num3,num2,num1)
    else:#aqui o num3 serÃ¡ o segundo
        print(num2,num3,num1)
elif num2> num3:#aqui o num2 serÃ¡ o ultimo no print
    if num3>num1:#aqui o num3 serÃ¡ o segundo
        print(num1,num3,num2)
    else:#aqui o num1 serÃ¡ o segundo
        print(num3,num1,num2)
else:#aqui o num3 Ã© o ultimo no print
    if num2>num1:#aqui o num2 Ã© o segundo
        print(num1,num2,num3)
    else:#aqui o num1 Ã© o segundo
        print(num2,num1,num3)


if num1 > num2 and num1 > num3:
    pass
elif num2 > num3:
    aux = num1
    num1 = num2
    num2 = aux
else:
    aux = num1
    num1 = num3
    num3 = aux
if num2>num3:
    print(num3,num2,num1)
else:
    print(num2,num3,num1)

a = int(input("Diga o primeiro lado do triangulo : "))
b = int(input("Diga o segundo lado do triangulo : "))
c = int(input("Diga o terceiro lado do triangulo : "))
if a==b and a==c:
    print("equilatero")
elif a==b or a==c or c==b:
    print('IsÃ³sceles')
else:
    print('escaleno')



a = int(input("Diga o primeiro angulo do triangulo : "))
b = int(input("Diga o segundo angulo do triangulo : "))
c = int(input("Diga o terceiro angulo do triangulo : "))
if a+b+c == 180:
    if a==90 or b == 90 or c == 90:
        print("Triangulo retangulo")
    elif a >90 or b > 90 or c >90:
        print("Triangulo obtuso")
    else:
        print("Triangulo agudo")
else:
    print(f"Os angulos que vc digitou nÃ£o correspondem a um triangulo ({a+b+c}!={180})")

#pegue d input a velocidade de um carro
#se ele estiver acima de 80 e abaixo de 100, cobre 5 reais de multa para cada km/h acima de 80
#se ele estiver entre 100 e 120, cobre 10 reais de multa para cada km/h a mais
#se ele estiver acima de 120, cobre 20 reais de multa para cada km/h a mais

v = float(input("Diga a velocidade : "))
multa = 0
if v<=80:
    print("voce Ã© responsÃ¡vel")
elif v<=100:
    print("prestenÃ§Ã£o")
    multa = (v-80)*5
elif v<=120:
    print('mano pega leve')
    multa = (v-100)*10 + 100
else:
    print('vc Ã© um fanfarrÃ£o')
    multa = (v-120)*20 + 100 + 200
print(f"Sua multa Ã© de R${multa}")

frase = 'Eu'
palavra = input("Diga a prÃ³xima palavra : ")
frase = frase + ' ' + palavra
print(frase)
palavra = input("Diga a prÃ³xima palavra : ")
frase = frase + ' ' + palavra
print(frase)
palavra = input("Diga a prÃ³xima palavra : ")
frase = frase + ' ' + palavra
print(frase)

i=0
frase = 'Eu'
while i<3:
    palavra = input(f"Diga a {i+1}Âª palavra : ")
    frase = frase + ' ' + palavra
    print(frase)
    i+=1
'''
senha = '1234'
tentativa = input("Diga sua senha : ")
qtd = 1
while senha != tentativa and qtd <3:
    tentativa = input("Diga sua senha : ")
    qtd+=1


print("Mudando o nome do commit")
