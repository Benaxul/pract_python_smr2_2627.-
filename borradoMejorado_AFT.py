import random

notas = []

while len(notas) < 100:
    nota = random.randint(0, 10)
    notas.append(nota)

print("En mi lista tengo", notas.count(0), "ceros.")

# Nos quedamos solo con los elementos distintos de 0
notas = [n for n in notas if n != 0]

print(len(notas), notas)