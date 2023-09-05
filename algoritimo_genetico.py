import secrets
import random

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

#calcula o peso dos itens do estado passado
def atualizaCapacidade(estado):
    cap = 0
    for i in range(len(estado)):
        if estado[i] == 1:
            cap += itens[i]['peso']
    return cap

#sorteia um estado inicial de forma aleatória 
def sorteiaEstado():
    estado = []  
    for i in range(len(itens)):
        if secrets.randbelow(2):
            estado.append(1)
        else:
            estado.append(0)
    return estado

#gera k individuos
def geraPopulacao(k):
    populacao = [];
    for est in range(k): 
        populacao.append(sorteiaEstado());
    return populacao

#calcula o valor dos itens do estado passado
#!!Se capacidade invalida retorna -1
def calcValor(estado):
    val = 0
    for i in range(len(estado)):
        if estado[i] == 1:
            val += itens[i]['valor']
    if atualizaCapacidade(estado) > capacidade:
        return -1
        
    return val

#seleciona um individuo com probabilidade relacionada 
#ao seu valor comparado aos outros
def selecaoRoleta(valorTotal, populacao):
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

#retorna o filho de 2 individuos
def reproduz(ind1, ind2, i):
    filho = ind1[:i] + ind2[i:];
    return filho

#faz a mutacao do individuo
def mutacao(ind):
    i = secrets.randbelow(len(ind));
    ind[i] = 0 if ind[i]==1 else 1;    
    return ind;

#codigo principal do algoritmo genetico
def algoritmoGenetico(populacao):
    t = 0;
    num_geracoes = 50
    for t in range(num_geracoes):
        filhos = [];
        paisvalidos = []

        #seleciona os individuos que respeitam a capacidade maxima
        for ind in populacao:
            if calcValor(ind) >=0:
                paisvalidos.append(ind);
        
        #faz o processo de 1 geracao
        for i in range(int(len(populacao)/2)):
            #sorteia 2 individuos
            valorTotal = 0        
            for ind in paisvalidos:
                valorTotal += calcValor(ind)
            ind1 = selecaoRoleta(valorTotal, paisvalidos);
            ind2 = selecaoRoleta(valorTotal, paisvalidos);

            #reproduz 2 filhos dos 2 escolhidos
            i = secrets.randbelow(len(paisvalidos[ind1]));
            filho1 = reproduz(paisvalidos[ind1], paisvalidos[ind2], i);
            filho2 = reproduz(paisvalidos[ind2], paisvalidos[ind1], i);

            #pequena chance de mutar cada filho
            if secrets.randbelow(100) < 5:
                filho1 = mutacao(filho1);
            if secrets.randbelow(100) < 5:
                filho2 = mutacao(filho2);
            
            #guarda os filhos
            filhos.append(filho1);
            filhos.append(filho2);
        
        #troca a geracao atual pelos filhos gerados
        populacao = filhos

        #calcula a media da geracao e armazena para gerar o grafico
        media = 0;
        valido = 0;
        for filho in filhos:
            if atualizaCapacidade(filho) <= capacidade:
                media = media + calcValor(filho);
                valido += 1;
        media = int(round(media/valido))
        print(f'Geracao {t+1} | Media = {media}')
        historico.append(media)

    #retorna o melhor individuo da ultima geracao
    melhor = []
    for estado in populacao:
        if calcValor(estado) > calcValor(melhor) and atualizaCapacidade(estado) <= capacidade:
            melhor = estado
    return melhor;

#roda o algoritimo e mostra o melhor
melhor = algoritmoGenetico(geraPopulacao(tam_populacao));
print(f'Melhor estado: {melhor}')
print(f"Valor: {calcValor(melhor)} | Peso: {atualizaCapacidade(melhor)}");

#gera o grafico da media do valor de cada geracao
from matplotlib import pyplot
pyplot.plot(range(len(historico)), historico)
pyplot.grid(True, zorder=0)
pyplot.title("Problema da mochila - Algoritmo Genetico")
pyplot.xlabel("Num. Geracao")
pyplot.ylabel("Valor medio")
pyplot.show()

