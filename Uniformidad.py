import random
import math


numeros_aleatorios = [random.random() for _ in range(100)]
numeros_aleatorios.sort()


n = len(numeros_aleatorios)
D_plus = max((i + 1) / n - numeros_aleatorios[i] for i in range(n))
D_minus = max(numeros_aleatorios[i] - i / n for i in range(n))
D = max(D_plus, D_minus)


D_critico = 1.36 / math.sqrt(n)


print(f"Estadístico de Kolmogorov-Smirnov calculado: {D:.4f}")
print(f"Valor crítico (al 5% de significancia): {D_critico:.4f}")


if D < D_critico:
    print("Los datos parecen ser uniformes (no se rechaza la hipótesis de uniformidad).")
else:
    print("Los datos no parecen ser uniformes (se rechaza la hipótesis de uniformidad).")

