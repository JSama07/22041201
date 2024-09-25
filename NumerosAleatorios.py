import random


def centros_al_cuadrado(semilla, n):
    resultados = []
    for _ in range(n):
        cuadrado = str(semilla ** 2).zfill(8)  
        semilla = int(cuadrado[2:6])  
        if semilla == 0:  
            semilla = random.randint(1000, 9999)  
        resultados.append(semilla / 10000)  
    return resultados


def medios_cuadrados(semilla, n):
    resultados = []
    for _ in range(n):
        cuadrado = semilla ** 2
        cuadrado_str = str(cuadrado).zfill(8)  
        medios = cuadrado_str[2:6]  
        semilla = int(medios)
        if semilla == 0: 
            semilla = random.randint(1000, 9999)  
        resultados.append(semilla / 10000)  
    return resultados


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
    
    
    for i, numero in enumerate(numeros, start=1):
        print(f"{i}: {numero}")


if __name__ == "__main__":
    generar_numeros_aleatorios()
