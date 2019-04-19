dia = int(input('Informe um número para saber o dia da semana:'))
semana = ['1 - Domingo', '2 - Segunda', '3 - Terça', '4 - Quarta', '5 - Quinta', '6 - Sexta', '7 - Sabado']

if dia == 1:
    print('O dia da semana é: {}'.format (semana[0]))
elif dia == 2:
    print('O dia da semana é: {}'.format(semana[1]))
elif dia == 3:
    print('O dia da semana é: {}'.format(semana[2]))
elif dia == 4:
    print('O dia da semana é: {}'.format(semana[3]))
elif dia == 5:
    print('O dia da semana é: {}'.format(semana[4]))
elif dia == 6:
    print('O dia da semana é: {}'.format(semana[5]))
elif dia == 7:
    print ('O dia da semana é: {}'.format(semana[6]))
else:
    print ('Valor invalido')
