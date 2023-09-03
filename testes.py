import secrets

itens = [
    {'valor': 1, 'peso': 1},
    {'valor': 2, 'peso': 2},
    {'valor': 3, 'peso': 3},
    {'valor': 4, 'peso': 4},
    {'valor': 5, 'peso': 5},
    ]

# for i in range(len(itens)):
#     print(i)

# aux = itens[2]
# aux['valor'] = 222

# print(aux)
# print(itens[2])

# for tp in range(10, 1, -1):
#     print(tp);

# print('');
# print(secrets.randbelow(5))
def atualizaCapacidade(estado):
    cap = 0
    for i in range(len(itens)):
        if estado[i] == 1:
            cap += itens[i]['peso']
    return cap

capacidade = 10;
atual = [1, 1, 0, 0];
vet_aux = [];
for x in range(len(itens)): vet_aux.append(x);
index = vet_aux.pop(secrets.randbelow(len(vet_aux)));
print(len(vet_aux));
while len(vet_aux) > 1:
    if atual[index] == 1:
        if atualizaCapacidade(atual) < capacidade:
            atual[index] = 0;
            break;
    else:
        atual[index] = 1;
        break;

import secrets
lista = [1, 2, 3, 4, 5]
print(lista)
for x in range(len(lista)):
    x = lista.pop(secrets.randbelow(len(lista)))
    print(x)
    print(lista)


for elemento in lista:
    print(elemento)

veta = [2, 3, 4, 8, 7]
vetb = [10, 20, 9, 5, 6]
print(veta)
print(vetb)
c = 3;
aux = veta[:c] + vetb[c:]
print(aux)

import random

# Vetor de elementos com probabilidades
elementos = ['A', 'B', 'C', 'D']
probabilidades = [0.1, 0.3, 0.2, 0.4]

# Realizar o sorteio ponderado
escolha = random.choices(elementos, probabilidades, k=1)[0]

# Exibir o resultado
print(f'O elemento escolhido foi: {escolha}')
