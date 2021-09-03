import random

def busqueda_lineal(lista, objetivo):
    macth = False

    for elemento in lista : #0(n)
        if elemento == objetivo :
            macth = True
            break
    return macth

if __name__ =='__main__':
    tamano_de_la_lista = int (input('De que tamano esl a lista? '))
    objetivo = int (input('que numero quieres encontrar? '))

    lista = [random.randint(0,100)for i in range (tamano_de_la_lista)]
    encontrado = busqueda_lineal(lista,objetivo)
    print (lista)
    print (f'El elemento {objetivo} {"esta" if encontrado else "no esta"} en la lista ' )       