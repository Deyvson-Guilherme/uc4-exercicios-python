import os
os.system("cls")

ClienteInadimplente = 37

for i in range(1, 50):
    if i == ClienteInadimplente:
        print(f"Clente n°{i} inadimplente!")
        print("Buscador finalizado")
        break

    print(f"Clente n°{i} regular.")