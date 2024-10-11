#Representação do Problema

#lista
pessoas = [('Lisboa','LIS'),
           ('Madrid','MAD'),
           ('Paris','CDG'),
           ('Dublin','DUB'),
           ('Bruxelas','BRU'),
           ('Londres','LHR')]

pessoas[5]

destino = 'FCO'

#dicionario
'''voos = {('BRU','FCO'): ['15:44','18:55', 382]}

voos

voos[('BRU', 'FCO')][0], voos[('BRU', 'FCO')][1], voos[('BRU', 'FCO')][2]
'''

voos = {}
for linha in open(r'C:\Users\Tilto\Desktop\Work\Guia IA e ML\Cap 03 - Algoritmos de otimização\flights.txt'):
    #print(linha)
    #print(linha.split(','))
    origem, destino, saida, chegada, preco = linha.split(',')
    voos.setdefault((origem, destino), [])
    voos[(origem, destino)].append((saida,chegada, int(preco)))
    
voos

voos[('LIS', 'FCO')]

voos [('FCO', 'LIS')]

