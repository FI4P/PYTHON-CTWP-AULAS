
array = [1 , 2 , 3 , 4, 5 , 6 , 7 , 8]


def media(array):
    soma = 0
    for i  in range(len(array)):
        soma = soma + array[i]
        print(soma)
    return soma/len(array)


def sub(media, array):
    numerador = 0
    for i in array:
        numerador = numerador + (i - media)**2

    return numerador


def desvio_padrao(array):

    avg = media(array)

    result = sub(avg, array)

    return print((result/len(array))**0.5)


desvio_padrao(array)


