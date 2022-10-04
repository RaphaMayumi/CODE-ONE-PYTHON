idade = int(input('Qual é a sua idade? '))

if idade >= 18: # OS DOIS PONTOS NO FINAL É EXTREMAMENTE IMPORTANTE POIS É LIDO COMO "ENTÃO"..... "SE IDADE FOR MAIOR OU IGUAL A 18 ENTÃO"
    print('Você é maior de idade!') # OS 4 ESPAÇOS(IDENTAÇÃO) SÃO GERADOS AUTOMÁTICAMENTE POIS TUDO EM QUE SE ENCONTRAR NESTA POSIÇÃO, SERÁ EXECUTADO NESTA CONDIÇÃO
else: # É DE EXTREMA IMPORTANCIA QUE OS 4 ESPAÇOS SEJAM RETIRADOS E APÓS O ELSE, SER ADICIONADO OS DOIS PONTOS
    print('Você é menor de idade!')



nota = float(input('Qual foi sua nota em Inglês? '))

if nota >= 7:
    print('Aprovado')
elif nota >= 5: # EQUIVALENTE A UM ELSE IF, SERIA UMA TERCEIRA CONDIÇÃO
    print('Recuperação')
else:
    print('Reprovado')


nota2 = float(input('Qual foi sua nota em Inglês? '))
presenca = int(input('Qual foi a porcentagem (número inteiro) de presença obtida? '))

if nota2 >= 7 and presenca >= 70: # AS DUAS CONDIÇÕES DEVEM SER OBRIGATÓRIAMENTE VERDADEIRAS, CASO DESEJE APENAS UMA, UTILIZAR "OR"
    print('Aprovado')
else:
    print('Reprovado')