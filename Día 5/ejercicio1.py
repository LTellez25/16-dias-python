def devolver_distintos(numero1, numero2, numero3):
    suma = numero1 + numero2 + numero3
    
    if suma > 15:
        return max(numero1, numero2, numero3)
    elif suma < 10:
        return min(numero1, numero2, numero3)
    else:
        numeros = [numero1, numero2, numero3]
        numeros.sort()
        return numeros[1] 

print(devolver_distintos(10, 0, 1))
