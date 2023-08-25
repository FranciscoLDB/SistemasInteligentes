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