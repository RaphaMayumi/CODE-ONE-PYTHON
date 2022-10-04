# STRING + STRING = CONCATENAÇÃO DE DADOS 

num1 = '5'
num2 = '94'

print(num1 + num2)

# CASO FOR STRING + INT = DARÁ ERRO

# CONVERSÃO DE TIPOS

"""
    - int()
    - str()
    - float()
    - bool()
"""

idade = '21'

print(idade, type(idade))  # ALÉM DE APRESENTAR O VALOR DA VARIÁVEL, MOSTRA O TIPO DELA+

idade_int = int(idade)  # FOI CRIADO UMA NOVA VARIÁVEL RECEBENDO A CONVSAO DE idade PARA INT

print(idade_int, type(idade_int))


# CONVERSÃO NO INPUT

altura = float(input('Informe sua altura: ')) # VALORES DIGITADOS PELOS USUÁRIOS SEMPRE SÃO LIDOS COMO STRING A PRINCÍPIO

print(altura, type(altura))