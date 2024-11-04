import numpy

class fastaReader():
    """Clase para leer un archivo FASTA y guardarlo en numpy array"""

    def __init__(self, path):
        self.path = path
        self.seqs = []
        self.names = []
        self.read()

    def read(self):
        f = open(self.path, "r")
        lines = f.readlines()
        f.close()
        seq = ""
        for line in lines:
            if line[0] == ">":
                self.names.append(line[1:].strip())
                if seq != "":
                    self.seqs.append(seq)
                seq = ""
            else:
                seq += line.strip()
        self.seqs.append(seq)
        self.seqs = numpy.array(self.seqs)
