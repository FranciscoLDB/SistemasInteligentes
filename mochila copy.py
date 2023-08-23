import random

itens = [
    {'valor': 5, 'peso': 5},
    {'valor': 2, 'peso': 2},
    {'valor': 7, 'peso': 8},
    {'valor': 3, 'peso': 4},
    ]

capacidade = 15
estados = []
num_estados = 20;

def sorteiaEstado(sol):
    if len(sol['fora']) < 1:
        return    
    cap_aux = sum(item["peso"] for item in sol["dentro"])
    aux = sol['fora'].pop(random.randint(0, len(sol['fora'])-1))
    cap_aux += aux['peso']
    if cap_aux <= capacidade:
        sol['dentro'].append(aux)
    else:
        sol['fora'].append(aux)

    # print(sol)

for x in range(num_estados):
    estado = {'dentro': [], 'fora': itens.copy()}
    for i in range(10):
        sorteiaEstado(estado)
    estados.append(estado)
    # print("=-=-=-=-==-=-=--=-=-=-===--=-=-=--=-")
    # print(estados)

print("========================================================")   
