f =  int(input('Informe um número para a sequencia de Fibonate'))
num = 500
ant = 0
prox = 1
soma = 1
for n in range (0, 501):
    print (ant)
    soma = prox + ant
    ant = prox
    prox = soma
