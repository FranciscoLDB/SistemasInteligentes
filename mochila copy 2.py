import secrets
import math

itens = [
    {'valor': 5, 'peso': 5},
    {'valor': 2, 'peso': 2},
    {'valor': 4, 'peso': 2},
    {'valor': 3, 'peso': 3},
    {'valor': 9, 'peso': 4},
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
        if atual[index] == 0:
            atual[index] = 1;
            if atualizaCapacidade(atual) < capacidade:
                break;
            else:
                atual[index] = 0;
        else:
            atual[index] = 0;
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

def escalonaT(t):
    T = 100 * math.exp(-0.001 * t)
    if T < 1:
        T = 0
    return T

def buscaEmFeixe(k):
    estados = sorteiaEstado();
    for est in range(k): 
        est = []
        estados.append(est);
    t = 0;
    estado_atual = sorteiaEstado()
    while True:
        # print(estado_atual);
        # print(calcValor(estado_atual))
        # print(f"Valor: {calcValor(estado_atual)} | Peso: {atualizaCapacidade(estado_atual)}");
        T = escalonaT(t);
        # print(T)
        if T <= 0:
            return estado_atual;
        estado_proximo = sucessorAtual(estado_atual.copy());
        deltaE = calcDelta(estado_proximo, estado_atual);
        # print(f"deltaE: {deltaE}")
        if deltaE > 0:
            estado_atual = estado_proximo;
            # print("Melhoro!")
        else:
            n = secrets.randbelow(101)/100;
            # print(f"n: {n}  <  {math.exp(deltaE/T)}")
            if n < math.exp(deltaE/T):
                estado_atual = estado_proximo;
                # print("Pioro!")
            else:
                # print("Manteve!")
                t=t;
        
        t += 1;

media = 0;
vezes = 1000;
for x in range(vezes):
    R = Temp();
    # print("=============================================");
    # print(R);
    # print(f"Valor: {calcValor(R)}");
    # print(f"Peso: {atualizaCapacidade(R)}");
    media += calcValor(R);


