import random

def ordenamineto_de_burbuja (lista):
    n = len(lista)
    for i in range(n):
        for j in range (0, n - i - 1):
            if lista[j] > lista [j + 1]:
                lista[j], lista[j + 1] = lista[j + 1], lista[j]
    return lista            



if __name__ =='__main__':
    tamano_de_la_lista = int (input('De que tamano esl a lista? '))

    lista = [random.randint(0,100)for i in range (tamano_de_la_lista)]
    print (lista)
    lista_ordenada = ordenamineto_de_burbuja(lista)
    print (lista_ordenada)