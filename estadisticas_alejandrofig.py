notas = [7.5, 4.2, 9.0, 6.8, 0.0, 5.5, 8.3, 3.9]

print("Nota más alta:", max(notas))
print("Nota más baja:", min(notas))
print("Suma de las notas:", sum(notas))
print("Número de notas:", len(notas))
print("Nota media:", sum(notas) / len(notas))

# ¿Hay algún suspenso?
print("¿Hay algún suspenso?", any(nota < 5 for nota in notas))

# ¿No hay ningún cero?
print("¿No hay ningún cero?", all(nota != 0 for nota in notas))