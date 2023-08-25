import random

itens = [
    {'valor': 5, 'peso': 5},
    {'valor': 2, 'peso': 2},
    {'valor': 7, 'peso': 8},
    {'valor': 3, 'peso': 4},
    ]

capacidade = 15
estados = []
num_estados = 3;

def sorteiaEstado(estado):
    if len(estado['fora']) < 1:
        return
    
    cap_aux = sum(item["peso"] for item in estado["dentro"])
    sorteio_fora = []
    while len(estado['fora']) > 0:
        item_sort = estado['fora'].pop(random.randint(0, len(estado['fora'])-1))
        cap_aux += item_sort['peso']
        if random.randint(0, 1) and cap_aux <= capacidade:
            estado['dentro'].append(item_sort)
        else:
            cap_aux -= item_sort['peso']
            sorteio_fora.append(item_sort)

    estado['fora'] = sorteio_fora.copy()
    # print(estado)

def percorre(estado):
    if len(estado['fora']) < 1:
        return    
    item_sort = estado['fora'].pop(random.randint(0, len(estado['fora'])-1))
    cap_aux = sum(item["peso"] for item in estado["dentro"])
    cap_aux += item_sort['peso']
    if cap_aux <= capacidade:
        estado['dentro'].append(item_sort)
    else:
        estado['fora'].append(item_sort)

for x in range(num_estados):
    estado = {'dentro': [], 'fora': itens.copy()}
    sorteiaEstado(estado)
    estados.append(estado)
    print(f"---------------------------| estado {x} |---------------------------")
    print(estado)
    print("")

print("===========================================")
print("==============Estados criados==============")
print("===========================================") 

melhor = {
    'num_estado': 0,
    'valor': 0
}
aux_melhor = 0;
c = 0;
while True:
    for estado in estados:
        percorre(estado)
        valor_estado = sum(item["valor"] for item in estado["dentro"])
        if valor_estado > melhor['valor']:
            melhor['num_estado'] = estados.index(estado)
            melhor['valor'] = valor_estado 

    if aux_melhor == melhor['valor']:
        c += 1
    else:
        aux_melhor = melhor['valor']
        c = 0
    
    print(f"Contagem: {c} Melhor estado: {melhor['num_estado']} | Valor: {melhor['valor']}")
    print(f"===========================================")
    
    if c >= 5:
        break




