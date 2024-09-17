carros = ["gol", "celta", "palio"]

for carro in carros:
    print(carro)


for indice, carro in enumerate(carros): #* aparecerá enumerado os itens, sendo o indece o numerador
    print(f"{indice}: {carro}")
