from bacteria import bacteria
from chemiotaxis import chemiotaxis


import numpy

# Parámetros iniciales
path = "C:/Users/ELGUA/OneDrive/Documents/multiFasta.fasta"
numeroDeBacterias = 10
iteraciones = 30
tumbo = 1  # Número de gaps a insertar


# Inicialización
poblacion = []
for _ in range(numeroDeBacterias):
    bact = bacteria(path)
    bact.tumboNado(tumbo)
    bact.autoEvalua()
    poblacion.append(bact)

chemio = chemiotaxis()
veryBest = None  # Mejor bacteria global
globalNFE = 0    # Número de evaluaciones de la función objetivo

for iter_num in range(iteraciones):
    # Evaluación y quimiotaxis
    for bacteria in poblacion:
        bacteria.tumboNado(tumbo)
        bacteria.autoEvalua()
    
    chemio.doChemioTaxis(poblacion)
    chemio.update_parameters(poblacion)
    globalNFE += chemio.parcialNFE

    # Elitismo: mantener las mejores bacterias
    elite = chemio.aplicar_elitismo(poblacion)

    # Reducción y reemplazo de la población
    chemio.reducir_poblacion(poblacion)
    num_new_bacterias = numeroDeBacterias - len(poblacion)
    nuevas_bacterias = chemio.generar_nuevas_bacterias(path, elite, num_new_bacterias)
    poblacion.extend(nuevas_bacterias)

    # Actualizar la mejor bacteria global
    best = max(poblacion, key=lambda x: x.fitness)
    if (veryBest is None) or (best.fitness > veryBest.fitness):
        veryBest = best.clonar(path)
        veryBest.fitness = best.fitness
        veryBest.blosumScore = best.blosumScore

    print(f"Iteración: {iter_num + 1}, Mejor Fitness: {veryBest.fitness}, NFE: {globalNFE}")

# Mostrar la mejor alineación encontrada
print("\nMejor Alineación Encontrada:")
veryBest.showGenome()