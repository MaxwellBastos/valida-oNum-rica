from time import sleep
while True:
    def leiaInt(msg):
        ok = False
        valor = 0
        while True:
            n = str(input(msg))
            if n.isnumeric():
                valor = int(n)
                ok = True
            else:
                print('\033[0;31mErro! Só é permitido valor numérico.\033[m')

            if ok:
                break
        return valor

    n = leiaInt('Digite um número inteiro: ')
    print(f'O número digitado foi: {n}')
    cn = input('Deseja continuar? S/N ').strip().upper()[0]
    if cn == 'S':
        pass
    elif cn == 'N':
        print('Finalizando...')
        sleep(1)
        break
