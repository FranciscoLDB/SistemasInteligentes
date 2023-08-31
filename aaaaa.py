import secrets

itens = [
    {'valor': 1, 'peso': 1},
    {'valor': 2, 'peso': 2},
    {'valor': 3, 'peso': 3},
    {'valor': 4, 'peso': 4},
    {'valor': 5, 'peso': 5},
    ]

for i in range(len(itens)):
    print(i)

aux = itens[2]
aux['valor'] = 222

print(aux)
print(itens[2])

for tp in range(10, 1, -1):
    print(tp);

print('');
print(secrets.randbelow(5))