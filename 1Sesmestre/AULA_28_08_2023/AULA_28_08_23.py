#print("Hello World")
'''palavra_1 = 'Hello'
palavra_2 = 'World'
frase = palavra_1 + ' ' + palavra_2
print(type(frase))

frase = 'Hello'
frase = frase + ' World'
print(frase)


frase = ''
contador=1
palavra = input(f"Diga a {contador}Âª palavra : ")
frase = frase + palavra
print(frase)
contador = contador + 1
palavra = input(f"Diga a {contador}Âª palavra : ")
frase = frase + ' ' + palavra
print(frase)
contador = contador + 1
palavra = input(f"Diga a {contador}Âª palavra : ")
frase = frase + ' ' + palavra
print(frase)
contador = contador + 1
palavra = input(f"Diga a {contador}Âª palavra : ")
frase = frase + ' ' + palavra
print(frase)

num1 = int(input('Diga um numero : '))
num2 = int(input("Diga outro numero : "))
resultado = num1 > num2
print(type(resultado))
print(f"O resultado de {num1} + {num2} Ã© {num1 + num2}")
print(f"O resultado de {num1} - {num2} Ã© {num1 - num2}")
print(f"O resultado de {num1} / {num2} Ã© {num1 / num2}")
print(f"O resultado de {num1} * {num2} Ã© {num1 * num2}")
print(f"O resultado de {num1} // {num2} Ã© {num1 // num2}")
print(f"O resultado de {num1} % {num2} Ã© {num1 % num2}")

num1 = int(input('Diga um numero : '))
num2 = int(input("Diga outro numero : "))
print(f"O resultado de {num1} > {num2} Ã© {num1 > num2}")
print(f"O resultado de {num1} < {num2} Ã© {num1 < num2}")
print(f"O resultado de {num1} >= {num2} Ã© {num1 >= num2}")
print(f"O resultado de {num1} <= {num2} Ã© {num1 <= num2}")
print(f"O resultado de {num1} == {num2} Ã© {num1 == num2}")
print(f"O resultado de {num1} != {num2} Ã© {num1 != num2}")


num1 = int(input('Diga um numero : '))
num2 = int(input("Diga outro numero : "))
num3 = int(input('Diga um numero : '))
num4 = int(input("Diga outro numero : "))
print('VersÃ£o OR : \n')
print(f"{num1} > {num2} or {num3} > {num4}, ou seja,"
      f" {num1 > num2} or {num3 > num4} dÃ¡ {num1 > num2 or num3 > num4}")
print(f"{num1} < {num2} or {num3} > {num4}, ou seja,"
      f" {num1 < num2} or {num3 > num4} dÃ¡ {num1 < num2 or num3 > num4}")
print(f"{num1} > {num2} or {num3} < {num4}, ou seja,"
      f" {num1 > num2} or {num3 < num4} dÃ¡ {num1 > num2 or num3 < num4}")
print(f"{num1} < {num2} or {num3} < {num4}, ou seja,"
      f" {num1 < num2} or {num3 < num4} dÃ¡ {num1 < num2 or num3 < num4}")
print()
print('VersÃ£o AND : \n')

print(f"{num1} > {num2} and {num3} > {num4}, ou seja,"
      f" {num1 > num2} and {num3 > num4} dÃ¡ {num1 > num2 and num3 > num4}")
print(f"{num1} < {num2} and {num3} > {num4}, ou seja,"
      f" {num1 < num2} and {num3 > num4} dÃ¡ {num1 < num2 and num3 > num4}")
print(f"{num1} > {num2} and {num3} < {num4}, ou seja,"
      f" {num1 > num2} and {num3 < num4} dÃ¡ {num1 > num2 and num3 < num4}")
print(f"{num1} < {num2} and {num3} < {num4}, ou seja,"
      f" {num1 < num2} and {num3 < num4} dÃ¡ {num1 < num2 and num3 < num4}")

salario = int(input("Diga seu salÃ¡rio : "))
if salario <2112:
    porcentagem = 0
elif salario <= 2826:
    porcentagem = 0.075
elif salario <= 3751:
    porcentagem = 0.15
elif salario <= 4664:
    porcentagem = 0.225
else:
    porcentagem = 0.275
desconto = porcentagem * salario
final = salario - desconto
print(f"Voce receberÃ¡ {final} com desconto de R${desconto}!!!")
'''

'''letra = input('Diga uma letra : ')
if letra == 'a':
    print(f"{letra} Ã© vogal")
elif letra == 'e':
    print(f"{letra} Ã© vogal")
elif letra == 'i':
    print(f"{letra} Ã© vogal")
elif letra == 'o':
    print(f"{letra} Ã© vogal")
elif letra == 'u':
    print(f"{letra} Ã© vogal")
else:
    print("nÃ£o Ã© vogal")

letra = input('Diga uma letra : ')
if letra == 'a' or letra =='e' or letra =='i' or letra =='o' or letra =='u':
    print(f"{letra} Ã© vogal")
else:
    print(f"{letra} nÃ£o Ã© vogal")
'''
#EXERCÃCIO 1
num1  = int(input("Diga o primeiro numero : "))
num2  = int(input("Diga o segundo numero : "))
if num1 > num2:
    print(f"{num1} > {num2}")
else:
    print(f"{num2} > {num1}")

#EXERCÃCIO 2
ano = int(input("Diga seu ano de nascimento : "))
if ano>=2006:
    print("vc nao pode votar")
else:
    print("vc pode votar")

#EXERCÃCIO 3