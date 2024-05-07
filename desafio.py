""" 
Bootcamp DIO - Python AI Backend Developer.
Lab Project - Criando um sistema bancário com Python.

Objetivo geral: criar um sistema bancário com operações de saque, 
depósito e visualização de extrato.
"""

menu = """

==========================
[1] Depósito
[2] Saque
[3] Extrato
[4] Sair
==========================

=> """

saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3

while True:
    opcao = int(input(menu))

    if opcao == 1:
        valor = float(input("Por favor, informe o valor do depósito: "))

        if valor > 0:
            saldo += valor
            extrato += f"Depósito no valor de: R$ {valor:.2f}\n"
        else:
            print("Operação não realizada! O Valor informado inválido.")
    
    elif opcao == 2:
        valor = float(input("Por favor, informe o valor do saque: "))

        excedeu_saldo = valor > saldo
        excedeu_limite = valor > limite
        excedeu_saques = numero_saques >= LIMITE_SAQUES

        if excedeu_saldo:
            print("Operação não realizada! Saldo em conta insuficiente.")
        elif excedeu_limite:
            print("Operação não realizada! Limite máximo de saque: R$ 500,00.")
        elif excedeu_saques:
            print("Operação não realizada! Número máximo de saques excedido (3)!")

        elif valor > 0:
            saldo -= valor
            extrato += f"Saque realizado no valor de: R$ {valor:.2f}\n"
            numero_saques += 1
        else:
            print("Operação não realizada! Valor informado inválido.")

    elif opcao == 3:
        print("\n============== EXTRATO ==============")
        print("Nenhuma movimentação realizada." if not extrato else extrato)
        print(f"\nSalto atual: R$ {saldo:.2f}")
        print("=====================================")
    
    elif opcao == 4:
        print("Operação finalizada! Obrigado por utilizar nosso sistema!\n")
        break
        

    else:
        print("Operação inválida, por favor selecione a opção desejada.")