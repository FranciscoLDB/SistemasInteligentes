import random

itens = [
    {'valor': 5, 'peso': 5},
    {'valor': 2, 'peso': 2},
    {'valor': 7, 'peso': 8},
    {'valor': 3, 'peso': 4},
    {'valor': 8, 'peso': 2},
    {'valor': 5, 'peso': 6},
    {'valor': 6, 'peso': 3},
    {'valor': 4, 'peso': 1},
    {'valor': 5, 'peso': 8},
    {'valor': 7, 'peso': 7},
    {'valor': 3, 'peso': 4},
    {'valor': 4, 'peso': 6},
    {'valor': 2, 'peso': 2},
    {'valor': 3, 'peso': 5},
    {'valor': 9, 'peso': 3},
    ]

capacidade = 20

estados = []
num_estados = 5;

def sorteiaEstado(sol):
    sol.append(itens[random.randint(0, len(itens)-1)])
    print(sol)

for x in range(num_estados):
    estado = []
    sorteiaEstado(estado)
    estados.append(estado)

print("=============================")
for est in range(num_estados):
    print("estado " + str(est))
    for item in estados[est]:
        print("peso: " + str(item['peso']) + " | valor: " + str(item['valor']))
    print("--------------------------------------------------------")
        
