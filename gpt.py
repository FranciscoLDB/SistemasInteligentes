import random

# Definir os parâmetros do problema
capacidade_mochila = 20
numero_de_itens = 15
maximo_de_candidatos = 50  # Número máximo de candidatos a serem mantidos em cada iteração

# Gerar os itens com valores e pesos aleatórios
itens = [
    {'valor': 5, 'peso': 5},
    {'valor': 2, 'peso': 2},
    {'valor': 7, 'peso': 8},
    {'valor': 3, 'peso': 42},
    {'valor': 8, 'peso': 2},
    {'valor': 5, 'peso': 6},
    {'valor': 6, 'peso': 3},
    {'valor': 4, 'peso': 1},
    {'valor': 5, 'peso': 8},
    {'valor': 7, 'peso': 27},
    {'valor': 3, 'peso': 4},
    {'valor': 4, 'peso': 6},
    {'valor': 2, 'peso': 2},
    {'valor': 3, 'peso': 5},
    {'valor': 9, 'peso': 3},
    ]

def avaliar_solucao(solucao):
    return sum(item['valor'] for item, escolhido in zip(itens, solucao) if escolhido)

# Inicializar o feixe com uma solução aleatória
feixe = [[random.choice([True, False]) for _ in range(numero_de_itens)] for _ in range(maximo_de_candidatos)]

# Número máximo de iterações
numero_de_iteracoes = 10

for _ in range(numero_de_iteracoes):
    novos_candidatos = []

    for candidato in feixe:
        for i in range(numero_de_itens):
            novo_candidato = candidato.copy()
            novo_candidato[i] = not novo_candidato[i]  # Inverter o estado do item
            novos_candidatos.append(novo_candidato)

    novos_candidatos.sort(key=lambda sol: -avaliar_solucao(sol))  # Ordenar candidatos por valor decrescente
    feixe = novos_candidatos[:maximo_de_candidatos]  # Manter os melhores candidatos

# Encontrar a melhor solução após todas as iterações
melhor_solucao = max(feixe, key=avaliar_solucao)
valor_melhor_solucao = avaliar_solucao(melhor_solucao)

print("Itens escolhidos:", melhor_solucao)
print("Valor total:", valor_melhor_solucao)
