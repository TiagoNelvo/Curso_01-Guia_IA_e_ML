
import numpy as np

class VetorOrdenado:
    def __init__(self, capacidade):
        self.capacidade = capacidade
        self.ultima_posicao = -1
        self.valores = np.empty(self.capacidade, dtype = int)

#0(n)
def imprime(self):
    if self.ultima_posicao == -1:
        print('O vetor esta vazio')
    else:
        for i in range(self.ultima_posicao + 1):
            print(i, ' - ', self.valores[i])