hora = float (input('Informe o valor da sua hora:'))
trabalho = float (input('Informe o as horas trabalhadas:'))
calc = hora * trabalho
if calc <= 900:
    print('Trabalhador Isento')
    print ('Salário: R$ {:.2f}'.format(calc))
elif calc > 900 and calc <= 1500:
    print ('Salário Brunto: ({} * {})  : R$ {:.2f}'.format(hora, trabalho, calc))
    ir = (calc * 5) / 100
    print ('(-) IR (5%)                    : R$ {:.2f}'.format(ir))
    inss = (calc * 10 ) / 100
    print ('(-) INSS (10%)                 : R$ {:.2f}'.format(inss))
    fgts = (calc * 11 ) / 100
    print ('(-) FGTS (11%)                 : R$ {:.2f}'.format(fgts))
    total = (ir + inss)
    print ('Total de descontos             : R$ {:.2f}'.format(total))
    salario = ( calc - total )
    print ('Salário líquido                : R$ {:.2f}'.format(salario))
elif calc > 1500 and calc <= 2500:
    print('Salário Brunto: ({} * {})  : R$ {:.2f}'.format(hora, trabalho, calc))
    ir = (calc * 10) / 100
    print('(-) IR (10%)                    : R$ {:.2f}'.format(ir))
    inss = (calc * 10) / 100
    print('(-) INSS (10%)                 : R$ {:.2f}'.format(inss))
    fgts = (calc * 11) / 100
    print('(-) FGTS (11%)                 : R$ {:.2f}'.format(fgts))
    total = (ir + inss)
    print('Total de descontos             : R$ {:.2f}'.format(total))
    salario = (calc - total)
    print('Salário líquido                : R$ {:.2f}'.format(salario))
else:
    print('Salário Brunto: ({} * {})  : R$ {:.2f}'.format(hora, trabalho, calc))
    ir = (calc * 20) / 100
    print('(-) IR (20%)                    : R$ {:.2f}'.format(ir))
    inss = (calc * 10) / 100
    print('(-) INSS (10%)                 : R$ {:.2f}'.format(inss))
    fgts = (calc * 11) / 100
    print('(-) FGTS (11%)                 : R$ {:.2f}'.format(fgts))
    total = (ir + inss)
    print('Total de descontos             : R$ {:.2f}'.format(total))
    salario = (calc - total)
    print('Salário líquido                : R$ {:.2f}'.format(salario))








