def GetValue(min, max, v_type, text):
    while True:
        try:
            value = v_type(input(text))
    
        except ValueError:
            print("Digite um valor válido.")
            continue

        if not min == None and not max == None: 
          if not min <= value <= max:
                print(f"Digite uma valor entre {min} e {max}")
                continue
        elif max == None and not min == None: 
          if value < min:
                print(f"Digite uma valor maior ou igual a {min}")
                continue
        elif min == None and not max == None: 
          if value > max:
                print(f"Digite uma valor menor ou igual a {max}")
                continue
        
        return value

print("Sejam bem vindos Cauã, Miguel, João Vitor e Jonatha a maratona!")
print("Estão todos presentes? 0 = Não   1 = Sim\n")

caua = GetValue(0, 1, int, "Cauã está presente? ")
miguel = GetValue(0, 1, int, "Miguel está presente? ")
joao = GetValue(0, 1, int, "João Vitor está presente? ")
jonatha = GetValue(0, 1, int, "Jonatha está presente? ")

total = caua + miguel + joao + jonatha
pessoas = "amigos" if 4 - total > 1 else "amigo"

if total == 4:
  print("\nMaratona confirmada! Preparem a pipoca!")
else:
  print(f"\nOps... {4 - total} {pessoas} Estão faltando, fica pra próxima!")