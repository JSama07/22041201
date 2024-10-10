import random
import math

# Generar 100 números aleatorios entre 0 y 1
numeros_aleatorios = [random.random() for _ in range(100)]
numeros_aleatorios.sort()

# Calcular D+, D- y el estadístico D de Kolmogorov-Smirnov
n = len(numeros_aleatorios)
D_plus = max((i + 1) / n - numeros_aleatorios[i] for i in range(n))
D_minus = max(numeros_aleatorios[i] - i / n for i in range(n))
D = max(D_plus, D_minus)

# Valor crítico de Kolmogorov-Smirnov para un nivel de significancia del 5%
# Fórmula aproximada para n > 35: D_crit = 1.36 / sqrt(n)
D_critico = 1.36 / math.sqrt(n)

# Mostrar resultados
print(f"Estadístico de Kolmogorov-Smirnov calculado: {D:.4f}")
print(f"Valor crítico (al 5% de significancia): {D_critico:.4f}")

# Interpretar el resultado
if D < D_critico:
    print("Los datos parecen ser uniformes (no se rechaza la hipótesis de uniformidad).")
else:
    print("Los datos no parecen ser uniformes (se rechaza la hipótesis de uniformidad).")

