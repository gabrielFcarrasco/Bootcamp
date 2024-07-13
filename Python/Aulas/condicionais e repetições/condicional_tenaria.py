#boa para manutenções do codigo, cria uma condição feita em uma unica linha composto por três partes

saldo = 2000.00
saque = 500.00

status = 'Sucesso' if saque < saldo else 'Falha'

print(f'{status} ao realizar o saque!')