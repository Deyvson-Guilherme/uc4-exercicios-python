import os
import time

os.system("cls")

def GetValue(min, text):
    while True:
        try:
            value = float(input(text))
    
        except ValueError:
            print("Digite um nota válida.")
            time.sleep(2)
            os.system("cls")
            continue
        
        if value <= 0:
            print(f"Digite uma valor maior que {min}")
            time.sleep(2)
            os.system("cls")
            continue
        
        return value

print("Seja bem vindo ao banco do super soldado!\n")
valor = GetValue(0, "Insira o valor da transação: ")


if valor > 1000:
    print(f"Devido a transferência num alto valor (R${valor}) uma taxa de R$15 será aplicada\no valor total subtraído da sua conta será: R${valor + 15}")
else:
    print(f"Valor subtraído do seu saldo: R${valor}, sem taxas extras cobradas")
