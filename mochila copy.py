import secrets
import math

itens = [
    {'valor': 5, 'peso': 5},
    {'valor': 2, 'peso': 2},
    {'valor': 4, 'peso': 1},
    {'valor': 3, 'peso': 4},
    {'valor': 9, 'peso': 3},
    ]

capacidade = 10
estados = []
num_estados = 3;

def atualizaCapacidade(estado):
    cap = 0
    for i in range(len(itens)):
        if estado[i] == 1:
            cap += itens[i]['peso']
    return cap

def sorteiaEstado():
    estado = []  
    for i in range(len(itens)):
        if secrets.randbelow(2):
            estado.append(1)
        else:
            estado.append(0)

    cap_aux = atualizaCapacidade(estado)
    while cap_aux > capacidade:
        rand = secrets.randbelow(5)
        if estado[rand] == 1:
            estado[rand] = 0
            cap_aux -= itens[rand]['peso']

    # print(estado)
    # print(f'capacidade: {cap_aux}')
    # print(f'=====================')
    return estado

def sucessorAtual(atual):
    index = secrets.randbelow(5);
    if atual[index] == 1:
        atual[index] = 0;
    else:
        atual[index] = 1;
    return atual

def calcValor(estado):
    val = 0
    for i in range(len(itens)):
        if estado[i] == 1:
            val += itens[i]['valor']
    return val
    
def calcDelta(proximo, atual):
    delta = calcValor(proximo) - calcValor(atual);
    return delta;    

def Temp():
    t = 0;
    T = 1000;
    resp = {
        'estado': [],
        'valor': 0,
        'peso': 0,
    };
    estado_atual = sorteiaEstado()

    while True:
        T -= 1;
        if T == 0:
            return resp;
        estado_proximo = sucessorAtual(estado_atual.copy());
        deltaE = calcDelta(estado_proximo, estado_atual);
        if deltaE > 0:
            estado_atual = estado_proximo;
        else:
            n = secrets.randbelow(101);
            if n < math.exp(deltaE/T):
                estado_atual = estado_proximo;
        
        t += 1;


while False: 
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
    
    c += 1
    # print(f"Contagem: {c} | Melhor estado: {melhor['num_estado']} | Valor: {melhor['valor']}")
    # print(melhor['itens'])
    # print(f"===========================================")
    if c >= 1000:
        print(f"FIM")
        break

print(Temp());
