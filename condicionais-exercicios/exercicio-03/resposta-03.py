import os
import time

os.system("cls") 

def GetValue(text):
    while True:
        try:
            value = float(input(text))
    
        except ValueError:
            print("Digite um valor válido.")
            time.sleep(2)
            os.system("cls")
            continue
        return value

temp = GetValue("Insira a temperatura atual: ")

if temp > 35:
    print(f"Condição atingida, a temperatura irá subir para {temp + 5}")
else:
    print("Nenhuma condição específica atingida, a temperatura se manterá.")