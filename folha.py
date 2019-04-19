sal = float(input(' Informe o salário do trabalhador: R$'))
percentual = ['20%', '15%', '10%', '5%']
if sal <= 280:
    cal = ( (20 * sal) / 100 ) + sal
    print ('Salário antes do Reajuste: R$ {:.2f}'.format(sal))
    print ('Percentual do Aumento Aplicado: {}'.format(percentual[0]))
    print ('O valor do aumento é: R$ {:.2f}'.format(( (20 * sal) / 100 )))
    print ('Novo salário: R$ {:.2f}'.format(cal))
elif sal > 280 and sal <= 700:
    cal = ((15 * sal) / 100) + sal
    print('Salário antes do Reajuste: R$ {:.2f}'.format(sal))
    print('Percentual do Aumento Aplicado: {}'.format(percentual[1]))
    print('O valor do aumento é: R$ {:.2f}'.format(((15 * sal) / 100)))
    print('Novo salário: R$ {:.2f}'.format(cal))
elif sal > 700 and sal <= 1500:
    cal = ((10 * sal) / 100) + sal
    print('Salário antes do Reajuste: R$ {:.2f}'.format(sal))
    print('Percentual do Aumento Aplicado: {}'.format(percentual[2]))
    print('O valor do aumento é: R$ {:.2f}'.format(((10 * sal) / 100)))
    print('Novo salário: R$ {:.2f}'.format(cal))
else:
    cal = ((5 * sal) / 100) + sal
    print('Salário antes do Reajuste: R$ {:.2f}'.format(sal))
    print('Percentual do Aumento Aplicado: {}'.format(percentual[3]))
    print('O valor do aumento é: R$ {:.2f}'.format(((5 * sal) / 100)))
    print('Novo salário: R$ {:.2f}'.format(cal))



