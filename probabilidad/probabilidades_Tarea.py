import random
from bokeh.plotting import figure, show

def tirar_dados (numero_de_tiros):
    suma_dados_por_tiro = []

    for _ in  range (numero_de_tiros):
        tiro_dado_1 = random.choice( [1, 2, 3, 4, 5, 6])
        tiro_dado_2 = random.choice ([1, 2, 3, 4, 5, 6])
        suma_dados_por_tiro.append(tiro_dado_1 + tiro_dado_2)

    return suma_dados_por_tiro

def graph(sim, prob):
    plot = figure(title='Probability get 12 with 1 shot',
                  x_axis_label='Attempts',
                  y_axis_label='Probability')
    
    plot.line(sim,prob)
    show(plot)

def calc_prob(tiros,n):
    tiros_con_12 = 0
    for tiro in tiros: 
        if 12  in tiro:
            tiros_con_12 += 1
             
    return tiros_con_12/ n


def main (numero_de_tiros, numero_de_intentos): 
    tiros = []
    sim  = []
    prob = []

    for n in range(1,numero_de_intentos,1):
        secuencia_de_tiros = tirar_dados(numero_de_tiros)
        tiros.append(secuencia_de_tiros)
        prob_shot_12 = calc_prob(tiros,n)

        prob.append (prob_shot_12)
        sim.append (n)
   ## print (f'Probabilidad de obtener por lo menos un 12 en {numero_de_tiros} tiros = {probabilidad_tiros_con_12} ')
    graph  (sim,prob)      



if __name__ == '__main__':
    numero_de_tiros = int(input('Cuantos tiros de los dados: '))
    numero_de_intentos = int (input('Cuantas Veces correra la simulación:  '))

    main(numero_de_tiros, numero_de_intentos)