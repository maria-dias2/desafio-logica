menu = f"""

[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair

=> """

saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3

while True:
    opcao = input(menu)
    
    if opcao == "d":
        valor = float(input("Digite o valor do depósito: "))
        if valor > 0:
            valor += saldo
            extrato += f"Depósito: R${valor:.2f}\n"
        else:
            print("Valor inválido, por favor digite um valor maior que 0.")
        
    elif opcao == "s":
        valor = float(input("Digite o valor a sacar: "))
        
        excedeu_saldo = valor > saldo
        excedeu_limite = valor > limite
        excedeu_saques = numero_saques >= LIMITE_SAQUES
        
        if excedeu_saldo:
            print("Você não tem saldo suficiente!")
            
        elif excedeu_limite:
            print("O valor do sauque excede o limite!") 
            
        elif excedeu_saques:
            print("Limite de saques atingido!")
            
        elif valor > 0:
            saldo -= valor
            extrato == f"Saque: R${valor:.2f}\n"
        
        else:
            print("Operação inválida. Valor informado inválido")
    elif opcao == "e":
        print("\n--------------- EXTRATO -------------\n")
        print("Não foram realizadas movimentações." if not extrato else extrato)
        print(f"\nSaldo: R$ {saldo:.2f}")
        print("----------------------------------------")
        
    elif opcao == "q":
        break
    
    else:
        print("Operação inválida, por favor selecione a operação desejada.")