import os
import time

caixa = 10
nome = ('')

while True:
    os.system('cls' if os.name == 'nt' else 'clear')
    print('Olá, seja bem vindo ao ATM ')
    print('--------------------')
    nome = input('Qual seu nome? ')

    while True:
            print(nome, 'O que deseja fazer?')
            print('...')
            print('...')
            option = int(input('1 - SACAR --- 2 - DEPOSITAR --- 3 - SALDO DO CAIXA --- 4 - SAIR >>> '))

            if option == 1:
                print("SAQUE")
                valor_saque = int(input('Qual o valor do seu saque? >>>'))
                print('Realizando o saque...')
                print('...')
                time.sleep(1)
                print('...')
                time.sleep(1)
                print('...')
                time.sleep(1)
                print('...')
                caixa -= valor_saque
                print(f'Saque realizado, o saldo atual do ATM é de', caixa, 'Unidades')


            elif option == 2:
                print('DEPÓSITO')
                valor_deposito = int(input('Quantas unidades deseja depositar >>>?'))
                print('Realizando o depósito...')
                print('...')
                time.sleep(1)
                print('...')
                time.sleep(1)
                print('...')
                time.sleep(1)
                print('...')
                caixa += valor_deposito
                print(f'O valor de {valor_deposito} foi depositado')
                print('O SALDO DO CAIXA É DE', caixa, 'Unidades')


            elif option == 3:
                print('O saldo do ATM é de ', caixa, 'Unidades')

            elif option == 4:
                print('...')
                print('...')
                print('Obrigado por usar nosso sistema!')
                break

            else:
                print('Opção Incorreta, escolha novamente')
