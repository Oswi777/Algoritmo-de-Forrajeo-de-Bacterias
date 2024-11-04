import math
import random
import numpy
from bacteria import bacteria

class chemiotaxis:
    def __init__(self):
        self.parcialNFE = 0
        # Parámetros iniciales
        self.d_attr = 0.1
        self.w_attr = 0.2
        self.h_rep = self.d_attr
        self.w_rep = 10
        self.prev_avg_fitness = None  # Para la adaptación dinámica de parámetros
    
    def compute_cell_interaction(self, bacteria, poblacion, d, w):
        total = 0.0
        for other in poblacion:
            diff = 0.0
            diff += (bacteria.blosumScore - other.blosumScore) ** 2.0
            total += d * math.exp(w * diff)
        return total

    def attract_repel(self, bacteria, poblacion):
        attract = self.compute_cell_interaction(bacteria, poblacion, -self.d_attr, -self.w_attr)
        repel = self.compute_cell_interaction(bacteria, poblacion, self.h_rep, -self.w_rep)
        return attract + repel

    def chemio(self, bacteria, poblacion):
        bacteria.interaction = self.attract_repel(bacteria, poblacion)
        bacteria.fitness = bacteria.blosumScore + bacteria.interaction

    def doChemioTaxis(self, poblacion):
        self.parcialNFE = 0
        for bacteria in poblacion:
            self.chemio(bacteria, poblacion)
            self.parcialNFE += bacteria.NFE
            bacteria.NFE = 0

    def update_parameters(self, poblacion):
        current_avg_fitness = sum(b.fitness for b in poblacion) / len(poblacion)
        if self.prev_avg_fitness is not None:
            if current_avg_fitness > self.prev_avg_fitness:
                self.w_attr *= 1.05  # Intensificar explotación
                self.w_rep *= 1.05
            else:
                self.w_attr *= 0.95  # Fomentar exploración
                self.w_rep *= 0.95
        self.prev_avg_fitness = current_avg_fitness

    def aplicar_elitismo(self, poblacion):
        elite_size = max(2, int(len(poblacion) * 0.1))  # Asegúrate de que el tamaño de la élite sea al menos 2
        poblacion.sort(key=lambda x: x.fitness, reverse=True)
        return poblacion[:elite_size]

    def reducir_poblacion(self, poblacion):
        reduction_rate = 0.1  # Reducir un 10% de la población
        reduce_by = int(len(poblacion) * reduction_rate)
        poblacion.sort(key=lambda x: x.fitness)
        for _ in range(reduce_by):
            poblacion.pop(0)

    def generar_nuevas_bacterias(self, path, elite, num_new_bacterias):
        nuevas_bacterias = []
        for _ in range(num_new_bacterias):
            if len(elite) >= 2:
                parent1, parent2 = random.sample(elite, 2)
            elif len(elite) == 1:
                parent1 = parent2 = elite[0]
            else:
                parent1, parent2 = random.sample(elite, 2)
            
            new_bacteria = self.recombinar_bacterias(path, parent1, parent2)
            nuevas_bacterias.append(new_bacteria)
        return nuevas_bacterias

    def recombinar_bacterias(self, path, bact1, bact2):
        new_bacteria = bacteria(path)
        new_seqs = []
        for i in range(len(bact1.matrix.seqs)):
            seq1 = bact1.matrix.seqs[i]
            seq2 = bact2.matrix.seqs[i]
            crossover_point = random.randint(0, len(seq1))
            new_seq = seq1[:crossover_point] + seq2[crossover_point:]
            new_seqs.append(new_seq)
        new_bacteria.matrix.seqs = numpy.array(new_seqs)
        new_bacteria.cuadra()
        new_bacteria.limpiaColumnas()
        new_bacteria.autoEvalua()
        return new_bacteria

    def randomBacteria(self, path):
        bact = bacteria(path)
        bact.tumboNado(random.randint(1, 10))
        return bact 

    def insertRamdomBacterias(self, path, num, poblacion):
        for _ in range(num):
            poblacion.append(self.randomBacteria(path))
            # Eliminar la bacteria con menor fitness
            poblacion.sort(key=lambda x: x.fitness)
            del poblacion[0]