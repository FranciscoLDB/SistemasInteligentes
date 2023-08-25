import random

itens = [
    {'valor': 5, 'peso': 5},
    {'valor': 2, 'peso': 2},
    {'valor': 4, 'peso': 1},
    {'valor': 3, 'peso': 4},
    {'valor': 9, 'peso': 3},
    ]

capacidade = 10
estados = []
num_estados = 1;

def sorteiaEstado():
    sys_random = random.SystemRandom()
    estado = {'dentro': [], 'fora': itens.copy()}
    
    cap_aux = sum(item["peso"] for item in estado["dentro"])
    sorteio_fora = []
    while len(estado['fora']) > 0:
        item_sort = estado['fora'].pop(0)
        cap_aux += item_sort['peso']
        if sys_random.randint(0, 1) and cap_aux <= capacidade:
            estado['dentro'].append(item_sort)
        else:
            cap_aux -= item_sort['peso']
            sorteio_fora.append(item_sort)

    # estado['fora'] = sorteio_fora.copy()

    return estado
    # print(estado)

def percorre(estado):
    sys_random = random.SystemRandom()
    if len(estado['fora']) < 1:
        return sum(item["valor"] for item in estado["dentro"])  
    item_first = estado['fora'].pop(0)
    cap_aux = sum(item["peso"] for item in estado["dentro"])
    cap_aux += item_first['peso']
    if sys_random.randint(0, 1) and cap_aux <= capacidade:
        estado['dentro'].append(item_first)
    # else:
    #     estado['fora'].append(item_first)
        
    
    return sum(item["valor"] for item in estado["dentro"])

for x in range(num_estados):
    estados.append(sorteiaEstado())

print("===========================================")
print("==============Estados criados==============")
print("===========================================") 

melhor = {
    'num_estado': 0,
    'valor': 0,
    'itens': []
}
aux_melhor = 0;
c = 0;
while True:
    for estado in estados:
        print(estado)
        print("-")
        valor_estado = sum(item["valor"] for item in estado["dentro"])
        deltaE = percorre(estado)
        if valor_estado > melhor['valor']:
            melhor['num_estado'] = estados.index(estado)
            melhor['valor'] = valor_estado
            melhor['itens'] = estado['dentro'].copy()
            
        if deltaE == valor_estado:
            # print(f"/////////////// ANTES //////////////////////////////")
            # print(estado)
            estado = sorteiaEstado()
            # print(f"/////////////// DEPOIS /////////////////////////////")
            # print(estado)
            valor_estado = 0
        
    
    c += 1
    # print(f"Contagem: {c} | Melhor estado: {melhor['num_estado']} | Valor: {melhor['valor']}")
    # print(melhor['itens'])
    # print(f"===========================================")
    if melhor['valor'] >= 17:
        print(f"FIM")
        break

print(f"Contagem: {c} | Melhor estado: {melhor['num_estado']} | Valor: {melhor['valor']}")
print(f"===========================================")


