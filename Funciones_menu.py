def mayor_que (num_1, num_2): 

    if num_1 > num_2:
        print('El primer numero es mayor que el segundo')
    elif num_1 < num_2:
        print('El segundo numero es mayor que el primero')
    else :
        print('Los dos numeros son iguales')


def raiz_binaria (objetivo):
    epsilon = 0.001
    bajo = 0.0 
    alto = max (1.0, objetivo)
    respuesta = (alto + bajo) / 2

    while abs (respuesta**2 - objetivo)>= epsilon:
        print (f'bajo={bajo}, alto={alto}, respuesta={respuesta}')
        if respuesta**2 < objetivo : 
            bajo  = respuesta
        else: 
            alto = respuesta 

        respuesta = (alto + bajo) / 2   

    print (f'la raiz cuadrda de {objetivo} es {respuesta}')  



print ('*****Menu pricipal*****')
print ('Opciones')
print ('Teclea 1 para identificar cual numero es mayor')
print ('Teclea 2 para encontrar raiz')
op = int(input('ingresa opción: '))



if (op == 1 ) : 
    print('BIENVENIDO A LA OPCIÓN MAYOR QUE')
    numero_1 = int(input('Escoge un entero '))
    numero_2 =  int(input('Escoge otro entero '))
    mayor_que(numero_1, numero_2)
elif (op == 2) :
    print('BIENVENIDO A LA OPCIÓN ENCONTRAR RAIZ')
    objetivo = int(input('Escoge un numero: '))
    raiz_binaria(objetivo)
else : 
    print ('la opción no es valida.')
    print('Fin.')

print('Gracias por ingresar.')





    
