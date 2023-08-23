import random

itens = [
    {'valor': 5, 'peso': 5},
    {'valor': 2, 'peso': 2},
    {'valor': 7, 'peso': 8},
    {'valor': 3, 'peso': 4},
    {'valor': 4, 'peso': 1},
    {'valor': 5, 'peso': 8},
    {'valor': 7, 'peso': 7},
    {'valor': 3, 'peso': 4},
    {'valor': 4, 'peso': 6},
    {'valor': 9, 'peso': 3},
    ]

capacidade = 20
itens_aux = itens
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
print(f"Estados: {num_estados}")
melhor = {
    'num_estado': 0,
    'valor': 0
}
for i in range(num_estados):
    valor_estado = sum(item["valor"] for item in estados[i]["dentro"])
    # print("estado " + str(i) + " | valor: " + str(valor_estado) + " | capacidade: " + str(sum(item["peso"] for item in estados[i]["dentro"])))
    if valor_estado > melhor['valor']:
        melhor['num_estado'] = i
        melhor['valor'] = valor_estado
    # for item in estados[i]['dentro']:
    #     print("peso: " + str(item['peso']) + " | valor: " + str(item['valor']))    
    # print("--------------------------------------------------------")

print(f"Melhor estado: {melhor['num_estado']} | Valor: {melhor['valor']}")

print("========================================================")   
