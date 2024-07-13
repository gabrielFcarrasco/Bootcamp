# BREAK no WHILE

#! serve para que 

while True:
    numero = int(input('informe um número: '))
    
    if numero == 10:
        break

    if numero % 2 == 0: #* nesse caso não exibirá quando for digitado um número par
        continue #! podemos usar o continue que pula o que nao queremos mostrar
    print(numero, end=" ")

