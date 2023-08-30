import secrets

itens = [
    {'valor': 5, 'peso': 5},
    {'valor': 2, 'peso': 2},
    {'valor': 4, 'peso': 1},
    {'valor': 3, 'peso': 4},
    {'valor': 9, 'peso': 3},
    {'valor': 6, 'peso': 3},
    {'valor': 5, 'peso': 8},
    {'valor': 8, 'peso': 4},
    {'valor': 1, 'peso': 1},
    {'valor': 4, 'peso': 6},
    ]

capacidade = 17
estados = []
num_estados = 3;

def sorteiaEstado():
    estado = {'dentro': [], 'fora': itens.copy()}
    
    cap_aux = sum(item["peso"] for item in estado["dentro"])
    sorteio_fora = []
    while len(estado['fora']) > 0:
        item_sort = estado['fora'].pop(0)
        cap_aux += item_sort['peso']
        if secrets.randbelow(2) and cap_aux <= capacidade:
            estado['dentro'].append(item_sort)
        else:
            cap_aux -= item_sort['peso']
            sorteio_fora.append(item_sort)

    estado['fora'] = sorteio_fora.copy()

    return estado
    # print(estado)

def percorre(estado):
    if len(estado['fora']) < 1:
        return sum(item["valor"] for item in estado["dentro"])  
    item_first = estado['fora'].pop(0)
    cap_aux = sum(item["peso"] for item in estado["dentro"])
    cap_aux += item_first['peso']
    if secrets.randbelow(2) and cap_aux <= capacidade:
        estado['dentro'].append(item_first)
    # else:
    #     estado['fora'].append(item_first)
        
    
    return sum(item["valor"] for item in estado["dentro"])

for x in range(num_estados):
    estados.append(sorteiaEstado())

print("=====================")
print("===Estados criados===")
print("=====================") 

melhor = {
    'num_estado': 0,
    'valor': 0,
    'itens': []
}
aux_melhor = 0;
c = 0;
while True: 
    for i in range (len(estados)):
        # print(estados[i])
        # print(f"- {c} -")
        valor_estado = sum(item["valor"] for item in estados[i]["dentro"])
        deltaE = percorre(estados[i])
        if valor_estado > melhor['valor']:
            melhor['num_estado'] = i
            melhor['valor'] = valor_estado
            melhor['itens'] = estados[i]['dentro'].copy()
            c = 0
            
        if deltaE == valor_estado:
            # print(f"/////////////// ANTES //////////////////////////////")
            # print(estados[i])
            estados[i] = sorteiaEstado()
            # print(f"/////////////// DEPOIS /////////////////////////////")
            # print(estados[i])
            # print(estados)
            
            valor_estado = 0
        
    
    c += 1
    # print(f"Contagem: {c} | Melhor estado: {melhor['num_estado']} | Valor: {melhor['valor']}")
    # print(melhor['itens'])
    # print(f"===========================================")
    if c >= 1000:
        print(f"FIM")
        break

print(f"Contagem: {c} | Melhor estado: {melhor['num_estado']} | Valor: {melhor['valor']}")
print(melhor['itens'])
print(f"===========================================")


