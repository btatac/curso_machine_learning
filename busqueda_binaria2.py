import random

def busqueda_binaria (lista,comienxo,final, objetivo):
    print (f'buscando {objetivo} entre {lista[comienxo]} y {lista[final-1]}')
    if (comienxo > final):
        return False

    medio = (comienxo + final) // 2 

    if lista[medio] == objetivo:
        return True
    elif lista [medio] < objetivo:
        return busqueda_binaria(lista, medio + 1 , final, objetivo)
    else:
        return busqueda_binaria(lista, comienxo, medio-1,objetivo)
        




if __name__ =='__main__':
    tamano_de_la_lista = int (input('De que tamano esl a lista? '))
    objetivo = int (input('que numero quieres encontrar? '))

    lista = sorted([random.randint(0,100)for i in range (tamano_de_la_lista)])
    encontrado = busqueda_binaria (lista,0,len(lista), objetivo)
    print (lista)
    print (f'El elemento {objetivo} {"esta" if encontrado else "no esta"} en la lista ' )       