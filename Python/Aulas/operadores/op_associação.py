#Os operadores de associação são operadores que verificam se um objeto está presente na sequencia

curso = 'curso em python'
frutas = ['banana', 'abacaxi', 'pera']
saques = [1000, 500, 340]

print('-----------------------')
print('          in           ')
print('-----------------------')
print('python' in curso)#será verdadeiro pq tem a palavra dentro dessa vairavel
print('banana' in frutas)#será verdadeiro
print('javascript' in curso)#será falso pois não tem essa palavra na variavel curso
print('-----------------------')
print('        in not         ')
print('-----------------------')
print('maçã' not in frutas)#não tem maçã na variavel frutas então aparecerá true pois o NOT busca se não tem o valor na variavel
print(200 not in saques)#aparecerá true pois não tem 200 na variavel
print(500 not in saques)#aparecerá false pois tem 500 em saques