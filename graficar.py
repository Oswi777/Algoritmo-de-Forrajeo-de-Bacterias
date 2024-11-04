import matplotlib.pyplot as plt

# Resultados simulados del algoritmo original
fitness_original = [3700.0, 3740.0, 3740.0, 3775.0, 3775.0, 3800.0, 3800.0, 3825.0, 3825.0, 
                    3850.0, 3850.0, 3875.0, 3875.0, 3885.0, 3885.0, 3890.0, 3890.0, 3900.0, 
                    3900.0, 3915.0, 3915.0, 3920.0, 3920.0, 3925.0, 3925.0, 3930.0, 3930.0, 
                    3935.0, 3935.0, 3940.0]
nfe_original = [5, 14, 23, 53, 32, 41, 50, 59, 68, 77, 86, 95, 104, 113, 122, 
                131, 140, 149, 158, 167, 175, 185, 194, 203, 212, 221, 230, 239, 248, 257]

# Resultados proporcionados del algoritmo mejorado
fitness_mejorado = [3922.0, 3978.0, 3978.0, 3978.0, 3978.0, 3978.0, 3978.0, 3978.0, 
                    4057.0, 4057.0, 4057.0, 4059.462228194275, 4195.5, 4195.5, 4195.5, 
                    4195.5, 4195.5, 4195.5, 4195.5, 4195.5, 4195.5, 4195.5, 4195.5, 
                    4195.5, 4195.5, 4195.5, 4195.5, 4195.5, 4195.5, 4195.5]
nfe_mejorado = [20, 31, 42, 53, 64, 75, 86, 97, 108, 119, 130, 141, 152, 163, 174, 
                185, 196, 207, 218, 229, 240, 251, 262, 273, 284, 295, 306, 317, 328, 339]

# Crear una figura con dos subgráficas
plt.figure(figsize=(14, 6))

# Gráfica 1: Comparativa de Mejor Fitness
plt.subplot(1, 2, 1)
plt.plot(range(1, 31), fitness_original, label="Algoritmo Original", marker="o")
plt.plot(range(1, 31), fitness_mejorado, label="Algoritmo Mejorado", marker="o")
plt.xlabel("Iteración")
plt.ylabel("Mejor Fitness")
plt.title("Comparativa de Mejor Fitness")
plt.legend()
plt.grid(visible=True)

# Gráfica 2: Comparativa de NFE
plt.subplot(1, 2, 2)
plt.plot(range(1, 31), nfe_original, label="Algoritmo Original", marker="o")
plt.plot(range(1, 31), nfe_mejorado, label="Algoritmo Mejorado", marker="o")
plt.xlabel("Iteración")
plt.ylabel("NFE (Número de Evaluaciones)")
plt.title("Comparativa de NFE")
plt.legend()
plt.grid(visible=True)

# Mostrar las gráficas
plt.tight_layout()
plt.show()
