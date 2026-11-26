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

print("Bem vindos João, Lucas e Ithalo, vamos codar com rap!\n")

execucoes = GetValue(0, None, int, "Insira o número de execuções: ")

if execucoes == 0:
  print("Zero execuções, nenhuma música desbloqueada")
elif 0 < execucoes < 10:
  print(f"Execute {10 - execucoes} execuções para desbloquear músicas")
else: 
  quantidade = 5 * (execucoes // 10)
  print(f"Você desbloqueou {quantidade} músicas")