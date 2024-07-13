# operadores de identidade são operadores são usdos para comparar se os dois objetos utilizados ocupam a mesma posição na memória

curso = 'curso em python'
nome_curso = curso
saldo, limite = 200, 200

print('-----------------------')
print('          is           ')
print('-----------------------')
print(    curso is nome_curso    )#aparecerá true pois os dois tem o mesmo valor no caso 'curso em python'
print(    saldo is limite    )#aparecerá true pois os dois tem o mesmo valor no caso 200
print('-----------------------')
print('         is not        ')
print('-----------------------')
print(curso is not nome_curso)#dará falso pois o NOT compara se os dois não tem o mesmo valor e no caso eles tem
saldo, limite = 500, 1000
print(saldo is not limite)#nesse caso dará true pois foi alterado seus valores
print('-----------------------')

