import blosum as bl

class evaluadorBlosum:
    
    def __init__(self):
        self.matrix = bl.BLOSUM(62)
        
    def showMatrix(self):
        print(self.matrix)
        
    def getScore(self, A, B):
        if A == "-" or B == "-":
            return -2  # Penalización por gap
        score = self.matrix[A][B]
        return score