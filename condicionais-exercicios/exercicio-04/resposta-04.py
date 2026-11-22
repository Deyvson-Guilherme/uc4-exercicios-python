import os
import time

os.system("cls") 

def GetValue(min, text):
    while True:
        try:
            value = int(input(text))
    
        except ValueError:
            print("Digite um valor válido.")
            time.sleep(2)
            os.system("cls")
            continue
        
        if not min == None: 
            if value < min:
                print(f"Digite uma valor maior que {min}")
                time.sleep(2)
                os.system("cls")
                continue
        
        return value

pontuacao = GetValue(0, "Parabéns pela jogatina, informe sua pontuação final: ")

if pontuacao >= 500:
    print(f"Bônus de pontução, seu score final é: {pontuacao + 100}")
else:
    print(f"Pontuação final {pontuacao}. Atinga 500 pontos para receber bônus de score!")