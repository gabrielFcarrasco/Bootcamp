lista = [1, "Python", [40, 30, 20]]

copia_lista = lista.copy()

print(lista)  # [1, "Python", [40, 30, 20]]

copia_lista[0] = 2

print(lista)
print(copia_lista)