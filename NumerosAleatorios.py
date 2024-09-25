import random

# Función para generar números aleatorios por el método de centros al cuadrado
def centros_al_cuadrado(semilla, n):
    resultados = []
    for _ in range(n):
        cuadrado = str(semilla ** 2).zfill(8)  # Asegurarse de que sea de 8 dígitos
        semilla = int(cuadrado[2:6])  # Tomar los 4 dígitos del medio
        if semilla == 0:  # Evitar que la semilla sea 0
            semilla = random.randint(1000, 9999)  # Cambiar a una nueva semilla aleatoria
        resultados.append(semilla / 10000)  # Normalizar dividiendo entre 10000
    return resultados

# Función para generar números aleatorios por el método de medios cuadrados
def medios_cuadrados(semilla, n):
    resultados = []
    for _ in range(n):
        cuadrado = semilla ** 2
        cuadrado_str = str(cuadrado).zfill(8)  # Asegurar que tenga 8 dígitos
        medios = cuadrado_str[2:6]  # Tomar los 4 dígitos del centro
        semilla = int(medios)
        if semilla == 0:  # Evitar que la semilla sea 0
            semilla = random.randint(1000, 9999)  # Cambiar a una nueva semilla aleatoria
        resultados.append(semilla / 10000)  # Normalizar dividiendo entre 10000
    return resultados

# Función principal que permite al usuario elegir el método
def generar_numeros_aleatorios():
    print("Seleccione el método para generar 100 números aleatorios:")
    print("1. Método de centros al cuadrado")
    print("2. Método de medios cuadrados")
    
    eleccion = input("Ingrese el número de su elección (1 o 2): ")
    
    semilla = int(input("Ingrese una semilla inicial (un número de 4 dígitos): "))
    cantidad = 100
    
    if eleccion == '1':
        numeros = centros_al_cuadrado(semilla, cantidad)
        print("\nNúmeros generados por el método de centros al cuadrado:")
    elif eleccion == '2':
        numeros = medios_cuadrados(semilla, cantidad)
        print("\nNúmeros generados por el método de medios cuadrados:")
    else:
        print("Selección no válida.")
        return
    
    # Mostrar los números generados
    for i, numero in enumerate(numeros, start=1):
        print(f"{i}: {numero}")

# Ejecutar el programa
if __name__ == "__main__":
    generar_numeros_aleatorios()
