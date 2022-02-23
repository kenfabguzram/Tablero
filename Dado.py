import numpy as np
class Dado:

    caras=0

    def __init__(self, numCaras):
        self.caras=numCaras 
          
    def lanzar(self):
        return np.random.randint(low=1,high=self.caras)
