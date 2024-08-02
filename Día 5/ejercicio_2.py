def letras_unicas_ordenadas(palabra):
    # Convertir la palabra a un conjunto para eliminar letras repetidas
    letras_unicas = set(palabra)
    
    # Convertir el conjunto a una lista y ordenarla alfabéticamente
    letras_ordenadas = sorted(letras_unicas)
    
    return letras_ordenadas

# Ejemplo de uso
resultado = letras_unicas_ordenadas("entretenido")
print(resultado)
