def cadastro():
    while True:
        try:
            nome = input('Digite seu nome completo: ')
            senha1 = input('Digite sua senha: ')
            senha2 = input('Confirme sua senha: ')
            if senha1 != senha2:
                print('As senhas não coincidem, tente novamente')
                print('='*30)
            else:
                print('Cadastro efetuado com sucesso')
                print('='*30)
                break
        except:
            print('Erro')

def sacar(valor = 0, total = 0, cart = 0):
    tot = total - valor
    cart = valor
    return tot,cart
def deposito(valor=0, total=0, cart=0):
    tot = total + valor
    cart -= valor
    return tot,cart
def banco():
    extrato = []
    """
    Documentação da função banco:
    Função Confusa, está funcionando e não tente mecher nela para não parar de funcionar. Assinado por lberasz...
    """
    tot = 100000
    cart = 0    
    while True:
        print('='*30)
        print('O que você gostária de fazer hoje? ')
        print('1 - Ver Saldo')
        print('2 - Sacar')
        print('3 - Depositar ')
        print('4 - Transferir')
        print('5 - Ver Extrato')
        print('6 - Sair ')
        op = int(input('Sua Opção: '))
        if op == 1:
            try:
                print('='*30)
                print(f'O saldo em sua conta é: R${tot}')
                print(f'E você tem R${cart} em sua carteira')
            except:
                print('Ocorreu um erro!')
        elif op == 2:
            try:
                print('='*30)
                qnt = float(input('Quanto você quer sacar: '))
                if qnt <= tot:
                    sc = sacar(qnt,tot,cart)
                    print(f'Agora seu saldo é de: {sc[0]}')
                    print(f'E você tem R${sc[1]} em sua carteira')
                    tot = sc[0]
                    cart = sc[1]
                else:
                    print('Saldo indisponivel')
                    print(f'Você tem R${tot} disponiveis para saque')
            except:
                print('Digite um numero racional valido')
        elif op == 3:
            try:
                print('='*30)
                qnt = float(input('Quanto você quer depositar: '))
                if qnt <= cart:
                    dp = deposito(qnt, tot, cart)
                    print(f'Agora seu saldo é de: {dp[0]}')
                    print(f'E você tem R${dp[1]} em sua carteira')
                    tot = dp[0]
                    cart = dp[1]
                else:
                    print('Saldo indisponivel')
                    print(f'Você tem R${cart} disponiveis para deposito')
            except:
                print('Digite um numero racional valido')
        elif op == 4:
            print('='*30)
            qm = input('Para quem você quer transferir: ')
            try:
                qnt = float(input('Quanto você quer transferir: '))
                if qnt <= tot:
                    tot -= qnt
                    print(f'Você transferiu R${qnt} para {qm}\nAgora seu saldo é de: {tot}')
                    extrato.append(qm)
                    extrato.append(qnt)
                    #Par Nome Impar Quantia
                else:
                    print('Saldo indisponivel')
                    print(f'Você tem R${tot} disponiveis para transferencia')
            except:
                print('Digite um numero racional valido')
        elif op == 5:
            print('='*30)
            for pos, val in enumerate(extrato):
                if pos % 2 == 0:
                    print(f'{val} - ', end='')
                else:
                    print(f'R${val}')
        elif op == 6:
            break
        else:
            print(f'A opção {op} é invalida.')
            print('='*30)