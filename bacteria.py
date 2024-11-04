import random
import numpy
import copy
from fastaReader import fastaReader
from evaluadorBlosum import evaluadorBlosum

class bacteria:
    
    def __init__(self, path):
        self.matrix = fastaReader(path)
        self.blosumScore = 0
        self.fitness = 0
        self.interaction = 0
        self.NFE = 0
        
    def showGenome(self):
        for seq in self.matrix.seqs:
            print(seq)

    def clonar(self, path):
        newBacteria = bacteria(path)
        newBacteria.matrix.seqs = numpy.array(copy.deepcopy(self.matrix.seqs))
        return newBacteria

    def tumboNado(self, numGaps):
        self.cuadra()
        matrixCopy = copy.deepcopy(self.matrix.seqs)
        matrixCopy = matrixCopy.tolist()  # Convertir a lista para modificar
        gapRandomNumber = random.randint(0, numGaps)  # Número de gaps a insertar
        for _ in range(gapRandomNumber):
            seqnum = random.randint(0, len(matrixCopy) - 1)  # Selección de secuencia
            pos = random.randint(0, len(matrixCopy[0]))
            part1 = matrixCopy[seqnum][:pos]
            part2 = matrixCopy[seqnum][pos:]
            temp = "-".join([part1, part2])  # Insertar gap
            matrixCopy[seqnum] = temp
        matrixCopy = numpy.array(matrixCopy)  # Convertir a numpy array nuevamente
        self.matrix.seqs = matrixCopy
        
        self.cuadra()
        self.limpiaColumnas()
    
    def cuadra(self):
        """Rellena con gaps las secuencias más cortas"""
        seq = self.matrix.seqs
        maxLen = len(max(seq, key=len))
        for i in range(len(seq)):
            if len(seq[i]) < maxLen:
                seq[i] = seq[i] + "-" * (maxLen - len(seq[i]))
        self.matrix.seqs = numpy.array(seq)
    
    def gapColumn(self, col):
        """Método para saber si una columna tiene gap en todos los elementos"""
        for i in range(len(self.matrix.seqs)):
            if self.matrix.seqs[i][col] != "-":
                return False
        return True

    def limpiaColumnas(self):
        """Elimina las columnas con gaps en todos los elementos"""
        i = 0
        while i < len(self.matrix.seqs[0]):
            if self.gapColumn(i):
                self.deleteColumn(i)
            else:
                i += 1

    def deleteColumn(self, pos):
        """Elimina un elemento específico en cada secuencia"""
        for i in range(len(self.matrix.seqs)):
            self.matrix.seqs[i] = self.matrix.seqs[i][:pos] + self.matrix.seqs[i][pos + 1:]

    def getColumn(self, col):
        """Obtiene una lista con los elementos de cada columna"""
        column = [self.matrix.seqs[i][col] for i in range(len(self.matrix.seqs))]
        return column

    def autoEvalua(self):
        """Evalúa las secuencias utilizando la matriz BLOSUM"""
        evaluador = evaluadorBlosum()
        score = 0
        for i in range(len(self.matrix.seqs[0])):
            column = self.getColumn(i)
            gapCount = column.count("-")
            column = [x for x in column if x != "-"]
            pares = self.obtener_pares_unicos(column)
            for par in pares:
                par_score = evaluador.getScore(par[0], par[1])
                score += par_score
                #print(f"Par: {par}, Score del par: {par_score}")  # Debug
            # Penalización menor para gaps
            score -= gapCount * 0.5
            #print(f"Gap count: {gapCount}, Penalización: {gapCount * 0.5}")  # Debug
        #print(f"Score total para esta bacteria: {score}")  # Debug
        self.blosumScore = score
        self.NFE += 1

    def obtener_pares_unicos(self, columna):
        pares_unicos = set()
        for i in range(len(columna)):
            for j in range(i + 1, len(columna)):
                par = tuple(sorted([columna[i], columna[j]]))
                pares_unicos.add(par)
        return list(pares_unicos)