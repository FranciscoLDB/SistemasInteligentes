import networkx as nx
import matplotlib.pyplot as plt

# Crie um objeto do tipo DiGraph (grafo direcionado)
G = nx.DiGraph()

# Adicione nós ao grafo
G.add_node('pao')
G.add_node('peixe')
G.add_node('roda')

# Adicione arestas ao grafo
G.add_edge('pao', 'peixe')
G.add_edge('pao', 'roda')

# Desenhe o grafo
pos = nx.spring_layout(G)  # Define a disposição dos nós
nx.draw(G, pos, with_labels=True, node_size=1000, node_color="skyblue", font_size=10, font_color="black")
plt.show()
