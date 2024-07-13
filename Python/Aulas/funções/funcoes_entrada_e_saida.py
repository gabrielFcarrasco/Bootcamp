#input recebe argumentos do usurario, que ira ser adicinado como valor na variavel
nome = input('Digite o seu nome: ')
idade = input('Digite sua idade: ')

print(nome, idade, end=" \n")
print(nome, idade, sep="#")
#teste
print(type(nome))
print(type(idade))

#todo input recebe e retorna o valor como string
#para travalhar com os números recebidos pelo input devemos converte-los
idade = int(idade)

#novo teste
print(type(nome))
print(type(idade))



