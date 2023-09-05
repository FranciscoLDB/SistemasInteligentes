import secrets
import math

itens = [
    {'valor': 5, 'peso': 5},
    {'valor': 10, 'peso': 2},
    {'valor': 4, 'peso': 2},
    {'valor': 3, 'peso': 3},
    {'valor': 7, 'peso': 4},
    {'valor': 5, 'peso': 2},
    {'valor': 20, 'peso': 5},
    {'valor': 7, 'peso': 7},
    {'valor': 10, 'peso': 4},
    ]

capacidade = 17
num_estados = 5;
historico = [];

#calcula o peso dos itens do estado passado
def atualizaCapacidade(estado):
    cap = 0
    for i in range(len(itens)):
        if estado[i] == 1:
            cap += itens[i]['peso']
    return cap

#sorteia um estado inicial de forma aleatória 
#!!nao permite estados que passem da capacidade maxima
def sorteiaEstado():
    estado = []  
    for i in range(len(itens)):
        if secrets.randbelow(2):
            estado.append(1)
        else:
            estado.append(0)

    cap_aux = atualizaCapacidade(estado)
    vet_aux = []
    for x in range(len(estado)): vet_aux.append(x);
    while cap_aux > capacidade:
        index = vet_aux.pop(secrets.randbelow(len(vet_aux)));
        if estado[index] == 1:
            estado[index] = 0
            cap_aux -= itens[index]['peso']

    return estado

#sorteia de forma aleatoria um estado sucessor do passado
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

#calcula o valor dos itens do estado passado
def calcValor(estado):
    val = 0
    for i in range(len(estado)):
        if estado[i] == 1:
            val += itens[i]['valor']
    return val

#calcula o delta de 2 estados
def calcDelta(proximo, atual):
    delta = calcValor(proximo) - calcValor(atual);
    return delta;    

#escalona a temperatura T
def escalonaT(t):
    T = 100 * math.exp(-0.007 * t)
    if T < 1:
        T = 0
    return T

#codigo principal da busca em feixe
def buscaEmFeixe(k = 1):
    #cria k estados iniciais
    estados = [];
    for est in range(k): 
        estados.append(sorteiaEstado());
    
    t = 0;
    while True:
        #escalona T em funcao de t
        T = escalonaT(t);
        if T <= 1:
            return estados;
    
        #varre o loop de estados
        for i in range(len(estados)):
            #pega um estado sucessor do atual e calcula o delta
            estado_proximo = sucessorAtual(estados[i].copy());
            deltaE = calcDelta(estado_proximo, estados[i]);

            #se delta positivo troca 
            
            if deltaE > 0:
                estados[i] = estado_proximo;
            else:
                #se delta negativo chance de trocar mesmo assim (maior no comeco / menor no final)
                n = secrets.randbelow(101)/100;
                if n < math.exp(deltaE/T):
                    estados[i] = estado_proximo;
        
        #quarda o melhor estado para gerar o grafico
        melhor = []
        for estado in estados:
            if calcValor(estado) > calcValor(melhor):
                melhor = estado
        historico.append(calcValor(melhor))

        t += 1;

Resp = buscaEmFeixe(num_estados);

#seleciona e mostra o melhor estado do resultado final
melhor = []
for estado in Resp:
    if calcValor(estado) > calcValor(melhor):
        melhor = estado
print(f'Melhor estado: {melhor}')
print(f"Valor: {calcValor(melhor)} | Peso: {atualizaCapacidade(melhor)}");

#gera o grafico de melhor valor em funcao dos passos
from matplotlib import pyplot
pyplot.plot(range(len(historico)), historico)
pyplot.grid(True, zorder=0)
pyplot.title("Problema da mochila - Busca em feixe")
pyplot.xlabel("Passos")
pyplot.ylabel("Melhor valor")
pyplot.show()

