senhas = ['certo', '123', '456']
while True:
    senha = input('Digite uma senha: ')
    if senha in senhas:
        print('Acertou a senha.')
        break
    else:
        print('digitá-la novamente.')
        
