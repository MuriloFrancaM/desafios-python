aux = False

while not aux:
    chave = (input ('Digite sua senha: '))
    if chave != 'python123':
        print ('senha incorreta')
    else:  
        print('Você acertou!') 
        aux=True