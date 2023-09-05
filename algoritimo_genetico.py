import secrets
import random
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
tam_populacao = 100;
historico = []

def atualizaCapacidade(estado):
    cap = 0
    for i in range(len(estado)):
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
    if atualizaCapacidade(estado) > capacidade:
        return -1
        
    return val

def selecaoRoleta(valorTotal, populacao, ignorar=-1):
    probabilidade = [];
    if (valorTotal == 0):
        return populacao[0]    
    for ind in populacao:
        prob = calcValor(ind)/valorTotal
        probabilidade.append(prob)

    vet_aux = []
    for x in range(len(populacao)): vet_aux.append(x);
    index = random.choices(vet_aux, probabilidade, k=1)[0]

    return index

def reproduz(ind1, ind2, i):
    filho = ind1[:i] + ind2[i:];
    return filho

def mutacao(ind):
    i = secrets.randbelow(len(ind));
    ind[i] = 0 if ind[i]==1 else 1;    
    return ind;

def algoritmoGenetico(populacao):
    t = 0;
    num_geracoes = 50
    for t in range(num_geracoes):
        filhos = [];
        rang = int(len(populacao)/2)
        #print(rang)
        #print(populacao)
        paisvalidos = []
        for ind in populacao:
            if calcValor(ind) >=0:
                paisvalidos.append(ind);
        
        for i in range(rang):
            valorTotal = 0            
            for ind in paisvalidos:
                valorTotal += calcValor(ind)
            ind1 = selecaoRoleta(valorTotal, paisvalidos);
            ind2 = selecaoRoleta(valorTotal, paisvalidos, ind1);

            i = secrets.randbelow(len(paisvalidos[ind1]));
            filho1 = reproduz(paisvalidos[ind1], paisvalidos[ind2], i);
            filho2 = reproduz(paisvalidos[ind2], paisvalidos[ind1], i);

            if secrets.randbelow(101) < 5:
                filho1 = mutacao(filho1);
            if secrets.randbelow(101) < 5:
                filho2 = mutacao(filho2);
            filhos.append(filho1);
            filhos.append(filho2);
        
        populacao = filhos

        media = 0;
        valido = 0;
        for filho in filhos:
            if atualizaCapacidade(filho) <= capacidade:
                media = media + calcValor(filho);
                valido += 1;
        media = int(round(media/valido))
        print(f'Geracao {t+1} | Media = {media}')
        historico.append(media)

    melhor = []
    for estado in populacao:
        if calcValor(estado) > calcValor(melhor) and atualizaCapacidade(estado) <= capacidade:
            melhor = estado
    return melhor;

melhor = algoritmoGenetico(geraPopulacao(tam_populacao));
print(f'Melhor estado: {melhor}')
print(f"Valor: {calcValor(melhor)} | Peso: {atualizaCapacidade(melhor)}");

#GERADOR DE GRAFICO
from matplotlib import pyplot
pyplot.plot(range(len(historico)), historico)
pyplot.grid(True, zorder=0)
pyplot.title("Problema da mochila - Algoritmo Genetico")
pyplot.xlabel("Num. Geracao")
pyplot.ylabel("Valor medio")
pyplot.show()

