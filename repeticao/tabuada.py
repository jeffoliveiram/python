tabuada = int(input('Informe um número de 1 até 10 para calcular a tabuada: '))
print (' A tabuada do {} é:'.format(tabuada))
for t in range(1, 11):
    n = tabuada * t
    print ('{} X {} = {}'.format(tabuada,t, n ))



