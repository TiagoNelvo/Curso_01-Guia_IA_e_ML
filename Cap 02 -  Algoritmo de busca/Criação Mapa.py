class Vertice:
    def __init__(self, rotulo):
        self.rotulo = rotulo
        self.visitado = False
        self.adjacentes = []
        
    def adiciona_adjacente(self, adjacente):
        self.adjacentes.append(adjacente)
        
    def mostra_adjacentes(self):
        for i in self.adjacentes:
            print(f"{i.vertice.rotulo} - custo: {i.custo}")
            
class Adjacente:
    def __init__(self, vertice, custo):
        self.vertice = vertice
        self.custo = custo
        
class Grafo:
    def __init__(self):
        self.arad      = Vertice('Arad')
        self.zerind    = Vertice('Zerind')
        self.oradea    = Vertice('Oradea')
        self.sibiu     = Vertice('Sibiu')
        self.timisoara = Vertice('Timisoara')
        self.lugoj     = Vertice('Lugoj')
        self.mehadia   = Vertice('Mehadia')
        self.dobreta   = Vertice('Dobreta')
        self.craiova   = Vertice('Craiova')
        self.rimnicu   = Vertice('Rimnicu')
        self.fagaras   = Vertice('Fagaras')
        self.pitesti   = Vertice('Pitesti')
        self.bucharest = Vertice('Bucharest')
        self.giurgiu   = Vertice('Giurgiu')
        
        self.cria_grafo()
    
    def cria_grafo(self):
        self.arad.adiciona_adjacente(Adjacente(self.zerind, 75))
        self.arad.adiciona_adjacente(Adjacente(self.sibiu, 140))
        self.arad.adiciona_adjacente(Adjacente(self.timisoara, 118))
        
        self.zerind.adiciona_adjacente(Adjacente(self.arad, 75))
        self.zerind.adiciona_adjacente(Adjacente(self.oradea, 71))
        
        self.oradea.adiciona_adjacente(Adjacente(self.zerind, 71))
        self.oradea.adiciona_adjacente(Adjacente(self.sibiu, 151))
        
        self.sibiu.adiciona_adjacente(Adjacente(self.oradea, 151))
        self.sibiu.adiciona_adjacente(Adjacente(self.arad, 140))
        self.sibiu.adiciona_adjacente(Adjacente(self.fagaras, 99))
        
        self.timisoara.adiciona_adjacente(Adjacente(self.arad, 118))
        self.timisoara.adiciona_adjacente(Adjacente(self.lugoj, 111))
        
        self.lugoj.adiciona_adjacente(Adjacente(self.timisoara, 111))
        self.lugoj.adiciona_adjacente(Adjacente(self.mehadia, 70))
        
        self.mehadia.adiciona_adjacente(Adjacente(self.lugoj, 70))
        self.mehadia.adiciona_adjacente(Adjacente(self.dobreta, 75))
        
        self.dobreta.adiciona_adjacente(Adjacente(self.mehadia, 75))
        self.dobreta.adiciona_adjacente(Adjacente(self.craiova, 120))
        
        self.craiova.adiciona_adjacente(Adjacente(self.dobreta, 120))
        self.craiova.adiciona_adjacente(Adjacente(self.pitesti, 138))
        
        self.rimnicu.adiciona_adjacente(Adjacente(self.sibiu, 80))
        self.rimnicu.adiciona_adjacente(Adjacente(self.pitesti, 97))
        self.rimnicu.adiciona_adjacente(Adjacente(self.craiova, 146))
        
        self.pitesti.adiciona_adjacente(Adjacente(self.rimnicu, 97))
        self.pitesti.adiciona_adjacente(Adjacente(self.craiova, 138))
        self.pitesti.adiciona_adjacente(Adjacente(self.bucharest, 101))
        
        self.fagaras.adiciona_adjacente(Adjacente(self.sibiu, 99))
        self.fagaras.adiciona_adjacente(Adjacente(self.bucharest, 211))
        
        self.bucharest.adiciona_adjacente(Adjacente(self.fagaras, 211))
        self.bucharest.adiciona_adjacente(Adjacente(self.pitesti, 101))
        self.bucharest.adiciona_adjacente(Adjacente(self.giurgiu, 90))
        
        self.giurgiu.adiciona_adjacente(Adjacente(self.bucharest, 90))

grafo = Grafo()
print('------')
grafo.arad.mostra_adjacentes()
print('------')
grafo.bucharest.mostra_adjacentes()
print('------')
