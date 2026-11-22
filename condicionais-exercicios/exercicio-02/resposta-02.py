import os
import time

os.system("cls")

def GetValue(min, text):
    while True:
        try:
            value = float(input(text))
    
        except ValueError:
            print("Digite um valor numérico.")
            time.sleep(2)
            os.system("cls")
            continue
        
        if not min == None: 
            if value <= min:
                print(f"Digite um valor maior que {min}")
                time.sleep(2)
                os.system("cls")
                continue
        
        return value

salario = GetValue(0, "Insira o valor do seu salário: ")

if salario < 1500:
    print(f"Seu salário será reajustado para: R${salario + 200}")
else:
    print(f"Seu salário permanecerá sem ajuste: {salario}")