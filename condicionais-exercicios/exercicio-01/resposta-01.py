import os
import time

os.system("cls")

def GetValue(min, text):
    while True:
        try:
            value = float(input(text))
    
        except ValueError:
            print("Digite um valor válido.")
            time.sleep(2)
            os.system("cls")
            continue
        
        if not min == None: 
            if value <= min:
                print(f"Digite uma valor maior que {min}")
                time.sleep(2)
                os.system("cls")
                continue
        
        return value


print("Bem vindo a loja do super soldado!\nDesconto em compras acima de R$200!\n ")

ValorDeCompras = GetValue(0, "Insira o valor em compras: ")

ValorFinal = ValorDeCompras - 30 if ValorDeCompras > 200 else ValorDeCompras

if ValorDeCompras > 200:
    print(f"desconto de R$30,00 aplicado!\nValor final a ser pago: R${ValorFinal}")
else:
    print(f"Valor final: R${ValorFinal}")