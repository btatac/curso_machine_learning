import random
import collections

PALOS = ['espada','corazon', 'picas','trebol']
VALORES = ['as',2,3,4,5,6,7,8,9,10,'jota','reina','rey']

def crear_baraja ():
    barajas = []
    for palo in PALOS:
        for valor in VALORES:
            barajas.append((palo,valor))

    return barajas

def obtener_mano(barajas,tamano_mano):
    mano = random.sample(barajas,tamano_mano)

    return mano

def cambiar_cartas_a_numero (valores):
    for i,valor in enumerate(valores): 
        if valor =='as':
            valores[i] = 1
        elif valor == 'jota':
            valores[i] = 11
        elif valor == 'reina':
            valores[i] = 12
        elif valor == 'rey':
            valores[i] = 13    
    return valores

def escalera (valores):

    valoresnumeros = cambiar_cartas_a_numero(valores)
    valores = sorted(valoresnumeros)
    count = 0
    hay_escalera = False
    for i in range (len(valores)-1):
        if valores[i]+1 != valores[i+1]:
            pass

        elif valores[i]+1 == valores[i+1]:
            count += 1
   
    if valores[len(valores)-1] - 1 == valores[len(valores)-2]:
            count += 1

    if count == 5:
        hay_escalera = True

    return hay_escalera            

def main(tamano_mano,intentos):
    barajas = crear_baraja()
    manos = []
    for _ in range(intentos):
        mano = obtener_mano(barajas,tamano_mano)
        manos.append(mano)

    pares = 0
    escaleras = 0
    for mano in manos:
        valore = []
        for carta in mano:
            valore.append (carta[1])   

        counter = dict (collections.Counter(valore))
        for val in counter.values():
            if val == 3:
                pares += 1
                break

        valoresint =  cambiar_cartas_a_numero (valore)  
        if escalera(valoresint) :
            escaleras += 1
 

    if (escaleras >=0 ):
        probabilidad_escalera = escaleras/intentos  
    elif (escaleras == 0) :
        probabilidad_escalera = 0

    probabilidad_par = pares/intentos 
    print (f'la probabilidad de encotrar un trio en una mano de {tamano_mano} cartas  es: {probabilidad_par}') 
    print (f'la probabilidad de encotrar una escalera en una mano de {tamano_mano} cartas  es: {probabilidad_escalera}')           

if __name__ == '__main__':
    tamano_mano = int (input ('De cuantas cartas sera la mano: '))
    intentos = int (input('cuantos intentos para calcular la probabilidad: '))

    main (tamano_mano,intentos)
