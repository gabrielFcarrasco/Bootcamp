#Strings de multiplas linhas são definidas com 3 aspas simples ou duplas, e elas podem oculpar varias linhas do codigo,e todos os espaços em branco são incluidos na string final.

nome = "Gabriel"
mensagem = f'''
    Olá, me chamo {nome},
    e estou aprendendo python
        essa mensagem tem recuos diferentes
'''
print(mensagem)

print('''
      ------------Menu------------

      [1] Sacar
      [2] Extrato
      [0] Sair
      
      -----------------------------
        Obrigado Por Usar o Sistema
      ''')