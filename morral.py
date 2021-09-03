def morral (tam_morral,pesos,valores, n):
    
    if n == 0 or tam_morral ==0:
        return 0

    if pesos [n-1] > tam_morral:
        return morral(tam_morral,pesos,valores,n-1)

    return max(valores[n-1] + morral(tam_morral-pesos[n-1],pesos,valores,n-1), 
                 morral(tam_morral,pesos,valores,n-1) )        


if __name__ == '__main__':
    valores = [60, 100, 120]
    pesos = [10, 20, 30]
    tama_morral = 50
    n = len(valores)

    resultado = morral(tama_morral, pesos, valores, n)
    print (resultado)