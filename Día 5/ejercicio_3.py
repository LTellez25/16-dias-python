def contiene_doble_cero(*args):
    # Recorre los argumentos y verifica si hay dos ceros consecutivos
    for i in range(len(args) - 1):
        if args[i] == 0 and args[i + 1] == 0:
            return True
    return False

# Ejemplos de uso
print(contiene_doble_cero(5, 6, 1, 0, 0, 9, 3, 5))  # True
print(contiene_doble_cero(6, 0, 5, 1, 0, 3, 0, 1))  # False
