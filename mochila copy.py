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

    return estado

def sucessorAtual(atual):
    vet_aux = [];
    for x in range(len(itens)): vet_aux.append(x);
    while len(vet_aux) > 1:
        index = vet_aux.pop(secrets.randbelow(len(vet_aux)));
        print(len(vet_aux));
        if atual[index] == 0:
            if atualizaCapacidade(atual) < capacidade:
                atual[index] = 1;
                print('break!!!!!!!!!!!!');
                break;
            else:
                print('esto no else');
        else:
            atual[index] = 0;
            print('break!!!!!!!!!!!!');
            break;

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
            return estado_atual;
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

R = Temp();
print(R);
print(f"Valor: {calcValor(R)}");
print(f"Valor: {atualizaCapacidade(R)}");
