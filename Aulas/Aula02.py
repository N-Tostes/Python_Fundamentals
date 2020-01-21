# # Dicionarios

# time_favorito = {'Joao':'Corithians',
#                  'Rafael':'Cruzeiro',
#                  'Camila':'Palmerense'}


# carros = {'modelo01': {'Honda Fit': {'cor':'branco',
#                                      'motor':1.5, 
#                                      'ano':2015}
#                       },
#           'modelo02': {'Fiat Uno': {'cor': 'prata',
#                                     'motor':1.0,
#                                     'ano':2011}}
          
#           }


# print(time_favorito['Camila'])


# dados = {
#     'estados':{
#         'sp':{
#             'nome':'São Paulo',
#             'municipios': 645,
#             'populacao': 44.04
#         },
#         'rj':{
#             'nome':'Rio de Janeiro',
#             'municipios': 92,
#             'populacao': 16.72
#         },
#         'mg':{
#             'nome': 'Minas Gerais',
#             'municipios': 31,
#             'populacao': 20.87
#         }
#     }
# }

# # imprima as seguintes informações:

# # Padrão: Nome: nome_estado
#         # Municipios: y
#         # População: x

# # 1 - nomes dos estado

# # 2 - nomes dos estados e suas populaçoes em milhões

# # 3 - nomes dos estados e e seus municipios


# dados = {
#     'estados':{
#         'SP':{
#             'nome':'São Paulo',
#             'municipios':645,
#             'populacao':44.04
#         },
#         'RJ':{
#             'nome':'Rio de Janeiro',
#             'municipios':92,
#             'populacao':16.72
#         },
#         'MG':{
#             'nome':'Minas Gerais',
#             'municipios':31,
#             'populacao':20.87
#         }
#     }
# }
# for chave in dados['estados']:
#     print(type(dados['estados'][chave]['nome']))

#     #print('Nome: {} /n Municipio: {} /n Municipios: {} /n Populacao: {}'.format(dados['estados'][chave]['nome'],dados['estados'][chave]['municipios'],dados['estados'][chave]['populacao']))    
















#

# idade = int(input('Digite sua Idade:  '))
# #if=se comparar
# 

# if idade >= 18 
#     print('Você pode dirigir')
# else:
#     print('Você não pode dirigir')



#Repição

#  x = 1 

# while x < 10:
#     print('Número: {}'.format(x))
#      x += 1
# print('O wile acabou')

# frutas =  ['banana' ,'maça', 'uva', 'caju']

# for f in frutas:
#     print (f)

# for i in range(1,500):
#     print('i agora é {}' .format)


# try:
#     print('Isso é um erro' + 10)

#     #resolução do erro

# except Exception as e:

# try:
#     print(x) #variavel nao declarada 

#     #resolução do erro

# except NameError:
#     print('Variavel não declarada')


# try:
#     a = int(input('Digite um numero:'))
#     b = int(input('Digite outro numero:'))
#     print('a/b - {}'.format (a/b))
#     print('a+b = {}'.format(a+b))

#     except ValueError:
#         print('Valor incorreto')

#     except ZeroDivisionError:
#         print('Não podemos dividir por zero')

#     except Exception:
#         print('Erro desconhecido')


# usuarios = ['ana','carlos','maria','luis','paulo','leovandison']

# while True:
#     try:
#         login = input('Digite seu usuario:')

#         if login.lower() not in usuarios:
#             raise NameError('Usuario não cadastrado!')
#         else:
#             print('bem vindo {}'.format(login.capitalize))
#             break
#     except NameErroras n:
#         print(n)


try:
    x = int(input('Digite o primeiro numero:'))
    y = int(input('Digite o segundo numero'))
    print(x + y)
    


#Raise criação de erros novos 


    # v = int(input('Digite um valor':))
    # if v <10:
    #     raise ValueError('Vnão pode ser menos que 10')
    # else:
    #     print('OK')
    # except ValueError as v:
    #     print(v)


