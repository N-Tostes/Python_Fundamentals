#Software de imposto de renda 

# peça ao usuario o valor do salario mensal
# se o salario for maior ou igual que 4600, a aliquota é de 27
# se o salario for menor 4600 e maior que 3700, a aliquota é de 22
# se o salario for menor 3700 e maior que 2800, a aliquota é de 15
# se o salario for menor que 2800, aliquota é 0

# valor = salario * (aliquota / 100.0)

salario = flot(input('Digite o valor do seu salario Mensal:  '))

if salario >= 4600:
    print('Sua Aliquota é de 27')

elif salario < 4600 and salario >  3700:
    print('Sua Aliquota é de 22')

elif salario > 3700 and salario < 2800:
    print('Sua Aliquota é de 15')

elif salario < 2800:
    print('Sua Aliquota é de 0')

valor_aliquota = salario  * (aliquota / 100.0)

print('A aliquota do IR é de {}' .formate(valor_aliquota))