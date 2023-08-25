import random

if random.randint(0, 1): 
    print("True!!!")
else:
    print("False!!!")

val = [1, 2, 3, 4]

print(val)
val.pop()
print(val)
val.append(6)
print(val)
val.pop()
print(val)
val.pop()
print(val)

my_list = [10, 20, 30, 40, 50]
index_to_remove = 2  # índice do elemento a ser removido

if 0 <= index_to_remove < len(my_list):
    removed_item = my_list.pop(index_to_remove)
    print(f"Item removido: {removed_item}")
else:
    print("Índice inválido")

print(my_list)
