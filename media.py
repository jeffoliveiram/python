m1 = float(input('Informe a primeira nota:'))
m2 = float(input('Informe a segunda nota:'))
media = (m1 + m2 ) / 2
conceito = [ 'A' , 'B', 'C', 'D', 'E' ]
if media > 9.0 and media <= 10:
    print ( 'Nota das provas: {:.1f} E {:.1f}'.format( m1 , m2 ))
    print ( 'sua media: {:.1f}'.format(media))
    print ( 'Seu conceito é: {}'.format(conceito[0]))
    print (  'Você foi APROVADO ')
elif media > 7.5 and media <= 9.0:
    print('Nota das provas: {:.1f} E {:.1f}'.format(m1, m2))
    print('sua media: {:.1f}'.format(media))
    print('Seu conceito é: {}'.format(conceito[1]))
    print('Você foi APROVADO ')
elif media > 6.0 and media <= 7.5:
    print('Nota das provas: {:.1f} E {:.1f}'.format(m1, m2))
    print('sua media: {:.1f}'.format(media))
    print('Seu conceito é: {}'.format(conceito[2]))
    print('Você foi APROVADO ')
elif media > 4.0 and media <= 6.0:
    print('Nota das provas: {:.1f} E {:.1f}'.format(m1, m2))
    print('sua media: {:.1f}'.format(media))
    print('Seu conceito é: {}'.format(conceito[3]))
    print('Você foi Reprovado ')
else:
    print('Nota das provas: {:.1f} E {:.1f}'.format(m1, m2))
    print('sua media: {:.1f}'.format(media))
    print('Seu conceito é: {}'.format(conceito[4]))
    print('Você foi Reprovado ')



