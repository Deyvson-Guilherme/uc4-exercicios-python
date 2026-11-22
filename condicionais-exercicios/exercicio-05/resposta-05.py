import os
import time

os.system("cls")

def GetValue(min, text):
    while True:
        try:
            value = int(input(text))
    
        except ValueError:
            print("Digite um nota válida.")
            time.sleep(2)
            os.system("cls")
            continue
        
        if value < min:
            print("Digite uma valor positivo")
            time.sleep(2)
            os.system("cls")
            continue
        
        return value

print("Bem vindo ao sistema de estoque!\n")
produto = input("Insira o nome do produto que quer checar: ")
quantidade = GetValue(0, "Insira a quantidade existente em estoque: ")

if quantidade < 20:
    print(f"Temos apenas {quantidade} {produto} em estoque, um pedido automático \nfoi disparado e logo teremos {quantidade + 50} {produto} em estoque")
else:
    print(f"{quantidade} {produto} em estoque, quantidade regular")