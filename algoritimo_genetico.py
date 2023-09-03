import secrets
import random
import math

itens = [
    {'valor': 5, 'peso': 5},
    {'valor': 2, 'peso': 2},
    {'valor': 4, 'peso': 2},
    {'valor': 3, 'peso': 3},
    {'valor': 9, 'peso': 4},
    ]
capacidade = 10
tam_populacao = 6;

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

def geraPopulacao(k):
    populacao = [];
    for est in range(k): 
        populacao.append(sorteiaEstado());
    return populacao

def calcValor(estado):
    val = 0
    for i in range(len(estado)):
        if estado[i] == 1:
            val += itens[i]['valor']
    return val

def escalonaT(t):
    T = 100 * math.exp(-0.001 * t)
    if T < 1:
        T = 0
    return T

def selecaoRoleta(populacao):
    probabilidade = [];
    valorTotal = 0
    for ind in populacao:
        valorTotal += calcValor(ind)

    for ind in populacao:
        prob = calcValor(ind)/valorTotal
        probabilidade.append(prob)
    
    escolhido = random.choices(populacao, probabilidade, k=1)[0]
    return escolhido

def reproduz(ind1, ind2, i):
    filho = ind1[:i] + ind2[i:];
    return filho

def mutacao(ind):
    i = secrets.randbelow(len(ind));
    ind[i] = 0 if ind[i]==1 else 1;    
    return ind;

def controlePopulacao(populacao):

    return populacao

def algoritmoGenetico(populacao):
    t = 0;
    while True:
        pop_aux = [];
    
        for i in range(len(populacao)):
            ind1 = selecaoRoleta(populacao);
            ind2 = selecaoRoleta(populacao);
            i = secrets.randbelow(len(ind1));
            filho1 = reproduz(ind1, ind2, i);
            filho2 = reproduz(ind2, ind1, i);
            if secrets.randbelow(101) < 5:
                filho1 = mutacao(filho1);
            if secrets.randbelow(101) < 5:
                filho2 = mutacao(filho2);
            pop_aux.append(filho1);
            pop_aux.append(filho2);
        
        populacao = pop_aux
        if t >= 50:
            break;
        t += 1;


melhor = algoritmoGenetico(geraPopulacao(tam_populacao));
print(f'Melhor estado: {melhor}')
print(f"Valor: {calcValor(melhor)} | Peso: {atualizaCapacidade(melhor)}");

